# Control

`if`, `elif`, and `else` choose a branch. `for from` walks a list. `while`
repeats while the condition holds.

```faber locale=en
main {
    let int score ← 85
    if score ≥ 90 {
        print "A"
    }
    elif score ≥ 80 {
        print "B"
    }
    else {
        print "C"
    }
    let list<int> nums ← [1, 2, 3]
    for from nums let item {
        print item
    }
    mut int n ← 0
    while n ≺ 2 {
        n ← n + 1
    }
    print n
}
```

`and` walks several lists in one loop, in lockstep, with one binder per source
joined the same way. The lists must have the same length.

```faber locale=en
main {
    let list<string> labels ← ["one", "two", "three"]
    let list<int> values ← [1, 2, 3]
    for from labels and values let label and value {
        print label
        print value
    }
}
```

A comma in a loop head means the next loop in, and each clause after it starts
with `from` or `range`. `for from a, b` is refused (`PARSE001`
`itera_bare_comma_source`). In 1.19 nested comma clauses are not lowered
(`SEM008 itera_nested_clause_unsupported`): write nested loops.

A `thread` loop (`for from t at [i] thread lane let v { … }`) runs its
iterations as independent lanes. `continue` skips the rest of one lane; `break`
and a plain `return` are refused (`SEM010 break_in_thread_body`,
`return_in_thread_body`). `return thread` ends the current lane from any depth
of the lane body, takes no value, and is refused outside a thread loop
(`SEM010 return_thread_outside_lane`). In 1.19 it is checked but not compiled:
code generation refuses it with `return_thread_lowering_pending`.

Fetch list: https://faberlang.dev/agents/index.md
