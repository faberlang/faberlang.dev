# Libraries

Norma is the standard library. Import a module by its quoted path and
bind a name. `text.reverse` returns the reversed string.

```faber locale=en
import from "norma:text" text

main {
    print text.reverse("ab")
}
```

`faber run` on this program prints `ba`.

Fetch list: https://faberlang.dev/agents/index.md
