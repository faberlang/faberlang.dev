+++
title = "Entry points"
section = "cheatsheet"
order = 31
sources = []
+++

Where a Faber program starts.

## The ordinary entry point {#incipit}

`incipit` — "it begins". No parameters, no return type.

```faber
incipit {
    nota "Salve, munde!"
}
```

## Async entry point {#async}

`incipiet` — "it will begin". Use it when the program awaits anything.

```faber
incipiet {
    nota "async ready"
}
```

The two are alternatives, not a pair: a program declares one or the other.

## Command-line arguments {#arguments}

`argumenta` binds the parsed argument object.

```faber
incipit argumenta args {
    nota "started"
}
```

## Naming the command {#cli}

The `@ cli` annotation names the binary the package produces.

```faber
@ cli "salve"
incipit argumenta args {
    nota "started"
}
```

## Declaring options {#options}

`@ optio` declares one command-line option. Repeat it for each. The binding
name comes first, then keyword-introduced fields — no braces, no commas.

```faber
@ cli "salve"
@ optio nomen brevis "n" longum "nomen" typus textus descriptio "who to greet"
@ optio quotiens longum "quotiens" typus numerus descriptio "how many times"
incipit argumenta args {
    nota "started"
}
```

| Field | Purpose |
|---|---|
| *(first word)* | The name the parsed value binds to |
| `brevis` | Short flag, as in `-n` |
| `longum` | Long flag, as in `--nomen` |
| `typus` | The option's type |
| `descriptio` | Help text |
| `ubique` | Accept the option on every subcommand |

An option can declare `longum` without `brevis`, as `quotiens` does above.

Related: [Commands](/cheatsheet/commands.html) for running what you build, and
[Your first package](/start/projects.html) for the surrounding package layout.
