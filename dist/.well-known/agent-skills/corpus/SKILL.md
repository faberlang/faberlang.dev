---
name: "corpus"
description: "Look up language constructs via generated corpus pages and the examples/corpus source tree."
---

# Faber language corpus

## Use this skill when

- you need an example for a specific keyword, glyph, or construct
- docs HTML is thin and you want source programs
- generating or validating language-surface coverage

## Surfaces

| Surface | URL |
|---|---|
| Generated docs hub (English) | https://faberlang.dev/en-US/corpus/ |
| Example category index | https://faberlang.dev/en-US/corpus/category/function.html |
| Source tree | https://github.com/faberlang/examples/tree/main/corpus |
| Ecosystem note | https://faberlang.dev/en-US/ecosystem/corpus.html |
| Machine index (all terms) | https://faberlang.dev/llms.txt |

## How to look up a construct

1. Guess the Latin or English term (e.g. `functio`, `si`, `redde`, `←`).
2. Open `https://faberlang.dev/en-US/corpus/<term>.html` when known
   (URL-encode special characters in the term).
3. Or browse https://faberlang.dev/en-US/corpus/ and category pages.
4. For source programs, open the matching directory under `examples/corpus/`.
5. Other site locales mirror corpus under `/{locale}/corpus/` with the same
   term set and locale-specific code samples.

Example term page: https://faberlang.dev/en-US/corpus/functio.html

## Notes

- Corpus programs are the authority for construct shape used by the site generator.
- Prefer corpus + syntax docs together over inventing syntax from memory.
- Prefer `/en-US/corpus/…` over bare `/corpus/…` (the latter is a redirect stub).

## Related

- skill: `language`
- skill: `examples`
- Syntax hub: https://faberlang.dev/en-US/syntax/
