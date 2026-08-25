+++
title = "लक्ष्य संगतता"
section = "targets"
order = 2
sources = "faber/docs/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"

translation_kind = "translated"
prose_hash = "sha256:322b9815ff12d39b4582e47418cc07891c657b115a360a260fc70edf1414db1e"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "b392dba3ba0222bd15e6f28156522cff1571b475"
source_locale = "en-US"
+++

Faber एक भाषा है, जिसके संकलन अनुबंध अनेक हैं। यह पृष्ठ **मापी गई
lowerability matrix** है: corpus के प्रत्येक term के लिए यह बताता है कि कौन-से
लक्ष्य उसे किस support level पर lower कर सकते हैं।

नीति के क्रिया-शब्द (support / erase / warn / reject / defer) और pipeline routing
[Codegen targets](/tooling/codegen-targets.html) में हैं। यह पृष्ठ नीचे दी गई
tables में HIR application-lane targets और MIR systems-lane targets की साथ-साथ
दी गई, जल्दी पढ़ी जा सकने वाली row list है।

CLI का लाइव सारांश: `faber targets`।

**रेंडर किया गया**: unknown, `faber/scripta/render-matrices.py` द्वारा radix मापन JSON से — **संपादित न करें**।
**मापन**: `emit_hir_target_matrix` + `emit_mir_target_matrix` (in-process, बाहरी toolchains के बिना)।
**Join**: `corpus/index.toml` terms → exempla।

यह **आधिकारिक generated** grammar×target support matrix है। यह exempla corpus
के हर term के लिए **lowerability** रिपोर्ट करती है — क्या target X grammar
production Y को lower कर सकता है। Runtime semantics (erase/warn/defer policy
verbs), per-target contracts और pipeline routing
[Codegen targets](/tooling/codegen-targets.html) में हैं; वही दस्तावेज़ rows के
लिए इस पृष्ठ से link करता है।

## संकेत-सूची

| चिह्न | अर्थ |
|---|---|
| ✓ | पूर्ण समर्थन — term के सभी analyzable exempla lower होते हैं |
| ◐ | आंशिक — कुछ exempla lower होते हैं, कुछ में measured gap है |
| ○ | योजनाबद्ध — अभी lower नहीं होता; curated overlay (`scripta/ebnf-matrix-overrides.toml`) |
| ✕ | असमर्थित — कोई exempla lower नहीं होता; default truth के अनुसार measured gap वास्तविक है |
| — | मापा नहीं गया — इस lane पर term के लिए कोई analyzable exempla नहीं है |

> ✓ का अर्थ है कि इस term का उपयोग करने वाले corpus exempla target तक lower होते
> हैं। इसका अर्थ समान runtime semantics की गारंटी नहीं है। कुछ targets कुछ
> constructs को *erase* या *warn* करते हैं (उदाहरण के लिए Go borrow modes
> `de`/`in`/`ex` को erase करता है) — फिर भी वे यहाँ ✓ के रूप में दिखते हैं क्योंकि
> वे lower होते हैं। इस बारीकी के लिए policy doc देखें।

## Corpus-व्यापी सारांश (सभी पंजीकृत terms)

**एप्लिकेशन लेन (HIR → उत्सर्जित स्रोत भाषाएँ)**

| लक्ष्य | सक्षम | विश्लेषण योग्य | % |
|---|---|---|---|
| rust | 288 | 290 | 99% |
| go | 267 | 290 | 92% |
| ts | 290 | 290 | 100% |
| faber | 290 | 290 | 100% |

**सिस्टम लेन (MIR → डिवाइस/IR आर्टिफैक्ट)**

| लक्ष्य | सक्षम | विश्लेषण योग्य | % |
|---|---|---|---|
| llvm-text | 279 | 285 | 98% |
| wasm-text | 256 | 285 | 90% |
| wasm | 256 | 285 | 90% |
| sexp-struct | 223 | 285 | 78% |
| sexp | 223 | 285 | 78% |
| scena | 242 | 285 | 85% |

## कीवर्ड — एप्लिकेशन लेन

### कीवर्ड

| term | rust | go | ts | faber |
|---|---|---|---|---|
| <a id="abstractus"></a>`abstractus` | ✓ | ✓ | ✓ | ✓ |
| <a id="ab"></a>`ab` | ✓ | ✓ | ✓ | ✓ |
| <a id="ad"></a>`ad` | ✓ | ✕ | ✓ | ✓ |
| <a id="adfirma"></a>`adfirma` | ✓ | ✓ | ✓ | ✓ |
| <a id="ante"></a>`ante` | ✓ | ✓ | ✓ | ✓ |
| <a id="atomic"></a>`atomic` | ✕ | ✓ | ✓ | ✓ |
| <a id="argumenta"></a>`argumenta` | ✓ | ✓ | ✓ | ✓ |
| <a id="bivalens"></a>`bivalens` | ✓ | ✓ | ✓ | ✓ |
| <a id="cape"></a>`cape` | ✓ | ✓ | ✓ | ✓ |
| <a id="casu"></a>`casu` | ✓ | ✓ | ✓ | ✓ |
| <a id="cede"></a>`cede` | ✓ | ✓ | ✓ | ✓ |
| <a id="ceteri"></a>`ceteri` | ✓ | ✓ | ✓ | ✓ |
| <a id="ceterum"></a>`ceterum` | ✓ | ✓ | ✓ | ✓ |
| <a id="clausura"></a>`clausura` | ✓ | ✓ | ✓ | ✓ |
| <a id="cli"></a>`cli` | ✓ | ✓ | ✓ | ✓ |
| <a id="copia"></a>`copia` | ✓ | ✓ | ✓ | ✓ |
| <a id="cura"></a>`cura` | ✓ | ✓ | ✓ | ✓ |
| <a id="curata"></a>`curata` | ✓ | ✓ | ✓ | ✓ |
| <a id="cursor"></a>`cursor` | ✓ | ✓ | ✓ | ✓ |
| <a id="custodi"></a>`custodi` | ✓ | ✓ | ✓ | ✓ |
| <a id="de"></a>`de` | ✓ | ✓ | ✓ | ✓ |
| <a id="descriptio"></a>`descriptio` | ✓ | ✓ | ✓ | ✓ |
| <a id="discerne"></a>`discerne` | ✓ | ✓ | ✓ | ✓ |
| <a id="discretio"></a>`discretio` | ✓ | ✓ | ✓ | ✓ |
| <a id="dum"></a>`dum` | ✓ | ✓ | ✓ | ✓ |
| <a id="ego"></a>`ego` | ✓ | ✓ | ✓ | ✓ |
| <a id="elige"></a>`elige` | ✓ | ✓ | ✓ | ✓ |
| <a id="errata"></a>`errata` | ✓ | ✓ | ✓ | ✓ |
| <a id="est"></a>`est` | ✓ | ✓ | ✓ | ✓ |
| <a id="ex"></a>`ex` | ✓ | ✓ | ✓ | ✓ |
| <a id="exitus"></a>`exitus` | ✓ | ✓ | ✓ | ✓ |
| <a id="fac"></a>`fac` | ✓ | ✓ | ✓ | ✓ |
| <a id="falsum"></a>`falsum` | ✓ | ✓ | ✓ | ✓ |
| <a id="fient"></a>`fient` | ✓ | ✓ | ✓ | ✓ |
| <a id="fiet"></a>`fiet` | ✓ | ✓ | ✓ | ✓ |
| <a id="figendum"></a>`figendum` | ✓ | ✓ | ✓ | ✓ |
| <a id="finge"></a>`finge` | ✓ | ✓ | ✓ | ✓ |
| <a id="fiunt"></a>`fiunt` | ✓ | ✓ | ✓ | ✓ |
| <a id="fixum"></a>`fixum` | ✓ | ✓ | ✓ | ✓ |
| <a id="fragilis"></a>`fragilis` | ✓ | ✓ | ✓ | ✓ |
| <a id="fractus"></a>`fractus` | ✓ | ✓ | ✓ | ✓ |
| <a id="functio"></a>`functio` | ✓ | ✓ | ✓ | ✓ |
| <a id="futura"></a>`futura` | ✓ | ✓ | ✓ | ✓ |
| <a id="futurum"></a>`futurum` | ✓ | ✓ | ✓ | ✓ |
| <a id="generis"></a>`generis` | ✓ | ✓ | ✓ | ✓ |
| <a id="genus"></a>`genus` | ✓ | ✓ | ✓ | ✓ |
| <a id="iace"></a>`iace` | ✓ | ✓ | ✓ | ✓ |
| <a id="iacit"></a>`iacit` | ✓ | ✓ | ✓ | ✓ |
| <a id="ignotum"></a>`ignotum` | ✓ | ✓ | ✓ | ✓ |
| <a id="immutata"></a>`immutata` | ✓ | ✓ | ✓ | ✓ |
| <a id="implet"></a>`implet` | ✓ | ✓ | ✓ | ✓ |
| <a id="importa"></a>`importa` | ✓ | ✓ | ✓ | ✓ |
| <a id="in"></a>`in` | ✓ | ✓ | ✓ | ✓ |
| <a id="incipiet"></a>`incipiet` | ✓ | ✓ | ✓ | ✓ |
| <a id="incipit"></a>`incipit` | ✓ | ✓ | ✓ | ✓ |
| <a id="inter"></a>`inter` | ✓ | ✓ | ✓ | ✓ |
| <a id="intra"></a>`intra` | ✓ | ✓ | ✓ | ✓ |
| <a id="instans"></a>`instans` | ✓ | ✓ | ✓ | ✓ |
| <a id="itera"></a>`itera` | ✓ | ✓ | ✓ | ✓ |
| <a id="lege"></a>`lege` | ✓ | ✓ | ✓ | ✓ |
| <a id="lineam"></a>`lineam` | ✓ | ✓ | ✓ | ✓ |
| <a id="lista"></a>`lista` | ✓ | ✓ | ✓ | ✓ |
| <a id="matrix"></a>`matrix` | ✓ | ✕ | ✓ | ✓ |
| <a id="mone"></a>`mone` | ✓ | ✓ | ✓ | ✓ |
| <a id="mori"></a>`mori` | ✓ | ✓ | ✓ | ✓ |
| <a id="nexum"></a>`nexum` | ✓ | ✓ | ✓ | ✓ |
| <a id="nihil"></a>`nihil` | ✓ | ✓ | ✓ | ✓ |
| <a id="numquam"></a>`numquam` | ✓ | ✓ | ✓ | ✓ |
| <a id="numerus"></a>`numerus` | ✓ | ✓ | ✓ | ✓ |
| <a id="non"></a>`non` | ✓ | ✓ | ✓ | ✓ |
| <a id="omitte"></a>`omitte` | ✓ | ✓ | ✓ | ✓ |
| <a id="omnia"></a>`omnia` | ✓ | ✓ | ✓ | ✓ |
| <a id="operandus"></a>`operandus` | ✓ | ✓ | ✓ | ✓ |
| <a id="optio"></a>`optio` | ✓ | ✓ | ✓ | ✓ |
| <a id="optiones"></a>`optiones` | ✓ | ✓ | ✓ | ✓ |
| <a id="ordo"></a>`ordo` | ✓ | ✓ | ✓ | ✓ |
| <a id="octeti"></a>`octeti` | ✓ | ✓ | ✓ | ✓ |
| <a id="implendum"></a>`implendum` | ✓ | ✓ | ✓ | ✓ |
| <a id="per"></a>`per` | ✓ | ✓ | ✓ | ✓ |
| <a id="perge"></a>`perge` | ✓ | ✓ | ✓ | ✓ |
| <a id="postpara"></a>`postpara` | ✓ | ✓ | ✓ | ✓ |
| <a id="postparabit"></a>`postparabit` | ✓ | ✓ | ✓ | ✓ |
| <a id="prae"></a>`prae` | ✓ | ✓ | ✓ | ✓ |
| <a id="praefixum"></a>`praefixum` | — | — | — | — |
| <a id="praepara"></a>`praepara` | ✓ | ✓ | ✓ | ✓ |
| <a id="praeparabit"></a>`praeparabit` | ✓ | ✓ | ✓ | ✓ |
| <a id="promissum"></a>`promissum` | ✓ | ✓ | ✓ | ✓ |
| <a id="privata"></a>`privata` | ✓ | ✓ | ✓ | ✓ |
| <a id="proba"></a>`proba` | ✓ | ✓ | ✓ | ✓ |
| <a id="probandum"></a>`probandum` | ✓ | ✓ | ✓ | ✓ |
| <a id="protecta"></a>`protecta` | — | — | — | — |
| <a id="publica"></a>`publica` | ✓ | ✓ | ✓ | ✓ |
| <a id="redde"></a>`redde` | ✓ | ✓ | ✓ | ✓ |
| <a id="reddet"></a>`reddet` | ✓ | ✓ | ✓ | ✓ |
| <a id="repete"></a>`repete` | ✓ | ✓ | ✓ | ✓ |
| <a id="requirit"></a>`requirit` | ✓ | ✓ | ✓ | ✓ |
| <a id="rumpe"></a>`rumpe` | ✓ | ✓ | ✓ | ✓ |
| <a id="scribe"></a>`scribe` | ✓ | ✓ | ✓ | ✓ |
| <a id="scriptum"></a>`scriptum` | ✓ | ✓ | ✓ | ✓ |
| <a id="secus"></a>`secus` | ✓ | ✓ | ✓ | ✓ |
| <a id="si"></a>`si` | ✓ | ✓ | ✓ | ✓ |
| <a id="sic"></a>`sic` | ✓ | ✓ | ✓ | ✓ |
| <a id="sin"></a>`sin` | ✓ | ✓ | ✓ | ✓ |
| <a id="sit"></a>`sit` | ✓ | ✓ | ✓ | ✓ |
| <a id="solum-in"></a>`solum_in` | ✓ | ✓ | ✓ | ✓ |
| <a id="solum"></a>`solum` | ✓ | ✓ | ✓ | ✓ |
| <a id="sparge"></a>`sparge` | ✓ | ✓ | ✓ | ✓ |
| <a id="sponte"></a>`sponte` | ✓ | ✓ | ✓ | ✓ |
| <a id="sub"></a>`sub` | ✓ | ✓ | ✓ | ✓ |
| <a id="tacet"></a>`tacet` | ✓ | ✓ | ✓ | ✓ |
| <a id="tacebit"></a>`tacebit` | ✓ | ✓ | ✓ | ✓ |
| <a id="tabula"></a>`tabula` | ✓ | ✓ | ✓ | ✓ |
| <a id="tag"></a>`tag` | ✓ | ✓ | ✓ | ✓ |
| <a id="temporis"></a>`temporis` | ✓ | ✓ | ✓ | ✓ |
| <a id="tensor"></a>`tensor` | ✓ | ✓ | ✓ | ✓ |
| <a id="textus"></a>`textus` | ✓ | ✓ | ✓ | ✓ |
| <a id="typus"></a>`typus` | ✓ | ✓ | ✓ | ✓ |
| <a id="ubique"></a>`ubique` | ✓ | ✓ | ✓ | ✓ |
| <a id="usque"></a>`usque` | ✓ | ✓ | ✓ | ✓ |
| <a id="ut"></a>`ut` | ✓ | ✓ | ✓ | ✓ |
| <a id="varia"></a>`varia` | ✓ | ✓ | ✓ | ✓ |
| <a id="variandum"></a>`variandum` | ✓ | ✓ | ✓ | ✓ |
| <a id="vector"></a>`vector` | ✓ | ◐ | ✓ | ✓ |
| <a id="vacuum"></a>`vacuum` | ✓ | ✓ | ✓ | ✓ |
| <a id="verum"></a>`verum` | ✓ | ✓ | ✓ | ✓ |
| <a id="vide"></a>`vide` | ✓ | ✓ | ✓ | ✓ |

## ऑपरेटर — एप्लिकेशन लेन

### ऑपरेटर समूह

| term | rust | go | ts | faber |
|---|---|---|---|---|
| <a id=""></a>`⊜` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∧` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`·` | ✓ | ◐ | ✓ | ✓ |
| <a id=""></a>`×` | ✓ | ○ | ✓ | ✓ |
| <a id=""></a>`⊗` | ✓ | ○ | ✓ | ✓ |
| <a id=""></a>`⊙` | ✓ | ◐ | ✓ | ✓ |
| <a id=""></a>`→` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`←` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↤` | ✓ | ✓ | ✓ | ✓ |
| <a id="aut"></a>`aut` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`![` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!.` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≠` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!(` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊻` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↦` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇒` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`‥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`…` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≡` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`=` | ✓ | ✓ | ✓ | ✓ |
| <a id="et"></a>`et` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≤` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↓` | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u16"></a>`modulus<u16>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u32"></a>`modulus<u32>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u64"></a>`modulus<u64>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u8"></a>`modulus<u8>` | ✓ | ✕ | ✓ | ✓ |
| <a id="non-est"></a>`non est` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊚` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∨` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∪` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↑` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?[` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?.` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?(` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`§` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇐` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊘` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊛` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`¬` | ✓ | ✓ | ✓ | ✓ |
| <a id="vel"></a>`vel` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∷` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∴` | ✓ | ✓ | ✓ | ✓ |
| <a id="ergo"></a>`ergo` | ✓ | ✓ | ✓ | ✓ |

## कीवर्ड — सिस्टम लेन

### कीवर्ड

| term | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
| --- | --- | --- | --- | --- | --- | --- |
| <a id="abstractus"></a>`abstractus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ab"></a>`ab` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ad"></a>`ad` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| <a id="adfirma"></a>`adfirma` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ante"></a>`ante` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="atomic"></a>`atomic` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| <a id="argumenta"></a>`argumenta` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="bivalens"></a>`bivalens` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cape"></a>`cape` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="casu"></a>`casu` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cede"></a>`cede` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="ceteri"></a>`ceteri` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ceterum"></a>`ceterum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="clausura"></a>`clausura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cli"></a>`cli` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="copia"></a>`copia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="cura"></a>`cura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="curata"></a>`curata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="cursor"></a>`cursor` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="custodi"></a>`custodi` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="de"></a>`de` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="descriptio"></a>`descriptio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="discerne"></a>`discerne` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="discretio"></a>`discretio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="dum"></a>`dum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ego"></a>`ego` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="elige"></a>`elige` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="errata"></a>`errata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="est"></a>`est` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="ex"></a>`ex` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="exitus"></a>`exitus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fac"></a>`fac` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="falsum"></a>`falsum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fient"></a>`fient` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fiet"></a>`fiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="figendum"></a>`figendum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="finge"></a>`finge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fiunt"></a>`fiunt` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fixum"></a>`fixum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fragilis"></a>`fragilis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="fractus"></a>`fractus` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="functio"></a>`functio` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="futura"></a>`futura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="futurum"></a>`futurum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="generis"></a>`generis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="genus"></a>`genus` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="iace"></a>`iace` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="iacit"></a>`iacit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ignotum"></a>`ignotum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="immutata"></a>`immutata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="implet"></a>`implet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="importa"></a>`importa` | ✓ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id="in"></a>`in` | — | — | — | — | — | — |
| <a id="incipiet"></a>`incipiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="incipit"></a>`incipit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="inter"></a>`inter` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="intra"></a>`intra` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="instans"></a>`instans` | ✓ | ✕ | ✕ | ✕ | ✕ | ◐ |
| <a id="itera"></a>`itera` | ✓ | ◐ | ◐ | ◐ | ◐ | ✓ |
| <a id="lege"></a>`lege` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="lineam"></a>`lineam` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="lista"></a>`lista` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="matrix"></a>`matrix` | ✕ | ✕ | ✕ | ✓ | ✓ | ✕ |
| <a id="mone"></a>`mone` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="mori"></a>`mori` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="nexum"></a>`nexum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="nihil"></a>`nihil` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="numquam"></a>`numquam` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ |
| <a id="numerus"></a>`numerus` | ✓ | ✓ | ✓ | ◐ | ◐ | ◐ |
| <a id="non"></a>`non` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="omitte"></a>`omitte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="omnia"></a>`omnia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="operandus"></a>`operandus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="optio"></a>`optio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="optiones"></a>`optiones` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="ordo"></a>`ordo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="octeti"></a>`octeti` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="implendum"></a>`implendum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="per"></a>`per` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="perge"></a>`perge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="postpara"></a>`postpara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="postparabit"></a>`postparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="prae"></a>`prae` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="praefixum"></a>`praefixum` | — | — | — | — | — | — |
| <a id="praepara"></a>`praepara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="praeparabit"></a>`praeparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="promissum"></a>`promissum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="privata"></a>`privata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="proba"></a>`proba` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="probandum"></a>`probandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="protecta"></a>`protecta` | — | — | — | — | — | — |
| <a id="publica"></a>`publica` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="redde"></a>`redde` | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ |
| <a id="reddet"></a>`reddet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="repete"></a>`repete` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="requirit"></a>`requirit` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id="rumpe"></a>`rumpe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="scribe"></a>`scribe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="scriptum"></a>`scriptum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="secus"></a>`secus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="si"></a>`si` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sic"></a>`sic` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sin"></a>`sin` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sit"></a>`sit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="solum-in"></a>`solum_in` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="solum"></a>`solum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="sparge"></a>`sparge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sponte"></a>`sponte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="sub"></a>`sub` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tacet"></a>`tacet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tacebit"></a>`tacebit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tabula"></a>`tabula` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="tag"></a>`tag` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="temporis"></a>`temporis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="tensor"></a>`tensor` | ✓ | ✓ | ✓ | ◐ | ◐ | ◐ |
| <a id="textus"></a>`textus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="typus"></a>`typus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ubique"></a>`ubique` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="usque"></a>`usque` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ut"></a>`ut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="varia"></a>`varia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="variandum"></a>`variandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vector"></a>`vector` | ✓ | ◐ | ◐ | ◐ | ◐ | ✕ |
| <a id="vacuum"></a>`vacuum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="verum"></a>`verum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vide"></a>`vide` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## ऑपरेटर — सिस्टम लेन

### ऑपरेटर समूह

| term | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
| --- | --- | --- | --- | --- | --- | --- |
| <a id=""></a>`⊜` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∧` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`·` | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id=""></a>`×` | ✓ | ○ | ○ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊗` | ○ | ○ | ○ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊙` | ◐ | ◐ | ◐ | ○ | ○ | ◐ |
| <a id=""></a>`→` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇥` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`←` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↤` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="aut"></a>`aut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`![` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!.` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≠` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!(` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊻` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↦` | ✓ | ◐ | ◐ | ✕ | ✕ | ✓ |
| <a id=""></a>`⇒` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`‥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`…` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≡` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`=` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="et"></a>`et` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≤` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↓` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u16"></a>`modulus<u16>` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="modulus-u32"></a>`modulus<u32>` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="modulus-u64"></a>`modulus<u64>` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="modulus-u8"></a>`modulus<u8>` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="non-est"></a>`non est` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊚` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∨` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∪` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↑` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?[` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?.` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?(` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`§` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇐` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊘` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊛` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`¬` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vel"></a>`vel` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∷` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id=""></a>`∴` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ergo"></a>`ergo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## अन्य terms (`existing-home` / निर्दिष्ट नहीं)

### existing-home

| term | rust | go | ts | faber |
|---|---|---|---|---|
| <a id="alias"></a>`alias` | ✓ | ✓ | ✓ | ✓ |
| <a id="arena"></a>`arena` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`@` | ✓ | ✓ | ✓ | ✓ |
| <a id="f16"></a>`f16` | ✕ | ✓ | ✓ | ✓ |
| <a id="imperia"></a>`imperia` | ✓ | ✓ | ✓ | ✓ |
| <a id="imperium"></a>`imperium` | ✓ | ✓ | ✓ | ✓ |
| <a id="manifest"></a>`manifest` | ✓ | ✓ | ✓ | ✓ |
| <a id="metior"></a>`metior` | ✓ | ✓ | ✓ | ✓ |
| <a id="nondum"></a>`nondum` | ✓ | ✓ | ✓ | ✓ |
| <a id="objectum"></a>`objectum` | ✓ | ✓ | ✓ | ✓ |
| <a id="prima"></a>`prima` | ✓ | ✓ | ✓ | ✓ |
| <a id="string"></a>`string` | ✓ | ✓ | ✓ | ✓ |
| <a id="block-string"></a>`block-string` | ✓ | ✓ | ✓ | ✓ |
| <a id="summa"></a>`summa` | ✓ | ✓ | ✓ | ✓ |
| <a id="targets"></a>`targets` | ✓ | ✓ | ✓ | ✓ |
| <a id="ultima"></a>`ultima` | ✓ | ✓ | ✓ | ✓ |
| <a id="versio"></a>`versio` | ✓ | ✓ | ✓ | ✓ |
