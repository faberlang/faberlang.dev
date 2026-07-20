+++
translation_kind = "translated"

title = "Syntax and semantics"
section = "syntax"
order = 0
sources = []


prose_hash = "sha256:756b1478369ce29cb747d6574830f684a1af6a995f5139ac5d8f0d00f1fecd08"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber सिंटैक्स तीन सिद्धांतों पर आधारित है: नामों से पहले प्रकार, व्यवहार के लिए लैटिन शब्द, और मान-प्रवाह के लिए संरचनात्मक ग्लिफ़। हर घोषणा पहले आशय और उसके बाद कार्य-विधि को व्यक्त करती है।

## डेटा प्रकार {#types}

प्रकार-प्रथम घोषणाएँ, संख्यात्मक चौड़ाइयाँ, टेन्सर, सूचियाँ और GPU के मूल प्रकार। [और पढ़ें →](/syntax/types.html)

## चर {#variables}

बाइंडिंग मान-प्रवाह के लिए `←` का उपयोग करती हैं। परिवर्तनशीलता `varia` के माध्यम से स्पष्ट रूप से व्यक्त की जाती है। [और पढ़ें →](/syntax/variables.html)

## फ़ंक्शन {#functions}

फ़ंक्शन नामों से पहले पैरामीटर प्रकार घोषित करते हैं। रिटर्न प्रकार ऐरो के बाद आते हैं। [और पढ़ें →](/syntax/functions.html)

## नियंत्रण प्रवाह {#control-flow}

शाखाकरण के लिए `si`/`ceterum`, पुनरावृत्ति के लिए `dum`, और लूप नियंत्रण के लिए `perge`/`rumpe`। [और पढ़ें →](/syntax/control-flow.html)

## त्रुटियाँ {#errors}

त्रुटियाँ अपवाद नहीं, बल्कि प्रकारित मान हैं। `aut` प्रकार सफलता या विफलता को वहन करता है। [और पढ़ें →](/syntax/errors.html)

## जेनेरिक {#generics}

फ़ंक्शन और संरचनाओं पर प्रकार पैरामीटर। ट्रेट बाउंड के माध्यम से प्रतिबंध। [और पढ़ें →](/syntax/generics.html)

## संग्रह {#collections}

संरचित डेटा के लिए सूचियाँ (`lista`), मैप और टेन्सर। [और पढ़ें →](/syntax/collections.html)

## स्ट्रिंग {#strings}

`textus` प्रकार, टेम्पलेट लिटरल और स्ट्रिंग ऑपरेशन। [और पढ़ें →](/syntax/strings.html)

## रूपांतरण {#conversion}

स्पष्ट प्रकार रूपांतरणों के लिए `conversio` प्रणाली। [और पढ़ें →](/syntax/conversion.html)

## ग्लिफ़ {#glyphs}

संरचनात्मक ग्लिफ़ संदर्भ: `←`, `→`, `‥`, `≡`, `≢` और अन्य। [और पढ़ें →](/syntax/glyphs.html)

## नल-योग्यता {#nullability}

अनुपस्थिति भी प्रकारित होती है। `forsitan` प्रकार और नल-योग्य एनोटेशन। [और पढ़ें →](/syntax/nullability.html)
