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

Parent: https://faberlang.dev/agents/types.md
Next: https://faberlang.dev/agents/types/conversions.md
