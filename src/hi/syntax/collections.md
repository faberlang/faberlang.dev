+++
translation_kind = "translated"

title = "Collections"
section = "syntax"
order = 7
sources = [
  "radix/README.md (Tensors And Sparsa)",
  "radix/docs/design/lista-intrinsics.md",
  "radix/docs/design/tabula-intrinsics.md",
  "radix/docs/design/tensor-intrinsics.md",
  "examples/corpus/lista/",
  "examples/corpus/tabula/",
  "examples/corpus/tensor/",
  "examples/corpus/sparsa/",
]


prose_hash = "sha256:a27f17bb659e59b09584d162f997eb5bba7534e0523767113e9d10559ae8e22d"
code_hash = "sha256:e9cb3fb1f45f7234d5ab43350f4d913db04eb58f4ee1854d59af1238e75ac07a"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber में कंपाइलर द्वारा स्वामित्व वाले कई कलेक्शन प्रकार हैं। इनके कैनोनिकल तरीके स्टैंडर्ड लाइब्रेरी में नहीं, बल्कि कंपाइलर में परिभाषित होते हैं।

## Lista — क्रमबद्ध डायनेमिक कलेक्शन {#lista}

```faber
fixum lista<numerus> empty ← vacua
fixum _ numbers ← [1, 2, 3, 4, 5]
fixum _ names ← ["Marcus", "Julia", "Gaius"]
fixum _ nested ← [[1, 2], [3, 4]]
```

`sparge` के साथ स्प्रेड करें:

```faber
fixum _ a ← [1, 2, 3]
fixum _ b ← [4, 5, 6]
fixum _ combined ← [sparge a, sparge b]
fixum _ headed ← [0, sparge a, 99]
```

मुख्य तरीके: `longitudo`, `accipe`, `appende`, `summa`, `primus`, `novissimus`।

## Tabula — कुंजी-मान मैप {#tabula}

```faber
fixum tabula<textus, numerus> scores ← { "alice": 10, "bob": 20 }
```

## Tensor — घना निश्चित-आकार बफ़र {#tensor}

```faber
fixum tensor<fractus<f32>, []> scalar ← vacua
fixum tensor<numerus, [4]> vector ← [1, 2, 3, 4] ↦ tensor<numerus, [4]>
fixum numerus ∪ nihil first ← vector[0]
```

Tensor शुगर (संख्यात्मक कोड के लिए):

```faber
fixum tf32[] seed ← vacua
fixum tf32[4] lanes ← seed.strue([1.0, 2.0, 3.0, 4.0], [4])
```

मुख्य तरीके: `forma`, `accipe`, `ponde`, `crea`, `structa`, `strue`, साथ ही
तत्व-स्तरीय अंकगणित, मैट्रिक्स गुणन (`multiplicatio`) और
रिडक्शन (`summa`, `productum`)।

## Sparsa — विरल निश्चित-आकार बफ़र {#sparsa}

```faber
fixum sparsa<fractus<f32>, [2, 3]> sparse ← vacua
sparse.ponde([0, 1], 4.0)
sparse.ponde([1, 2], 9.0)

# accipe returns the stored value, here 4.0
nota sparse.accipe([0, 1])
# count of stored entries
nota sparse.nonnihil()
```

घने और विरल रूपों के बीच रूपांतरण:

```faber
fixum tf32[2, 2] dense ← [[1.0, 0.0], [0.0, 2.0]] ↦ tf32[2, 2]
fixum sf32[2, 2] sparse ← dense ↦ sf32[2, 2]
fixum tf32[2, 2] roundtrip ← sparse ↦ tf32[2, 2]
```

## Cursors — लेज़ी स्ट्रीम {#cursors}

`cursor<T>` एक लेज़ी स्ट्रीम प्रकार है। इसे कलेक्शन इटरेटर, `tuus` व्यू या जनरेटर फ़ंक्शन से बनाया जाता है। इसका उपभोग `itera ex` के माध्यम से किया जाता है:

```faber
fixum _ items ← [1, 2, 3]
itera ex items fixum item {
    nota item
}
```

## Intervallum — रेंज {#intervallum}

```faber
# exclusive range: 0, 1, 2, 3, 4
itera ab 0‥5 fixum i {
    nota i
}
# inclusive range: 0, 1, 2, 3, 4, 5
itera ab 0…5 fixum i {
    nota i
}
```

`‥` एक्सक्लूसिव रेंज एंडपॉइंट है; `…` इनक्लूसिव है।
