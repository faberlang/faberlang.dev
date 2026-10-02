+++
title = "Sealed reader locales"
section = "language"
order = 13
sources = [
  "radix/docs/design/reader-locale.md",
  "examples/reader-locale/",
]
+++

Large models have localised the *conversation* around programming. A Thai
computer scientist can ask for help in Thai. The durable artifact — the source,
the compiler errors, the standard library — stayed English-shaped, so English
proficiency became a gate to computer science rather than to conversation.

A reader locale is Faber's answer: the compiler renders keywords, primitive
type names and diagnostics in the reader's language, without forking the
semantics. A Thai file and a Latin file lower to exactly the same HIR. The
mechanism that renders Faber to Thai is the same one that renders it to Rust —
`HIR → surface` — and neither is privileged.

## One file, one locale {#sealed}

A source file is lexed under **exactly one** reader pack. Keywords from another
pack are not keywords there, they are ordinary identifiers, so a file that
mixes surfaces does not compile as a mixture — it fails. Sealing is what makes
a locale surface reliable: inside a Thai file, every keyword is Thai, and a
reader never has to hold two vocabularies at once.

```faber outcome=rejects
functio duplica(numerus n) → numerus {
    return n * 2
}
```

`return` is the English spelling of the Latin keyword `redde`; under the Latin
pack it is just a name, and the file is rejected. The fix is to pick one
surface for the file.

## The glyphs never move {#glyphs}

Only words are localised. The glyphs (`←`, `→`, `⇥`, `≡`, `∪`, `↦`) and the
type-first order are identical in every rendering, and identifiers are
preserved byte-for-byte. A reader who knows Faber in one locale can read it in
any locale, because the structure is the part that does not change. Numerals
stay ASCII everywhere.

## It is never a one-way door {#lossless}

Any surface can become any other, including canonical Latin, at any time.
`faber format --locale la` re-emits the canonical surface, so a localised file
is never trapped in one vocabulary. This is the same canonical-versus-sugar
property as the glyph law: one defined form, many renderings of it.

## What it looks like {#shape}

The same source, in canonical Latin and rendered into Thai:

```faber
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    nota salve("munde")
}
```

```console
$ faber convert --from la --to th-TH
ฟังก์ชัน salve(ข้อความ nomen) → ข้อความ {
    คงที่ ข้อความ msg ← "Salve, §!"(nomen)
    คืน msg
}

เริ่ม {
    บันทึก salve("munde")
}
```

The keywords and type names changed; the glyphs, the order, and the identifier
`salve` did not. The program still runs:

```text
$ faber run
Salve, munde!
```

Eight packs ship today: `en` (the base English surface), `la` (canonical
Latin), and `th-TH`, `zh-Hans`, `zh-Hant`, `ar`, `hi`, `vi` as the reference
set. The reference locales are chosen for architectural stress — a spaceless
script, right-to-left runs, half/full-width pairs and NFKC width collapse —
not for population.
Diagnostics are structured facts with stable codes and named arguments, so the
same message renders in any pack. The full tables are in
[Reader locales](/language/reader-locales.html).
