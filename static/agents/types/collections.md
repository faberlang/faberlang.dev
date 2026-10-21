# Collections

A list names its element type. `empty` is the empty list. A literal writes
the elements in brackets.

```faber locale=en
main {
    let list<i32> nums ← [1, 2, 3]
    let list<i32> blank ← empty
    print nums
    print blank
}
```

`take(n)` and `slice(a, b)` report a window that runs past the end; they do
not clamp. Both are failable: outside `main` give them a handler, such as a
`⊥` recovery value.

```faber locale=en
fn head(list<i32> xs, i32 n) → list<i32> {
    return xs.take(n) ⊥ xs
}

main {
    let list<i32> nums ← [1, 2, 3]
    print head(nums, 2)
    print head(nums, 9)
}
```

This prints `[1, 2]` and `[1, 2, 3]`.

A range is a value of type `range<int>`. `for range` walks it.

```faber locale=en
main {
    let range<int> r ← 0‥3
    print r
    for range r let i {
        print i
    }
}
```

Write `range`, not the Latin `intervallum`, and `sparse`, not `sparsa`, in an
English file (`PARSE040` `wrong_locale_type`).

Parent: https://faberlang.dev/agents/types.md
Next: https://faberlang.dev/agents/types/conversions.md
