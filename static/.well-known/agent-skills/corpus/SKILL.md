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
| Generated docs hub | https://faberlang.dev/corpus/ |
| Category indexes | https://faberlang.dev/corpus/category/ |
| Source tree | https://github.com/faberlang/examples/tree/main/corpus |
| Ecosystem note | https://faberlang.dev/ecosystem/corpus.html |

## How to look up a construct

1. Guess the Latin or English term (e.g. `functio`, `si`, `redde`, `←`).
2. Open `https://faberlang.dev/corpus/<term>.html` when known.
3. Or browse https://faberlang.dev/corpus/ and category pages.
4. For source programs, open the matching directory under `examples/corpus/`.

Example term page: https://faberlang.dev/corpus/functio.html

## Notes

- Corpus programs are the authority for construct shape used by the site generator.
- Prefer corpus + syntax docs together over inventing syntax from memory.

## Related

- skill: `language`
- skill: `examples`
- Syntax hub: https://faberlang.dev/syntax/
