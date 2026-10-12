Faber में फ़ंक्शन `functio` का उपयोग करके घोषित किए जाते हैं। पैरामीटर के लिए type-first सिंटैक्स और return type के लिए glyph का उपयोग किया जाता है।

## मूल सिंटैक्स {#basic-syntax}

<<<FENCE 0>>>

त्रुटि चैनल के साथ:

<<<FENCE 1>>>

## उदाहरण {#examples}

<<<FENCE 2>>>

## Return मान {#return-values}

सामान्य return के लिए `redde` का उपयोग करें:

<<<FENCE 3>>>

`vacuum` return type के लिए खाली `redde`:

<<<FENCE 4>>>

## Borrowing और mutability (`de`, `in`, `ex`) {#borrowing-and-mutability}

Faber पैरामीटर पर छोटे पूर्वसर्गों के माध्यम से बताता है कि कोई मान किस प्रकार पास किया जाता है:

| Marker | उद्देश्य | सामान्य Rust lowering |
|--------|---------|----------------------|
| *(none)* | स्वामित्व वाला मान | `T` by value |
| `de` | साझा borrow (केवल पढ़ने योग्य) | `&T` |
| `in` | mutable borrow | `&mut T` |
| `ex` | consume करना (callee में move करना) | `T` by move |

<<<FENCE 5>>>

यही शब्द (`de`, `ex`) अन्य constructs में भी दोबारा उपयोग किए जाते हैं — हर `ex` को “consume” न समझें:

| Surface | भूमिका |
|---------|--------|
| पैरामीटर पर `de textus name` | साझा borrow |
| पैरामीटर पर `in numerus count` | mutable borrow |
| पैरामीटर पर `ex textus buffer` | callee में move करना |
| `itera ex items fixum item` | मानों पर iterate करना |
| `itera de tabula fixum key` | keys पर iterate करना |
| `ex source fixum x, ceteri rest` | fields को destructure करना |
| `importa ex "path"` | module से import करना |

## Entry point {#entry-point}

प्रोग्राम का entry point `incipit` होता है:

<<<FENCE 6>>>

## CLI entry point {#cli-entry-point}

CLI प्रोग्रामों के लिए `incipit argumenta` parsed command arguments प्राप्त करता है:

<<<FENCE 7>>>

## Passing mode — `sponte` {#passing-mode-sponte}

`sponte` ऐसे पैरामीटर को चिह्नित करता है जिसे caller छोड़ सकता है:

<<<FENCE 8>>>
