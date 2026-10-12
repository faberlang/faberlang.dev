*Faber और ऑपरेटिंग सिस्टम द्वारा I/O लागू करने के हर तरीके के बीच का जोड़।*

`ad` Faber का निम्न-स्तरीय capability call primitive है — Faber कोड और बाहरी दुनिया के बीच की सीमा। यह route string से पहचाने गए host resource के साथ एक typed conversation (`sermo`) खोलता है, फिर directional half-streams के ज़रिए structured frames (`scrinium`) का आदान-प्रदान करता है। Host kernel हर route को एक pluggable provider crate तक भेजता है, जो वास्तविक I/O लागू करता है — filesystem, networking, console, time, randomness, या OS द्वारा किए जा सकने वाले किसी भी अन्य कार्य को।

## `ad` primitive {#ad}

`ad` एक keyword है, function नहीं। यह एक `ascii` literal द्वारा नामित route के साथ opaque conversation खोलता है और opener data वैकल्पिक होता है:

<<<FENCE 0>>>

Route string `prefix:verb` pattern का पालन करती है। Host kernel केवल **prefix** पर match करता है — उस prefix के अंतर्गत आने वाले सभी verbs का स्वामित्व provider के पास होता है:

<<<FENCE 1>>>

`ad` foreign function interface नहीं है। यह C functions को call नहीं करता, dynamic libraries load नहीं करता और inline assembly embed नहीं करता। यह structured message passing boundary है: Faber typed frames भेजता और typed frames प्राप्त करता है, बिना यह जाने कि provider Rust में implement किया गया है, in-process चलता है, system call को delegate करता है या remote host को forward करता है।

## Frame types {#types}

Compiler द्वारा स्वामित्व वाले पाँच types frame system बनाते हैं:

| Type | भूमिका | मुख्य surface |
|------|--------|---------------|
| `sermo` | Conversation handle — चल रहा bidirectional exchange | `ad` द्वारा बनाया जाता है; `↦ T` के ज़रिए drain किया जाता है या views में split किया जाता है |
| `scrinium<T>` | Frame envelope — conversation में एक structured message | Fields: `id`, `call`, `status`, `data`, `created_ms`, `from`, `trace` |
| `status` | Lifecycle marker enum | `request`, `item`, `byte`, `bulk`, `done`, `error`, `cancel` |
| `meus<T>` | Outbound half-stream — provider को frames भेजता है | `da(T)`, `fini() → status` |
| `tuus<T>` | Inbound half-stream — provider से frames प्राप्त करता है | `accipe()`, `cursor()`, `exhauri()`, `fini()` |

### Directional views का उपयोग {#using-directional-views}

<<<FENCE 2>>>

### सरल materialization {#simple-materialization}

सामान्य स्थिति में — open करना, opener भेजना और सभी response frames को एक value में drain करना — `sermo ↦ T` conversation को समेट देता है:

<<<FENCE 3>>>

Materialization एक type-directed collector का उपयोग करता है: `↦ textus` सभी inbound frames को concatenate करता है, `↦ json` concatenated payload को parse करता है और `↦ lista<T>` frames को एक list में collect करता है।

## Host providers {#providers}

Effect families को `faberlang/host-providers-rs` के अंतर्गत अलग-अलग provider crates के रूप में implement किया जाता है। प्रत्येक provider अपने prefix के अंतर्गत आने वाले सभी verbs का स्वामी होता है:

| Provider | Prefix | I/O domain |
|----------|--------|------------|
| `solum` | `solum:*` | Filesystem: read, write, metadata, directory operations |
| `processus` | `processus:*` | Process execution: spawn, pipe, exit codes |
| `consolum` | `consolum:*` | Console I/O: stdin, stdout, stderr |
| `tempus` | `tempus:*` | Time: now, sleep, timers |
| `aleator` | `aleator:*` | Randomness: entropy, distributions |
| `http` | `http:*` | HTTP client (Tier D, जब उपलब्ध होगा) |

Providers अलग-अलग crates हैं और उनकी dependencies भी अलग हैं — `solum` HTTP को pull in नहीं करता और `http` filesystem code को pull in नहीं करता। प्रत्येक provider एक `register()` function export करता है, जिसे generated host manifest startup पर call करता है।

## Layer stack {#layers}

<<<FENCE 4>>>

Compiler generic dispatch emit करता है — generated code में provider crate names कभी embed नहीं करता। Runtime `HostDispatch` और conversation protocol उपलब्ध कराता है। Kernel (`host-kernel-rs` से) prefix के आधार पर frames को सही provider तक route करता है। Provider (`host-providers-rs` से) वास्तविक I/O करता है।

इसका अर्थ है कि generated Faber code **provider-neutral** है। Compile manifest बदलकर उसी compiled binary को अलग-अलग provider implementations के साथ link किया जा सकता है — production के लिए real filesystem provider और testing के लिए mock provider।

## Compile manifest {#manifest}

कौन-से providers link किए जाएँगे, यह generated compile manifest और `faber.toml` की `[dispatch]` table नियंत्रित करते हैं:

<<<FENCE 5>>>

Authoring के दौरान missing providers runtime `E_NO_ROUTE` error उत्पन्न करते हैं। Strict mode में (भविष्य में), program में मौजूद हर `ad` prefix को compile manifest में दिखाई देना होगा और compiler यह validate करेगा कि provider का capability manifest उपयोग किए गए routes को cover करता है।

## Architecture {#architecture}

Host platform को `faberlang` organisation के तीन repositories में बाँटा गया है:

| Repository | भूमिका |
|------------|--------|
| `host-kernel-rs` | Thin router — `Frame`, `Conversation`, terminal lifecycle, prefix dispatch, structured errors (`E_NO_ROUTE`) और capability manifest aggregation का स्वामी |
| `host-native-rs` | Native attach — workers, `register_providers` startup hook और generated `host_register.rs` integration |
| `host-providers-rs` | Provider implementations — per-family crates (`solum`, `processus`, आदि) वाला Cargo workspace |

प्रत्येक provider crate अपनी native dependencies का स्वामी है। HTTP enabled होने पर `http` provider केवल तभी `hyper` और `tokio` pull in करता है। `solum` provider standard file APIs का उपयोग करता है और उसे किसी अतिरिक्त network dependencies की आवश्यकता नहीं होती।

> **एक ही route, कोई भी host।** क्योंकि `ad` route strings पर dispatch करता है और providers pluggable हैं, इसलिए वही Faber source native binary (`host-native-rs`), WASM runtime (Frame/Wasm adapter के रूप में host-kernel) या TypeScript Node.js process (`host-providers-ts`) को target कर सकता है, बिना Faber code की एक भी line बदले।

## Norma wrappers {#stdlib}

अधिकांश Faber code सीधे `ad` call नहीं करता। Norma standard library सामान्य `ad` routes को typed functions में wrap करती है:

<<<FENCE 6>>>

ये wrapper functions `ad` boundary के पार होने वाले I/O के तथ्य को छिपाए बिना type safety, documentation और error handling प्रदान करते हैं। Norma wrappers open source हैं और `norma/src/` के अंतर्गत रहते हैं।

## References {#references}

1. `radix/docs/design/frame-stream-types.md` — `sermo`, `scrinium`, `status`, `meus`, `tuus` की पूरी specification
2. `radix/docs/design/host-provider-gateway.md` — thin router architecture, provider contracts और compile manifest
3. `faberlang/host-kernel-rs/` — kernel router implementation
4. `faberlang/host-native-rs/` — native attach और registration
5. `faberlang/host-providers-rs/` — provider crates (`solum`, `processus`, `consolum`, `tempus`, `aleator`, `http`)
6. `examples/corpus/ad/` — `sermo` exempla files
