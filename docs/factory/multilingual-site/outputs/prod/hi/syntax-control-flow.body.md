## सशर्त शाखाकरण {#conditional-branching}

### si / sin / secus {#si-sin-secus}

<<<FENCE 0>>>

`else-if` और `else` के साथ:

<<<FENCE 1>>>

### ∴ के साथ संक्षिप्त शाखा {#compact-branch-with}

एकल-कथन वाली शाखा का बॉडी `∴` (या इसके उपनाम `ergo`) का उपयोग करता है:

<<<FENCE 2>>>

## पुनरावृत्ति {#iteration}

### मान — itera ex {#values-itera-ex}

<<<FENCE 3>>>

### कुंजियाँ — itera de {#keys-itera-de}

<<<FENCE 4>>>

### परास — itera ab {#range-itera-ab}

<<<FENCE 5>>>

## While लूप {#while-loops}

<<<FENCE 6>>>

## Guard अनुभाग — custodi {#guard-sections-custodi}

`custodi` किसी फ़ंक्शन के मुख्य बॉडी से पहले शीघ्र-बाहर निकलने वाली जाँचों को समूहित करता है।  
प्रत्येक `si` क्लॉज़ एक क्रमिक guard है:

<<<FENCE 7>>>

v1 में `custodi` से बाहर निकलना संभव नहीं है — यह लूप नहीं, बल्कि एक guard rail है।

## पैटर्न मिलान — elige {#pattern-matching-elige}

`elige` पहली मेल खाने वाली शाखा चुनता है:

<<<FENCE 8>>>

## टैग किए गए यूनियन का मिलान — discerne {#tagged-union-matching-discerne}

`discerne` `discretio` के सभी वैरिएंट का पूर्ण मिलान करता है:

<<<FENCE 9>>>

## Try ब्लॉक — fac / cape {#try-blocks-fac-cape}

`fac` ऐसा ब्लॉक खोलता है जिसमें त्रुटि उत्पन्न हो सकती है, और `cape` उसे संभालता है:

<<<FENCE 10>>>
