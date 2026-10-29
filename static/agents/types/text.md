# Text windows

`s.slice(a, b)` is the half-open window of characters `a` up to `b`. It is
failable: an end past the length, a negative bound or a start past the end is
reported on the `⇥` channel, and the text is never clamped. Outside `main` the
call needs a `⊥` recovery value, a `do { } catch`, or a failable enclosing
function.

```faber locale=en
fn window(string s, int lo, int hi) → string {
    return s.slice(lo, hi) ⊥ "reported"
}

main {
    let string s ← "héllo"
    print s.slice(1, 3) ⊥ "reported"
    print window(s, 2, 99)
}
```

This prints `él` and `reported`.

Parent: https://faberlang.dev/agents/types.md
