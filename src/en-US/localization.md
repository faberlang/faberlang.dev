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
class Span {
    const f64 low
    const f64 high

    fn contains(f64 x) → bool {
        return self.low ≤ x and x ≤ self.high
    }

    fn center() → f64 {
        return (self.low + self.high) ÷ 2.0
    }
}

fn choose<T>(bool first, T a, T b) → T {
    return first ✓ a ✗ b
}

main {
    const Span bytes ← Span { low = 0.0, high = 255.0 }
    print bytes.center()
    print choose(bytes.contains(300.0), "inside", "outside")
    print -7 / 2
}
```

## Latin {#la}

**Canonical surface.** Latin is the interchange dialect because it is **neutral relative to every modern national language**. No living population has a claim on it, so no reader pack has to be the one that everyone else is a translation of.

*Architectural stress:* None unique — by design. It is the complete template every translated pack is built from.

```faber locale=la
genus Span {
    fixum f64 low
    fixum f64 high

    functio contains(f64 x) → bivalens {
        redde ego.low ≤ x et x ≤ ego.high
    }

    functio center() → f64 {
        redde (ego.low + ego.high) ÷ 2.0
    }
}

functio choose<T>(bivalens first, T a, T b) → T {
    redde first ✓ a ✗ b
}

incipit {
    fixum Span bytes ← Span { low = 0.0, high = 255.0 }
    nota bytes.center()
    nota choose(bytes.contains(300.0), "inside", "outside")
    nota -7 / 2
}
```

## ภาษาไทย — Thai {#th-th}

**The tokenizer stress test.** The original access-wedge choice: a large developer population with low English proficiency and no existing native-programming-language tradition. It tests the access thesis directly rather than theoretically.

*Architectural stress:* **Spaceless script.** Thai has no inter-word boundaries, so a tokenizer that quietly assumed whitespace separates words breaks immediately. Combining vowel and tone marks stack on base characters, so a keyword is not a run of independent code points.

```faber locale=th-TH
ชนิด Span {
    คงที่ f64 low
    คงที่ f64 high

    ฟังก์ชัน contains(f64 x) → ตรรกะ {
        คืน ตัวฉัน.low ≤ x และ x ≤ ตัวฉัน.high
    }

    ฟังก์ชัน center() → f64 {
        คืน (ตัวฉัน.low + ตัวฉัน.high) ÷ 2.0
    }
}

ฟังก์ชัน choose<T>(ตรรกะ first, T a, T b) → T {
    คืน first ✓ a ✗ b
}

เริ่ม {
    คงที่ Span bytes ← Span { low = 0.0, high = 255.0 }
    บันทึก bytes.center()
    บันทึก choose(bytes.contains(300.0), "inside", "outside")
    บันทึก -7 / 2
}
```

## 简体中文 — Simplified Chinese {#zh-hans}

**Width, pairing, and emission fidelity.** Optimizes for reach while surfacing the deepest set of script problems beyond tokenization.

*Architectural stress:* **Full-width and half-width punctuation** collapse under NFKC normalization, so the compiler cannot treat visually distinct characters as distinct tokens. **Paired keywords** (如果 / 否则) are single tokens rather than multi-token phrases, which is what forced reader packs to support keyword groups at all.

```faber locale=zh-Hans
类 Span {
    常量 f64 low
    常量 f64 high

    函数 contains(f64 x) → 布尔 {
        返回 自身.low ≤ x 且 x ≤ 自身.high
    }

    函数 center() → f64 {
        返回 (自身.low + 自身.high) ÷ 2.0
    }
}

函数 choose<T>(布尔 first, T a, T b) → T {
    返回 first ✓ a ✗ b
}

入口 {
    常量 Span bytes ← Span { low = 0.0, high = 255.0 }
    显示 bytes.center()
    显示 choose(bytes.contains(300.0), "inside", "outside")
    显示 -7 / 2
}
```

## 繁體中文 — Traditional Chinese {#zh-hant}

**Sibling-pack divergence.** Not a variant spelling of Simplified — a separate pack with genuinely different vocabulary. `常量` against `定值` for the same concept.

*Architectural stress:* **Sibling packs.** Two packs for one language proved the substrate could carry divergent vocabulary over identical semantics, and forced the vocabulary-governance rules that keep them from drifting apart.

```faber locale=zh-Hant
類型 Span {
    定值 f64 low
    定值 f64 high

    函式 contains(f64 x) → 布林 {
        傳回 自身.low ≤ x 且 x ≤ 自身.high
    }

    函式 center() → f64 {
        傳回 (自身.low + 自身.high) ÷ 2.0
    }
}

函式 choose<T>(布林 first, T a, T b) → T {
    傳回 first ✓ a ✗ b
}

入口 {
    定值 Span bytes ← Span { low = 0.0, high = 255.0 }
    註記 bytes.center()
    註記 choose(bytes.contains(300.0), "inside", "outside")
    註記 -7 / 2
}
```

## Tiếng Việt — Vietnamese {#vi}

**The Latin-script control.** The control case. Without it the architecture could be "works on exotic scripts, unproven on Latin" — correct for the hard cases and quietly wrong for the familiar one.

*Architectural stress:* **Heavy diacritics on Latin script.** NFKC edge cases and accent-sensitive suggestion matching, where two spellings look nearly identical and must not be confused. Multi-word keywords join with underscores: `bắt_đầu`.

```faber locale=vi
kiểu Span {
    hằng f64 low
    hằng f64 high

    hàm contains(f64 x) → logic {
        trả tôi.low ≤ x và x ≤ tôi.high
    }

    hàm center() → f64 {
        trả (tôi.low + tôi.high) ÷ 2.0
    }
}

hàm choose<T>(logic first, T a, T b) → T {
    trả first ✓ a ✗ b
}

bắt_đầu {
    hằng Span bytes ← Span { low = 0.0, high = 255.0 }
    ghi_chú bytes.center()
    ghi_chú choose(bytes.contains(300.0), "inside", "outside")
    ghi_chú -7 / 2
}
```

## العربية — Arabic {#ar}

**The required RTL pack.** The only right-to-left language in the set. Without it the architecture can ship code that is correct on paper and renders wrong on screen — and nobody would find out from a test suite.

*Architectural stress:* **Bidirectional text.** Contextual glyph shaping, ligatures, and the split between logical and visual order. Diagnostics have to bidi-isolate the source they quote, or an error message points at the wrong character.

```faber locale=ar
صنف Span {
    ثابت f64 low
    ثابت f64 high

    دالة contains(f64 x) → منطقي {
        أعد ذات.low ≤ x و x ≤ ذات.high
    }

    دالة center() → f64 {
        أعد (ذات.low + ذات.high) ÷ 2.0
    }
}

دالة choose<T>(منطقي first, T a, T b) → T {
    أعد first ✓ a ✗ b
}

بداية {
    ثابت Span bytes ← Span { low = 0.0, high = 255.0 }
    اعرض bytes.center()
    اعرض choose(bytes.contains(300.0), "inside", "outside")
    اعرض -7 / 2
}
```

## हिन्दी — Hindi {#hi}

**The Indic-family representative.** Stands in for the whole Indic family. A pack that handles Devanagari proves the path for Bengali, Tamil, Telugu, Gujarati, and the rest — they inherit the substrate this one established.

*Architectural stress:* **Matra and virama consonant clusters**, where a grapheme spans several code points and NFKC equivalence has to hold. It is also the pack that confirmed **Indic numerals** (०-९) stay rejected inside numeric literals — a digit that looks like a number but is not one.

```faber locale=hi
वर्ग Span {
    स्थिर f64 low
    स्थिर f64 high

    फलन contains(f64 x) → तार्किक {
        लौटाओ मैं.low ≤ x और x ≤ मैं.high
    }

    फलन center() → f64 {
        लौटाओ (मैं.low + मैं.high) ÷ 2.0
    }
}

फलन choose<T>(तार्किक first, T a, T b) → T {
    लौटाओ first ✓ a ✗ b
}

आरंभ {
    स्थिर Span bytes ← Span { low = 0.0, high = 255.0 }
    दिखाओ bytes.center()
    दिखाओ choose(bytes.contains(300.0), "inside", "outside")
    दिखाओ -7 / 2
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
