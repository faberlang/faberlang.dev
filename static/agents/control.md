# Control

`if`, `elif`, and `else` choose a branch. `for from` walks a list. `while`
repeats while the condition holds.

```faber locale=en
main {
    const int score ← 85
    if score ≥ 90 {
        print "A"
    }
    elif score ≥ 80 {
        print "B"
    }
    else {
        print "C"
    }
    const list<int> nums ← [1, 2, 3]
    for from nums const item {
        print item
    }
    var int n ← 0
    while n ≺ 2 {
        n ← n + 1
    }
    print n
}
```

Fetch list: https://faberlang.dev/agents/index.md
