# Entry

`main` is the program entry. A command-line entry is `main args`. The plain
package entry is https://faberlang.dev/agents/program.md.

```faber locale=en
@ cli { name = "echo" }
@ description "Prints text"
@ operand { rest = true, type = string, binding = words }
main args argv {
    for from argv.words const word {
        print word
    }
}
```

Parent: https://faberlang.dev/agents/functions.md
