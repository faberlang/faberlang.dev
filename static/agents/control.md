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

A `thread` loop (`for from t at [i] thread lane let v { … }`) runs its
iterations as independent lanes. `continue` skips the rest of one lane; `break`
and a plain `return` are refused (`SEM010 break_in_thread_body`,
`return_in_thread_body`). `return thread` ends the current lane from any depth
of the lane body, takes no value, and is refused outside a thread loop
(`SEM010 return_thread_outside_lane`). In 1.17 it is checked but not compiled:
code generation refuses it with `return_thread_lowering_pending`.

Fetch list: https://faberlang.dev/agents/index.md
