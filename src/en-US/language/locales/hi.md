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

Generated from the packs; read a row across to translate one term. The Latin column is the canonical name, which keys the [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          Latin        हिन्दी
| ---------------  -----------  --------------
| all              omnia        सभी
| and              et           और
| any              quilibet     कोई
| argmax           argmaxima    argmax
| argmin           argminima    argmin
| args             argumenta    तर्क
| as               ut           रूपमें
| asc              ascendens    आरोही
| assert           adfirma      पुष्टि
| async            fiet         async
| async_generator  fient        async_जनक
| async_main       incipiet     आरंभasync
| async_setup      praeparabit  पूर्वतैयारasync
| async_teardown   postparabit  पश्चतैयारasync
| at               apud         पर
| await            tacebit      रुको
| await_const      figendum     रुको_स्थिर
| await_var        variandum    रुको_चर
| axis             axis         अक्ष
| before           ante         पहले
| bench            metior       मापो
| between          inter        बीच
| break            rumpe        तोड़ो
| call             ad           सेवा
| case             casu         स्थिति
| catch            cape         पकड़ो
| class            genus        वर्ग
| cli              cli          cli
| coalesce         vel          डिफ़ॉल्ट
| column           columna      कॉलम
| command          imperium     आदेश
| comptime         praefixum    उपसर्ग
| const            fixum        स्थिर
| continue         perge        जारी
| conversion       conversio    रूपांतरण
| —                conversion   बदलें
| copy             exemplum     प्रतिलिपि
| count            numeratio    गिनती
| cursor           cursor       संकेतक
| debug            vide         देखो
| default          ceterum      अन्यतम
| desc             descendens   अवरोही
| describe         probandum    परीक्षणसमूह
| description      descriptio   विवरण
| do               fac          करो
| elif             sin          अन्यथायदि
| else             secus        अन्यथा
| embed            insere       अंतःस्थापित
| empty            vacua        खाली
| enum             ordo         क्रम
| errors           errata       त्रुटि
| exit             exitus       निर्गम
| expect_failure   erratur      अपेक्षित_विफलता
| false            falsum       असत्य
| flaky            fragilis     नाज़ुक
| fn               functio      फलन
| for              itera        दोहराओ
| format           scriptum     लिखित
| fragment         fragment     खंड
| from             ex           सेवन
| future           futura       भविष्य
| generator        fiunt        जनक
| global           ubique       वैश्विक
| guard            custodi      रक्षक
| if               si           यदि
| implements       implet       लागूकरता
| import           importa      आयात
| interface        implendum    अनुबन्ध
| internal         interna      आंतरिक
| is               est          है
| kernel           nucleum      कर्नेल
| lambda           clausura     समापन
| lane             lane         लेन
| let              sit          बैठा
| line             lineam       पंक्ति
| long             longum       विस्तृत
| main             incipit      आरंभ
| match            discerne     मिलाओ
| max              maxima       अधिकतम
| min              minima       न्यूनतम
| module           regio        क्षेत्र
| mut              in           में
| name             nomen        नाम
| nan              nonnumerus   nan
| not              non          नहीं
| null             nulla        शून्यवत्
| only             solum        केवल
| only_in          solum_in     केवलमें
| operand          operandus    ऑपरेंड
| option           optio        विकल्प
| optional         sponte       स्वेच्छा
| options          optiones     चयन
| or               aut          या
| own              penes        स्वामित्व
| panic            mori         मरोजाओ
| pass             tacet        मौन
| per              pro          अनुसार
| primus_quem      primus_quem  primus_quem
| print            nota         दिखाओ
| private          privata      निजी
| product          factum       गुणनफल
| protected        protecta     संरक्षित
| public           publica      सार्वजनिक
| radix            radix        radix
| range            ab           सीमा
| read             lege         पढ़ो
| readonly         immutata     अपरिवर्तित
| reduce           reducta      समेटो
| ref              de           से
| reject           reice        अस्वीकार
| rename           verte        नाम_बदलें
| repeat           repete       पुनरावृत्ति
| require          requirit     आवश्यक
| rest             ceteri       बाकी
| return           redde        लौटाओ
| return_await     reddet       रुको_लौटाओ
| schema           schema       स्कीमा
| self             ego          मैं
| setup            praepara     पूर्वतैयार
| shared           commune      साझा
| short            brevis       संक्षिप्त
| size             magnitudo    आकार
| skip             omitte       छोड़ो
| sort             ordinata     क्रमबद्ध_करो
| spread           sparge       फैलाओ
| static           generis      स्थैतिक
| step             per          प्रति
| sum              summa        योग
| switch           elige        चुनो
| tag              tag          टैग
| teardown         postpara     पश्चतैयार
| test             proba        परीक्षण
| then             ergo         अतः
| thread           filum        धागा
| throw            iace         इधरफेंको
| throws           iacit        फेंकता
| timeout          temporis     समय
| todo             futurum      लंबित
| trap             capta        जाल
| true             verum        सत्य
| tuple            iuncta       टपल
| type             typus        प्रकार
| ubi              ubi          ubi
| union            discretio    विभेद
| unstable         nondum       अस्थिर
| until            usque        तक
| var              varia        चर
| variant          finge        गढ़ो
| vertex           vertex       शीर्ष
| via              via          द्वारा
| warn             mone         चेताओ
| while            dum          जबतक
| within           intra        भीतर
| wrapping         modulus      मॉड्यूल
| write            scribe       लिखो
| yield            cede         आगेबढ़ो
```

### Types {#types}

```text locale=la
| English      Latin        हिन्दी
| -----------  -----------  --------------
| any          quidlibet    कुछभी
| ascii        ascii        ascii
| atomic       atomic       परमाणु
| bool         bivalens     तार्किक
| byte         octetus      बाइट_मान
| bytes        octeti       बाइट
| census       census       गणना
| channel      sermo        चैनल
| char         littera      अक्षर
| clamp        clampa       किनारा_स्थिर
| filter       filtrum      फ़िल्टर
| float        fractus      भिन्न
| frame        scrinium     फ़्रेम
| instant      instans      क्षण
| int          numerus      संख्या
| intervallum  intervallum  अंतराल
| iterator     cursor_t     कर्सर
| json         json         json
| ledger       tabulae      बही
| list         lista        सूची
| map          tabula       तालिका
| matrix       matrix       आव्यूह
| never        numquam      कभीनहीं
| none         nihil        शून्य_मान
| object       objectum     वस्तु
| promise      promissum    वादा
| queue        queue        कतार
| record       ratio        ratio
| recv         tuus         पाना
| reflect      reflexa      किनारा_परावर्तन
| regex        regex        regex
| saturating   saturatus    संतृप्त
| send         meus         भेजना
| series       series       शृंखला
| set          copia        समुच्चय
| sparsa       sparsa       विरल
| stack        stack        स्टैक
| string       textus       पाठ
| tensor       tensor       टेंसर
| trapping     exactus      सटीक
| unknown      ignotum      अज्ञात
| value        valor        मान
| vector       vector       सदिश
| void         vacuum       रिक्त
| wrap         involuta     किनारा_लपेट
| wrapping_ty  modulus_t    मॉड्यूल_टाइप
```

### Intrinsics {#intrinsics}

```text locale=la
| English               Latin                  हिन्दी
| --------------------  ---------------------  -----------------
| abs                   absolutum              निरपेक्ष
| add                   adde                   जोड़ो
| added                 addita                 जोड़ा
| added_bias            addita_bias            बायस_जोड़ा
| all                   omnia                  सभी
| any                   quilibet               कोई
| append                appende                पीछे_जोड़ो
| apply                 applica                लगाओ
| approx                approximata            सन्निकट
| argmax                argmaxima              argmax
| argmin                argminima              argmin
| at                    apud                   पर
| at_least              maxime                 कम_से_कम
| at_most               minime                 अधिक_से_अधिक
| bit_and               coniuncta              बिट_और
| bit_and_assign        coniunge               बिट_और_सौंपो
| bit_or                disiuncta              बिट_या
| bit_or_assign         disiunge               बिट_या_सौंपो
| ceiling               tectum                 ऊपर_पूर्णांक
| clamp                 coercere               सीमित_करो
| compare_exchange      compare_exchange       तुलना_और_बदलो
| complement            complementa            पूरक_करो
| complemented          complementata          पूरक
| contains              continet               शामिल
| cos                   cosinus                कोज्या
| count_nonzero         nonnihil               अशून्य_गणना
| create                crea                   बनाओ
| cross                 transversum            सदिश_गुणनफल
| cross_entropy         crux_entropia          क्रॉस_एंट्रॉपी
| cumulate              cumulata               संचयी
| cursor                cursor                 कर्सर
| delete                dele                   मिटाओ
| densify               densata                घना_करो
| difference            differentia            अंतर
| difference_symmetric  symmetrica             सममित_अंतर
| divide                divida                 भाग_दो
| divide                divisio                विभाजन
| divided               divisa                 विभाजित
| dot                   productum              बिंदु_गुणनफल
| drop                  omissa                 आरंभ_छोड़ो
| end                   terminus               अंत
| ends_with             finis                  पर_समाप्त
| escape                munita                 एस्केप
| exchange              exchange               अदलाबदली
| exp                   exponentia             चरघातांकी
| expanded              expande                फैलाओ
| fill                  reple                  भरो
| filter                filtrata               छानो
| find                  inventa                खोज
| find_all              collecta               सभी_खोज
| first                 primus                 पहला
| flatten               planata                समतल_करो
| flip                  alterna                पलटो
| flipped               alternata              पलटा
| floor                 pavimentum             नीचे_पूर्णांक
| formata               formata                formata
| gather                gather                 एकत्र_करो
| gelu                  gelu                   gelu
| get                   accipe                 पाओ
| greater               maior                  बड़ा
| group                 coetus                 समूह
| has                   habet                  उपस्थित
| intersect             inter                  प्रतिच्छेद
| intersection          intersectio            प्रतिच्छेदन
| invert                inversa                व्युत्क्रम
| is_empty              vacua                  रिक्त
| is_subset             subcopia               उपसमुच्चय_है
| is_superset           supercopia             अधिसमुच्चय_है
| keys                  claves                 कुंजियाँ
| last                  ultimus                अंतिम
| length                longitudo              लंबाई
| less                  minor                  छोटा
| limes                 limes                  किनारा
| ln                    logarithmus            प्राकृतिक_लघुगणक
| load                  load                   लोड
| log10                 logarithmus_decimalis  दशमलव_लघुगणक
| lowercase             minuscula              छोटे_अक्षर
| map                   mappata                रूपांतरित
| matches               consentit              मेल_खाता_है
| materialize           materialize            मूर्त_करो
| matmul                matmul                 आव्यूह_गुणन
| maximum               maximus                अधिकतम
| mean                  media                  माध्य
| minimum               minimus                न्यूनतम
| modulo                modulata               शेषफल
| modulo_assign         modula                 शेषफल_सौंपो
| multiplied            multiplicata           गुणित
| multiply              multiplica             गुणा_करो
| named                 nominatus              नामित
| negate                nega                   चिह्न_पलटो
| negated               negativa               चिह्न_पलटा
| norm_layer            laminatio              परत_सामान्यीकरण
| norm_rms              rms_norm               rms_norm
| norm_rope             rope_norm              rope_norm
| normalize             normalizata            सामान्यीकृत
| power                 potentia               घात
| put                   pone                   रखो
| reduce                reducta                समेटो
| relu                  activatio_relu         रेलू_सक्रियण
| remove_first          decapita               पहला_हटाओ
| remove_last           detrahe                अंतिम_हटाओ
| replace               muta                   बदलो
| reshape               forma                  आकार_बदलो
| reverse               inverte                उलटो
| rope_half             rope_half              rope_half
| round                 rotunda                निकटतम_पूर्णांक
| set                   ponde                  निर्धारित_करो
| shape                 magnitudines           आकृति
| shift                 disloco                खिसकाओ
| shift_left            sinistra               बाएँ_सरकाओ
| shift_right           dextra                 दाएँ_सरकाओ
| shifted_left          sinistrata             बाएँ_सरकाया
| shifted_right         dextrata               दाएँ_सरकाया
| sign                  signum                 चिह्न
| silu                  silu                   silu
| sin                   sinus                  ज्या
| slice                 sectio                 टुकड़ा
| softmax               activatio_softmax      सॉफ्टमैक्स
| softmax_causal        softmax_causal         सॉफ्टमैक्स_कारणात्मक
| sort                  ordina                 क्रमबद्ध_करो
| sorted                ordinata               क्रमबद्ध
| split                 divide                 बाँटो
| sqrt                  radix                  वर्गमूल
| start                 principium             आरंभ
| starts_with           initium                से_आरंभ
| store                 store                  संचय
| subtract              subtrahe               घटाओ
| subtracted            subtracta              घटाया
| sum                   summa                  योग
| swizzle               swizzle                swizzle
| take                  prima                  पहले_लो
| take_last             ultima                 अंतिम_लो
| tan                   tangens                स्पर्शज्या
| text                  inventum               पाठ
| transpose             transpone              परिवर्त
| trim                  recide                 छाँटो
| truncate              trunca                 काटो
| union                 unio                   सम्मिलन
| union                 union                  सम्मिलन
| uppercase             maiuscula              बड़े_अक्षर
| values                valores                मान
```

---

[All reader locales](/language/reader-locales.html) · [Keyword reference](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
