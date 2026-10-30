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

`norma:db` writes to SQLite through `Connection`, `Transaction` and
`PreparedWrite`, on the MIR runner and generated Rust. Parameters are bound as a
`list<value>`. A transaction that is not committed rolls back when it leaves
scope. `copy` of a resource is `SEM066`. There is no typed row or cursor reading
yet.

```faber locale=en
import from "norma:db" db

main {
    do {
        let db.Connection connection ← db.open(":memory:")
        print connection.close() ⊥ false
    } catch fault {
        print fault.kind
    }
}
```

Fetch list: https://faberlang.dev/agents/index.md
