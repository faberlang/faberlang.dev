+++
title = "Reader locales"
section = "cheatsheet"
order = 41
sources = []
+++

The same program, rendered in eight human languages. Not a translation of a
document — the compiler renders source into a reader locale, so what you see
below is the same analyzed program every time.

Keywords and primitive type names remap. **Identifiers and string literals do
not.** `flat_a` stays `flat_a` in Arabic; `media()` stays `media()` in Thai.
That is what makes a review across locales possible: the nouns of your program
are stable, only the grammar words move.

Every panel on this page is compiler output, captured from the toolchain rather
than written by hand.

## The program {#program}

It builds two typed matrices, multiplies them, and reduces the product to a
scalar mean.

### English {#en}

The English reader surface — the base spelling for everyday source.

```faber locale=en
main {
    const list<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    const list<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    const tensor<f32, []> seed ← vacua
    const tensor<f32, [2, 3]> a ← seed.strue(flat_a, [2, 3])
    const tensor<f32, [3, 4]> b ← seed.strue(flat_b, [3, 4])
    const tensor<f32, [2, 4]> product ← a.matmul(b)
    const f32 mean ← product.media()
    print mean
}
```

### Latin {#la}

Canonical Faber, the classical surface the language is named for.

```faber locale=la
incipit {
    fixum lista<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    fixum lista<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    fixum tf32[] seed ← vacua
    fixum tf32[2, 3] a ← seed.strue(flat_a, [2, 3])
    fixum tf32[3, 4] b ← seed.strue(flat_b, [3, 4])
    fixum tf32[2, 4] product ← a.matmul(b)
    fixum f32 mean ← product.media()
    nota mean
}
```

### ภาษาไทย — Thai {#th-th}

A spaceless script; the compiler tokenizes it the same way.

```faber locale=th-TH
เริ่ม {
    คงที่ รายการ<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    คงที่ รายการ<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    คงที่ tensor<f32, []> seed ← vacua
    คงที่ tensor<f32, [2, 3]> a ← seed.strue(flat_a, [2, 3])
    คงที่ tensor<f32, [3, 4]> b ← seed.strue(flat_b, [3, 4])
    คงที่ tensor<f32, [2, 4]> product ← a.matmul(b)
    คงที่ f32 mean ← product.media()
    บันทึก mean
}
```

### 简体中文 — Simplified Chinese {#zh-hans}

Keywords and type names remap; identifiers do not.

```faber locale=zh-Hans
入口 {
    常量 列表<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    常量 列表<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    常量 tensor<f32, []> seed ← vacua
    常量 tensor<f32, [2, 3]> a ← seed.strue(flat_a, [2, 3])
    常量 tensor<f32, [3, 4]> b ← seed.strue(flat_b, [3, 4])
    常量 tensor<f32, [2, 4]> product ← a.matmul(b)
    常量 f32 mean ← product.media()
    显示 mean
}
```

### 繁體中文 — Traditional Chinese {#zh-hant}

A separate pack from Simplified — `常量` against `定值`.

```faber locale=zh-Hant
入口 {
    定值 列表<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    定值 列表<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    定值 tensor<f32, []> seed ← vacua
    定值 tensor<f32, [2, 3]> a ← seed.strue(flat_a, [2, 3])
    定值 tensor<f32, [3, 4]> b ← seed.strue(flat_b, [3, 4])
    定值 tensor<f32, [2, 4]> product ← a.matmul(b)
    定值 f32 mean ← product.media()
    註記 mean
}
```

### Tiếng Việt — Vietnamese {#vi}

Multi-word keywords join with underscores: `bắt_đầu`.

```faber locale=vi
bắt_đầu {
    hằng danh_sách<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    hằng danh_sách<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    hằng tensor<f32, []> seed ← vacua
    hằng tensor<f32, [2, 3]> a ← seed.strue(flat_a, [2, 3])
    hằng tensor<f32, [3, 4]> b ← seed.strue(flat_b, [3, 4])
    hằng tensor<f32, [2, 4]> product ← a.matmul(b)
    hằng f32 mean ← product.media()
    ghi_chú mean
}
```

### العربية — Arabic {#ar}

Right-to-left, bidi isolated. Identifiers stay left-to-right.

```faber locale=ar
بداية {
    ثابت قائمة<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    ثابت قائمة<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    ثابت tensor<f32, []> seed ← vacua
    ثابت tensor<f32, [2, 3]> a ← seed.strue(flat_a, [2, 3])
    ثابت tensor<f32, [3, 4]> b ← seed.strue(flat_b, [3, 4])
    ثابت tensor<f32, [2, 4]> product ← a.matmul(b)
    ثابت f32 mean ← product.media()
    اعرض mean
}
```

### हिन्दी — Hindi {#hi}

Devanagari keywords over unchanged identifiers and literals.

```faber locale=hi
आरंभ {
    स्थिर सूची<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    स्थिर सूची<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    स्थिर tensor<f32, []> seed ← vacua
    स्थिर tensor<f32, [2, 3]> a ← seed.strue(flat_a, [2, 3])
    स्थिर tensor<f32, [3, 4]> b ← seed.strue(flat_b, [3, 4])
    स्थिर tensor<f32, [2, 4]> product ← a.matmul(b)
    स्थिर f32 mean ← product.media()
    दिखाओ mean
}
```

## Switching locale {#switching}

Render existing source into another locale with `faber format`:

```bash
faber format --reader-locale th-TH <package>
```

The reader locale is a rendering choice, not a fork. Two people can hold the
same package open in different locales and be editing one program.

## What this is not {#not}

- Not a translation layer over the page. The compiler produces these.
- Not string localization. Your `"messages"` are untouched.
- Not a dialect. There is one grammar; only its surface spelling changes.

Related: [Reader locales](/language/reader-locales.html) for the full
mechanism · [Glyphs and Latin](/language/glyphs.html) for why the glyphs stay
constant across every pack
