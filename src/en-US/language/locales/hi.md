+++
title = "Hindi reader locale"
section = "locales"
order = 13
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

**हिन्दी** — the `hi` reader pack. Script: Devanagari; direction: left-to-right.

| Field | Value |
|---|---|
| **Locale code** | `hi` |
| **Native name** | हिन्दी |
| **Script** | Devanagari |
| **Direction** | left-to-right |

Matra and virama consonant clusters, where one grapheme spans several code points. Indic numeral glyphs (०–९) are rejected inside numeric literals; digits stay ASCII.

## English ↔ Hindi {#mapping}

Generated from the packs; the canonical (Latin) name keys the full [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          हिन्दी
| ---------------  --------------
| all              सभी
| and              और
| any              कोई
| argmax           argmax
| argmin           argmin
| args             तर्क
| as               रूपमें
| assert           पुष्टि
| async            async
| async_generator  async_जनक
| async_main       आरंभasync
| async_setup      पूर्वतैयारasync
| async_teardown   पश्चतैयारasync
| at               पर
| await            रुको
| await_const      रुको_स्थिर
| await_var        रुको_चर
| before           पहले
| bench            मापो
| between          बीच
| break            तोड़ो
| call             सेवा
| case             स्थिति
| catch            पकड़ो
| class            वर्ग
| cli              cli
| coalesce         डिफ़ॉल्ट
| column           कॉलम
| command          आदेश
| comptime         उपसर्ग
| const            स्थिर
| continue         जारी
| conversion       रूपांतरण
| —                बदलें
| copy             प्रतिलिपि
| count            गिनती
| cursor           संकेतक
| debug            देखो
| default          अन्यतम
| describe         परीक्षणसमूह
| description      विवरण
| do               करो
| elif             अन्यथायदि
| else             अन्यथा
| embed            अंतःस्थापित
| empty            खाली
| enum             क्रम
| errors           त्रुटि
| exit             निर्गम
| expect_failure   अपेक्षित_विफलता
| false            असत्य
| flaky            नाज़ुक
| fn               फलन
| for              दोहराओ
| format           लिखित
| fragment         खंड
| free             मुक्त
| from             सेवन
| future           भविष्य
| generator        जनक
| global           वैश्विक
| guard            रक्षक
| if               यदि
| implements       लागूकरता
| import           आयात
| interface        अनुबन्ध
| internal         आंतरिक
| is               है
| kernel           कर्नेल
| lambda           समापन
| lane             लेन
| let              बैठा
| line             पंक्ति
| long             विस्तृत
| main             आरंभ
| match            मिलाओ
| max              अधिकतम
| min              न्यूनतम
| module           क्षेत्र
| mut              में
| name             नाम
| nan              nan
| nihil            शून्य
| not              नहीं
| null             शून्यवत्
| only             केवल
| only_in          केवलमें
| operand          ऑपरेंड
| option           विकल्प
| optional         स्वेच्छा
| options          चयन
| or               या
| own              स्वामित्व
| panic            मरोजाओ
| pass             मौन
| per              अनुसार
| primus_quem      primus_quem
| print            दिखाओ
| private          निजी
| product          गुणनफल
| protected        संरक्षित
| public           सार्वजनिक
| radix            radix
| range            सीमा
| read             पढ़ो
| readonly         अपरिवर्तित
| reduce           समेटो
| ref              से
| reject           अस्वीकार
| rename           नाम_बदलें
| repeat           पुनरावृत्ति
| require          आवश्यक
| rest             बाकी
| return           लौटाओ
| return_await     रुको_लौटाओ
| schema           स्कीमा
| self             मैं
| setup            पूर्वतैयार
| shared           commune
| short            संक्षिप्त
| size             आकार
| skip             छोड़ो
| spread           फैलाओ
| static           स्थैतिक
| step             प्रति
| sum              योग
| switch           चुनो
| tag              टैग
| teardown         पश्चतैयार
| test             परीक्षण
| then             अतः
| thread           धागा
| throw            इधरफेंको
| throws           फेंकता
| timeout          समय
| todo             लंबित
| trap             जाल
| true             सत्य
| tuple            टपल
| type             प्रकार
| ubi              ubi
| union            विभेद
| unstable         अस्थिर
| until            तक
| var              चर
| variant          गढ़ो
| vertex           शीर्ष
| via              द्वारा
| warn             चेताओ
| while            जबतक
| within           भीतर
| wrapping         मॉड्यूल
| write            लिखो
| yield            आगेबढ़ो
```

### Types {#types}

```text locale=la
| English      हिन्दी
| -----------  -----------
| any          कुछभी
| ascii        ascii
| atomic       परमाणु
| bool         तार्किक
| byte         बाइट_मान
| bytes        बाइट
| census       गणना
| channel      चैनल
| char         अक्षर
| filter       फ़िल्टर
| float        भिन्न
| frame        फ़्रेम
| instant      क्षण
| int          संख्या
| intervallum  अंतराल
| iterator     कर्सर
| json         json
| list         सूची
| map          तालिका
| matrix       आव्यूह
| never        कभीनहीं
| none         शून्य_मान
| object       वस्तु
| promise      वादा
| queue        कतार
| record       ratio
| recv         पाना
| regex        regex
| saturating   संतृप्त
| send         भेजना
| series       शृंखला
| set          समुच्चय
| sparsa       विरल
| stack        स्टैक
| string       पाठ
| tensor       टेंसर
| trapping     सटीक
| unknown      अज्ञात
| value        मान
| vector       सदिश
| void         रिक्त
| wrapping_ty  मॉड्यूल_टाइप
```

### Intrinsics {#intrinsics}

```text locale=la
| English               हिन्दी
| --------------------  ---------------
| abs                   निरपेक्ष
| add                   जोड़ो
| added                 जोड़ा
| added_bias            बायस_जोड़ा
| all                   सभी
| any                   कोई
| append                पीछे_जोड़ो
| apply                 लगाओ
| approx                सन्निकट
| argmax                argmax
| argmin                argmin
| at_least              कम_से_कम
| at_most               अधिक_से_अधिक
| bit_and               बिट_और
| bit_and_assign        बिट_और_सौंपो
| bit_or                बिट_या
| bit_or_assign         बिट_या_सौंपो
| ceiling               ऊपर_पूर्णांक
| clamp                 सीमित_करो
| compare_exchange      तुलना_और_बदलो
| complement            पूरक_करो
| complemented          पूरक
| contains              शामिल
| cos                   कोज्या
| create                बनाओ
| cross                 सदिश_गुणनफल
| cross_entropy         क्रॉस_एंट्रॉपी
| cumulate              संचयी
| cursor                कर्सर
| delete                मिटाओ
| densify               घना_करो
| difference            अंतर
| divide                भाग_दो
| divide                विभाजन
| divided               विभाजित
| dot                   बिंदु_गुणनफल
| drop                  आरंभ_छोड़ो
| end                   अंत
| ends_with             पर_समाप्त
| escape                एस्केप
| exchange              अदलाबदली
| exp                   चरघातांकी
| fill                  भरो
| filter                छानो
| find                  खोज
| find_all              सभी_खोज
| first                 पहला
| flatten               समतल_करो
| flip                  पलटो
| flipped               पलटा
| floor                 नीचे_पूर्णांक
| formata               formata
| from_flat             समतल_से_बनाओ
| gather                एकत्र_करो
| gelu                  gelu
| get                   पाओ
| greater               बड़ा
| group                 समूह
| has                   उपस्थित
| intersect             प्रतिच्छेद
| intersection          प्रतिच्छेदन
| invert                व्युत्क्रम
| is_empty              रिक्त
| is_subset             उपसमुच्चय_है
| is_superset           अधिसमुच्चय_है
| keys                  कुंजियाँ
| last                  अंतिम
| layer_norm            परत_सामान्यीकरण
| length                लंबाई
| less                  छोटा
| ln                    प्राकृतिक_लघुगणक
| load                  लोड
| log10                 दशमलव_लघुगणक
| lowercase             छोटे_अक्षर
| map                   रूपांतरित
| matches               मेल_खाता_है
| materialize           मूर्त_करो
| matmul                आव्यूह_गुणन
| maximum               अधिकतम
| mean                  माध्य
| minimum               न्यूनतम
| modulo                शेषफल
| modulo_assign         शेषफल_सौंपो
| multiplied            गुणित
| multiply              गुणा_करो
| named                 नामित
| negate                चिह्न_पलटो
| negated               चिह्न_पलटा
| nonzero_count         अशून्य_गणना
| normalize             सामान्यीकृत
| power                 घात
| put                   रखो
| reduce                समेटो
| relu                  रेलू_सक्रियण
| remove_first          पहला_हटाओ
| remove_last           अंतिम_हटाओ
| replace               बदलो
| reshape               आकार_बदलो
| reverse               उलटो
| rms_norm              rms_norm
| rope_norm             rope_norm
| round                 निकटतम_पूर्णांक
| set                   निर्धारित_करो
| shape                 आकृति
| shift_left            बाएँ_सरकाओ
| shift_right           दाएँ_सरकाओ
| shifted_left          बाएँ_सरकाया
| shifted_right         दाएँ_सरकाया
| sign                  चिह्न
| silu                  silu
| sin                   ज्या
| slice                 टुकड़ा
| softmax               सॉफ्टमैक्स
| sort                  क्रमबद्ध_करो
| sorted                क्रमबद्ध
| split                 बाँटो
| sqrt                  वर्गमूल
| start                 आरंभ
| starts_with           से_आरंभ
| store                 संचय
| subtract              घटाओ
| subtracted            घटाया
| sum                   योग
| swizzle               swizzle
| symmetric_difference  सममित_अंतर
| take                  पहले_लो
| take_last             अंतिम_लो
| tan                   स्पर्शज्या
| text                  पाठ
| transpose             परिवर्त
| trim                  छाँटो
| truncate              काटो
| union                 सम्मिलन
| union                 सम्मिलन
| uppercase             बड़े_अक्षर
| values                मान
```

---

[All reader locales](/language/reader-locales.html) · [Full keyword mapping](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
