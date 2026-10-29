# Entry

`main` is the program entry. A command-line entry is `main args`. The plain
package entry is https://faberlang.dev/agents/program.md.

```faber locale=en
@ cli { name = "echo" }
@ description "Prints text"
@ operand { rest = true, type = string, binding = words }
main args argv {
    for from argv.words let word {
        print word
    }
}
```

`exit N` after `main` sets the exit code. The body runs first and keeps its
output; `exit 3` does not stop it early. `faber run` ends with that code, and a
program built for any target that runs programs (runner, Rust, Go, TypeScript,
Swift, Python, LLVM, Cranelift) ends with it too. A plain `main` ends with `0`.

```faber locale=en
main exit 2 {
    print "done"
}
```

Parent: https://faberlang.dev/agents/functions.md
