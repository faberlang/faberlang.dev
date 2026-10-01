# Locales

One source file uses one locale pack. The files in this canon are
English. Keywords, types, and library members in a file come from that
pack.

A comment is a `#` line by itself.

```faber locale=en
# English source.
main {
    print "en"
}
```

Do not write `//`. That is rejected as `LEX006` `c_style_line_comment`.
Do not put `#` after code on the same line. That is rejected as `LEX007`
`inline_hash_after_code`.

Fetch list: https://faberlang.dev/agents/index.md
