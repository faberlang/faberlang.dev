+++
title = "Latin reader locale"
section = "locales"
order = 11
sources = [
  "radix/locale/<locale>/pack.toml",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

**Latina** — the `la` reader pack. Script: Latin; direction: left-to-right.

| Field | Value |
|---|---|
| **Locale code** | `la` |
| **Native name** | Latina |
| **Script** | Latin |
| **Direction** | left-to-right |

The canonical pack. Every other pack is a translation of this one, and the pack key — the canonical name — *is* the Latin spelling.

## English ↔ Latin {#mapping}

Generated from the packs; the canonical (Latin) name keys the full [keyword reference](/language/locales/keywords.html).

### Keywords {#keywords}

```text locale=la
| English          Latina
| ---------------  -----------
| all              omnia
| and              et
| any              quilibet
| argmax           argmaxima
| argmin           argminima
| args             argumenta
| as               ut
| assert           adfirma
| async            fiet
| async_generator  fient
| async_main       incipiet
| async_setup      praeparabit
| async_teardown   postparabit
| at               apud
| await            tacebit
| await_const      figendum
| await_var        variandum
| before           ante
| bench            metior
| between          inter
| break            rumpe
| call             ad
| case             casu
| catch            cape
| class            genus
| cli              cli
| coalesce         vel
| column           columna
| command          imperium
| comptime         praefixum
| const            fixum
| continue         perge
| conversion       conversio
| —                conversion
| copy             exemplum
| count            numeratio
| cursor           cursor
| debug            vide
| default          ceterum
| describe         probandum
| description      descriptio
| do               fac
| elif             sin
| else             secus
| embed            insere
| empty            vacua
| enum             ordo
| errors           errata
| exit             exitus
| expect_failure   erratur
| false            falsum
| flaky            fragilis
| fn               functio
| for              itera
| format           scriptum
| fragment         fragment
| free             libera
| from             ex
| future           futura
| generator        fiunt
| global           ubique
| guard            custodi
| if               si
| implements       implet
| import           importa
| interface        implendum
| internal         interna
| is               est
| kernel           nucleum
| lambda           clausura
| lane             lane
| let              sit
| line             lineam
| long             longum
| main             incipit
| match            discerne
| max              maxima
| min              minima
| module           regio
| mut              in
| name             nomen
| nan              nonnumerus
| nihil            nihil
| not              non
| null             nulla
| only             solum
| only_in          solum_in
| operand          operandus
| option           optio
| optional         sponte
| options          optiones
| or               aut
| own              penes
| panic            mori
| pass             tacet
| per              pro
| primus_quem      primus_quem
| print            nota
| private          privata
| product          factum
| protected        protecta
| public           publica
| radix            radix
| range            ab
| read             lege
| readonly         immutata
| reduce           reducta
| ref              de
| reject           reice
| rename           verte
| repeat           repete
| require          requirit
| rest             ceteri
| return           redde
| return_await     reddet
| schema           schema
| self             ego
| setup            praepara
| shared           commune
| short            brevis
| size             magnitudo
| skip             omitte
| spread           sparge
| static           generis
| step             per
| sum              summa
| switch           elige
| tag              tag
| teardown         postpara
| test             proba
| then             ergo
| thread           filum
| throw            iace
| throws           iacit
| timeout          temporis
| todo             futurum
| trap             capta
| true             verum
| tuple            iuncta
| type             typus
| ubi              ubi
| union            discretio
| unstable         nondum
| until            usque
| var              varia
| variant          finge
| vertex           vertex
| via              via
| warn             mone
| while            dum
| within           intra
| wrapping         modulus
| write            scribe
| yield            cede
```

### Types {#types}

```text locale=la
| English      Latina
| -----------  -----------
| any          quidlibet
| ascii        ascii
| atomic       atomic
| bool         bivalens
| byte         octetus
| bytes        octeti
| census       census
| channel      sermo
| char         littera
| filter       filtrum
| float        fractus
| frame        scrinium
| instant      instans
| int          numerus
| intervallum  intervallum
| iterator     cursor_t
| json         json
| list         lista
| map          tabula
| matrix       matrix
| never        numquam
| none         nihil
| object       objectum
| promise      promissum
| queue        queue
| record       ratio
| recv         tuus
| regex        regex
| saturating   saturatus
| send         meus
| series       series
| set          copia
| sparsa       sparsa
| stack        stack
| string       textus
| tensor       tensor
| trapping     exactus
| unknown      ignotum
| value        valor
| vector       vector
| void         vacuum
| wrapping_ty  modulus_t
```

### Intrinsics {#intrinsics}

```text locale=la
| English               Latina
| --------------------  ---------------------
| abs                   absolutum
| add                   adde
| added                 addita
| added_bias            addita_bias
| all                   omnia
| any                   quilibet
| append                appende
| apply                 applica
| approx                approximata
| argmax                argmaxima
| argmin                argminima
| at_least              maxime
| at_most               minime
| bit_and               coniuncta
| bit_and_assign        coniunge
| bit_or                disiuncta
| bit_or_assign         disiunge
| ceiling               tectum
| clamp                 coercere
| compare_exchange      compare_exchange
| complement            complementa
| complemented          complementata
| contains              continet
| cos                   cosinus
| create                crea
| cross                 transversum
| cross_entropy         crux_entropia
| cumulate              cumulata
| cursor                cursor
| delete                dele
| densify               densata
| difference            differentia
| divide                divida
| divide                divisio
| divided               divisa
| dot                   productum
| drop                  omissa
| end                   terminus
| ends_with             finis
| escape                munita
| exchange              exchange
| exp                   exponentia
| fill                  reple
| filter                filtrata
| find                  inventa
| find_all              collecta
| first                 primus
| flatten               planata
| flip                  alterna
| flipped               alternata
| floor                 pavimentum
| formata               formata
| from_flat             strue
| gather                gather
| gelu                  gelu
| get                   accipe
| greater               maior
| group                 coetus
| has                   habet
| intersect             inter
| intersection          intersectio
| invert                inversa
| is_empty              vacua
| is_subset             subcopia
| is_superset           supercopia
| keys                  claves
| last                  ultimus
| layer_norm            laminatio
| length                longitudo
| less                  minor
| ln                    logarithmus
| load                  load
| log10                 logarithmus_decimalis
| lowercase             minuscula
| map                   mappata
| matches               consentit
| materialize           materialize
| matmul                matmul
| maximum               maximus
| mean                  media
| minimum               minimus
| modulo                modulata
| modulo_assign         modula
| multiplied            multiplicata
| multiply              multiplica
| named                 nominatus
| negate                nega
| negated               negativa
| nonzero_count         nonnihil
| normalize             normalizata
| power                 potentia
| put                   pone
| reduce                reducta
| relu                  activatio_relu
| remove_first          decapita
| remove_last           detrahe
| replace               muta
| reshape               forma
| reverse               inverte
| rms_norm              rms_norm
| rope_norm             rope_norm
| round                 rotunda
| set                   ponde
| shape                 magnitudines
| shift_left            sinistra
| shift_right           dextra
| shifted_left          sinistrata
| shifted_right         dextrata
| sign                  signum
| silu                  silu
| sin                   sinus
| slice                 sectio
| softmax               activatio_softmax
| sort                  ordina
| sorted                ordinata
| split                 divide
| sqrt                  radix
| start                 principium
| starts_with           initium
| store                 store
| subtract              subtrahe
| subtracted            subtracta
| sum                   summa
| swizzle               swizzle
| symmetric_difference  symmetrica
| take                  prima
| take_last             ultima
| tan                   tangens
| text                  inventum
| transpose             transpone
| trim                  recide
| truncate              trunca
| union                 unio
| union                 union
| uppercase             maiuscula
| values                valores
```

---

[All reader locales](/language/reader-locales.html) · [Full keyword mapping](/language/locales/keywords.html) · [Diagnostics in this locale](/language/locales/diagnostics.html)
