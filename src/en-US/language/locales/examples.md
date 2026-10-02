+++
title = "Locale examples"
section = "locales"
order = 3
sources = [
  "generator/locale-tabs/",
]
# This page is about the vocabulary itself; the reader-span pass would
# otherwise translate the reference it exists to show.
translate_spans = false
+++

One program, eight reader surfaces. Faber source is written once and printed in whichever locale the reader asks for: keywords and type names change, while identifiers, strings, and the glyphs carrying structure stay put.

The panels below are the committed `generator/locale-tabs/` cache — `faber convert` output, not hand-written Thai or Arabic. The Latin panel is canonical Faber; the rest are that same program rendered into each locale.

## English (`en`) {#en}

```text locale=en
main {
    print "Salve, munde!"
}
```

## Latin (`la`) {#la}

```faber locale=la
incipit {
    nota "Salve, munde!"
}
```

The canonical surface every other panel is a re-rendering of.

## Arabic (`ar`) {#ar}

```text locale=ar
بداية {
    اعرض "Salve, munde!"
}
```

## Hindi (`hi`) {#hi}

```text locale=hi
आरंभ {
    दिखाओ "Salve, munde!"
}
```

## Thai (`th-TH`) {#th-th}

```text locale=th-TH
เริ่ม {
    บันทึก "Salve, munde!"
}
```

## Vietnamese (`vi`) {#vi}

```text locale=vi
bắt_đầu {
    ghi_chú "Salve, munde!"
}
```

## Simplified Chinese (`zh-Hans`) {#zh-hans}

```text locale=zh-Hans
入口 {
    显示 "Salve, munde!"
}
```

## Traditional Chinese (`zh-Hant`) {#zh-hant}

```text locale=zh-Hant
入口 {
    註記 "Salve, munde!"
}
```

---

[All reader locales](/language/reader-locales.html) · [Keyword reference](/language/locales/keywords.html)
