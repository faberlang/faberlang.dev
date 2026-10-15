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

The panels below are the committed `generator/locale-tabs/` cache — `faber convert` output, not hand-written Thai or Arabic. The Latin panel is the identity pack's rendering; the rest are that same program rendered into each locale.

## English (`en`) {#en}

```text locale=en
main {
    print "Hello, world!"
}
```

## Latin (`la`) {#la}

```faber locale=la
incipit {
    nota "Hello, world!"
}
```

The same program on the identity pack, whose words are the pack keys.

## Arabic (`ar`) {#ar}

```text locale=ar
بداية {
    اعرض "Hello, world!"
}
```

## Hindi (`hi`) {#hi}

```text locale=hi
आरंभ {
    दिखाओ "Hello, world!"
}
```

## Thai (`th-TH`) {#th-th}

```text locale=th-TH
เริ่ม {
    บันทึก "Hello, world!"
}
```

## Vietnamese (`vi`) {#vi}

```text locale=vi
bắt_đầu {
    ghi_chú "Hello, world!"
}
```

## Simplified Chinese (`zh-Hans`) {#zh-hans}

```text locale=zh-Hans
入口 {
    显示 "Hello, world!"
}
```

## Traditional Chinese (`zh-Hant`) {#zh-hant}

```text locale=zh-Hant
入口 {
    註記 "Hello, world!"
}
```

---

[All reader locales](/language/reader-locales.html) · [Keyword reference](/language/locales/keywords.html)
