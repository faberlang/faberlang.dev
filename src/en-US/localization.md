+++
title = "Localization"
section = "localization"
order = 2
sources = [
  "radix/docs/design/reader-locale.md",
]
+++

Faber source can be read in eight human languages. Not translated — *rendered*.
The compiler holds one analyzed program and prints it in whichever reader
locale you ask for, so keywords and type names change while identifiers, string
literals, and the glyphs carrying structure stay exactly where they were.

That is what makes cross-language review possible: two people can hold the same
package open in different languages and be editing one program.

## Why these languages {#why}

The set is not the eight largest languages, and it is not a wish list. Each
pack was selected against three axes:

| Axis | Question |
|---|---|
| **Access** | Does this population face a real English barrier when programming? |
| **Reach** | How many developers does it serve? |
| **Architectural stress** | Does it force the compiler to confront a Unicode or emission problem no other pack does? |

The third axis is the lever. A set chosen for population alone proves nothing
the substrate did not already handle; a set chosen for
**collective architectural coverage** turns "pick languages" into
"derive architecture."
Every major Unicode axis — spaceless tokenization, width normalization,
bidirectional rendering, consonant clusters, diacritic-heavy Latin — is
stressed by at least one language here, on purpose.

## English {#en}

**Base surface.** The spelling most people write day to day, and the one English-trained models emit most reliably. It is a reader pack like any other — not a privileged default — but it is where most source starts.

*Architectural stress:* None unique. It is the baseline the others are measured against.

```faber locale=en
main {
    const tensor<f32, [2, 3]> a ← empty
    const tensor<f32, [3, 4]> b ← empty
    const tensor<f32, [2, 4]> product ← a · b
    print product
}
```

## Latin {#la}

**Canonical surface.** Latin is the interchange dialect because it is **neutral relative to every modern national language**. No living population has a claim on it, so no reader pack has to be the one that everyone else is a translation of.

*Architectural stress:* None unique — by design. It is the complete template every translated pack is built from.

```faber locale=la
incipit {
    fixum tensor<f32, [2, 3]> a ← vacua
    fixum tensor<f32, [3, 4]> b ← vacua
    fixum tensor<f32, [2, 4]> product ← a · b
    nota product
}
```

## ภาษาไทย — Thai {#th-th}

**The tokenizer stress test.** The original access-wedge choice: a large developer population with low English proficiency and no existing native-programming-language tradition. It tests the access thesis directly rather than theoretically.

*Architectural stress:* **Spaceless script.** Thai has no inter-word boundaries, so a tokenizer that quietly assumed whitespace separates words breaks immediately. Combining vowel and tone marks stack on base characters, so a keyword is not a run of independent code points.

```faber locale=th-TH
เริ่ม {
    คงที่ เทนเซอร์<f32, [2, 3]> a ← เซตว่าง
    คงที่ เทนเซอร์<f32, [3, 4]> b ← เซตว่าง
    คงที่ เทนเซอร์<f32, [2, 4]> product ← a · b
    บันทึก product
}
```

## 简体中文 — Simplified Chinese {#zh-hans}

**Width, pairing, and emission fidelity.** Optimizes for reach while surfacing the deepest set of script problems beyond tokenization.

*Architectural stress:* **Full-width and half-width punctuation** collapse under NFKC normalization, so the compiler cannot treat visually distinct characters as distinct tokens. **Paired keywords** (如果 / 否则) are single tokens rather than multi-token phrases, which is what forced reader packs to support keyword groups at all.

```faber locale=zh-Hans
入口 {
    常量 张量<f32, [2, 3]> a ← 空集
    常量 张量<f32, [3, 4]> b ← 空集
    常量 张量<f32, [2, 4]> product ← a · b
    显示 product
}
```

## 繁體中文 — Traditional Chinese {#zh-hant}

**Sibling-pack divergence.** Not a variant spelling of Simplified — a separate pack with genuinely different vocabulary. `常量` against `定值` for the same concept.

*Architectural stress:* **Sibling packs.** Two packs for one language proved the substrate could carry divergent vocabulary over identical semantics, and forced the vocabulary-governance rules that keep them from drifting apart.

```faber locale=zh-Hant
入口 {
    定值 張量<f32, [2, 3]> a ← 空集
    定值 張量<f32, [3, 4]> b ← 空集
    定值 張量<f32, [2, 4]> product ← a · b
    註記 product
}
```

## Tiếng Việt — Vietnamese {#vi}

**The Latin-script control.** The control case. Without it the architecture could be "works on exotic scripts, unproven on Latin" — correct for the hard cases and quietly wrong for the familiar one.

*Architectural stress:* **Heavy diacritics on Latin script.** NFKC edge cases and accent-sensitive suggestion matching, where two spellings look nearly identical and must not be confused. Multi-word keywords join with underscores: `bắt_đầu`.

```faber locale=vi
bắt_đầu {
    hằng ten_xo<f32, [2, 3]> a ← tập_rỗng
    hằng ten_xo<f32, [3, 4]> b ← tập_rỗng
    hằng ten_xo<f32, [2, 4]> product ← a · b
    ghi_chú product
}
```

## العربية — Arabic {#ar}

**The required RTL pack.** The only right-to-left language in the set. Without it the architecture can ship code that is correct on paper and renders wrong on screen — and nobody would find out from a test suite.

*Architectural stress:* **Bidirectional text.** Contextual glyph shaping, ligatures, and the split between logical and visual order. Diagnostics have to bidi-isolate the source they quote, or an error message points at the wrong character.

```faber locale=ar
بداية {
    ثابت موتر<f32, [2, 3]> a ← فارغ
    ثابت موتر<f32, [3, 4]> b ← فارغ
    ثابت موتر<f32, [2, 4]> product ← a · b
    اعرض product
}
```

## हिन्दी — Hindi {#hi}

**The Indic-family representative.** Stands in for the whole Indic family. A pack that handles Devanagari proves the path for Bengali, Tamil, Telugu, Gujarati, and the rest — they inherit the substrate this one established.

*Architectural stress:* **Matra and virama consonant clusters**, where a grapheme spans several code points and NFKC equivalence has to hold. It is also the pack that confirmed **Indic numerals** (०-९) stay rejected inside numeric literals — a digit that looks like a number but is not one.

```faber locale=hi
आरंभ {
    स्थिर टेंसर<f32, [2, 3]> a ← खाली
    स्थिर टेंसर<f32, [3, 4]> b ← खाली
    स्थिर टेंसर<f32, [2, 4]> product ← a · b
    दिखाओ product
}
```

## Why not others {#why-not}

Reasonable languages that are deliberately absent, and what it would take to
add them:

| Language | Why not yet |
|---|---|
| **Japanese** | The natural next addition. Its concerns — Kanji/Kana mixing, paired constructs — overlap heavily with Chinese, so it adds reach more than new architecture. If the set grows, this is next. |
| **Korean** | Hangul handles cleanly under XID identifier rules, so it needs no new substrate work. |
| **Spanish · French · Russian · Portuguese** | Little unique architectural stress, and weaker access wedges — these populations broadly reach English already. Adding them is vocabulary work, not compiler work. |
| **Bengali · Tamil · Telugu · Gujarati** | Subsumed by Hindi as the Indic representative. Their packs inherit the substrate Hindi proved; they are additions, not new problems. |
| **Swahili · Hausa** | A genuine access wedge, but current LLM coverage is thin and developer populations small, so the authoring loop does not close yet. Worth revisiting as coverage improves. |

Absence is not judgement. A language missing from this list is missing because
it would not teach the compiler anything new — which means adding it later is
mostly translation, not architecture.

## What does not change {#invariant}

Across every pack above:

- **Glyphs** — `←` `→` `∴` `≡` `∪` `⇥` — never localize. Structure reads the
  same everywhere.
- **Identifiers and string literals** stay exactly as written.
- **The machine interior** — HIR, stable diagnostic codes, `norma:*` package
  ids — stays Latin behind the curtain, so tooling is not chasing a moving
  target.

Diagnostics render in your reader locale too. An error at the fault site is not
English prose sitting inside Thai source.

## Switching locale {#switching}

```bash
faber convert --to th-TH <package>
```

A reader locale is a rendering choice, not a fork. There is one grammar; only
its surface spelling moves.

Related: [Reader locales](/language/reader-locales.html) for the full
mechanism · [Glyphs and Latin](/language/glyphs.html) for why the glyphs hold
still · [Cheat sheet](/cheatsheet/) where every example carries all eight
surfaces
