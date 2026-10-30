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

A length limit is written after `size`: `list<int, size 4>` holds at most four
elements, and `list<int, size 1 … ∞>` is never empty (`…` includes its upper
bound, `‥` leaves it out). A bare `list<int, 4>` is `SEM008`
`list_count_needs_size`; `queue`, `stack`, `string`, `ascii` and `vector` take
the same `size` marker (`SEM008` `capacity_needs_size`, `vector_width_needs_size`).
A short list literal takes the capacity of the cell it is stored into, a call
argument included. Appending past the maximum reports on the error channel.

```faber locale=en
main {
    let list<int, size 0 … 3> pair ← [1, 2]
    print pair
    mut list<int, size 2 ‥ 5> ys ← [10, 20]
    do {
        ys.append(30)
        ys.append(40)
        ys.append(50)
    }
    catch err {
        print "full"
    }
    print ys
}
```

This prints `[1, 2]`, `full` and `[10, 20, 30, 40]`.

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

`s ⇜ x` sinks one item into a writable sink. On a list it appends (duplicates
kept); on a set it adds a missing item. A class becomes a sink with
`implements Sink<T>` and the methods `sink(T)` and `flush()`. In 1.18 the Go,
TypeScript, Swift and Python targets refuse `⇜` by name.

```faber locale=en
main {
    mut list<string> log ← []
    log.append("begin")
    log ⇜ "step"
    print log
}
```

A record is a labeled value. A bare `{ label = value }` with an inferred cell
is a `record<*>`; it prints without a type name. Record fields are read-only:
`r.x ← v` is `SEM020` `assignment_to_fixum_field`.

```faber locale=en
main {
    let _ point ← { x = 1.5, y = 2 }
    print point.y
    print point
}
```

A matrix element reads and writes by row and column: `m[[r, c]]` and
`m[[r, c]] ← v`, with literal or computed coordinates. In 1.18 this runs on
`faber run`; generated Rust does not compile it yet, and Swift and LLVM refuse
it by name.

```faber locale=en
main {
    mut matrix<f32, [2, 2]> m ← [[1.0, 2.0], [3.0, 4.0]] ↦ matrix<f32, [2, 2]>
    m[[1, 0]] ← 7.5
    print m[[1, 0]]
}
```

A range is a value of type `range<int>`. `for range` walks it.

```faber locale=en
main {
    let range<int> r ← 0 ‥ 3
    print r
    for range r let i {
        print i
    }
}
```

A stored range may carry a step; the step is part of the type.

```faber locale=en
main {
    let range<int, 2> evens ← 0 … 10 step 2
    print evens.length()
    print evens.contains(3)
}
```

This prints `6` and `false`.

Write `range`, not the Latin `intervallum`, and `sparse`, not `sparsa`, in an
English file (`PARSE040` `wrong_locale_type`).

Parent: https://faberlang.dev/agents/types.md
Next: https://faberlang.dev/agents/types/conversions.md
