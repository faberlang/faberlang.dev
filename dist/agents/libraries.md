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

`norma:*` is embedded in the `faber` binary and needs no setup. Other libraries
(`triga:`, `gradus:`, `tela:`) are separate checkouts. Point the compiler at the
directory that holds them with `--library-home DIR`, or `[paths] library_home`
in `faber.toml`. Without that, the import is `PKG001` `unknown_library_provider`.
`faber doctor` prints the resolved library home and which libraries it finds.

Fetch list: https://faberlang.dev/agents/index.md
