# cli

CLI root with options, operands, subcommands, and module mounts.

**Term** `cli` · **Section** ANNOTATIONS

## Syntax

```
@ cli <name>
```

## What this teaches

- Full CLI framework — `@ cli`, `@ versio`, `@ description`, `@ option`, `@ operand`, `@ command`, and `@ alias` compose a complete CLI application definition
- Subcommands — `@ command "greet"` declares a subcommand with its own options and operands
- Module mounting — `@ imperia` imports command modules from packages

## Common mistakes

- attaching `@ cli` to a `fn` instead of an `main` (SEM009), or reusing duplicate CLI flags or binding names within the same CLI surface

## Grammar

```
cliDecl :← '@' 'cli' stringLit
incipit argumenta args { ... }
```

## Expected output

```
Requires CLI flags/args at run time; no fixed stdout contract.
```

## Backend

```
Rust runtime whitelist (missing operand 'nomen'); Go compile whitelist.
Cross-ref optio/, operandus/, descriptio/, ubique/, argumenta/ keyword dirs.
```

## Example

```fab
@ cli "exemplum"
@ versio "0.1.0"
@ description "Faber CLI framework smoke exemplum"
@ option verbose short "v" long "verbose" type bool global description "Enable verbose output"
main args args {
}

@ command "greet"
@ alias "g"
@ description "Greet by name"
@ operand string nomen description "Name to greet"
fn greet() args args → void {
    if args.verbose {
        print "verbose"
    }
    print "Salve, §!"(args.nomen)
}

@ command "version"
@ alias "v"
fn version() → void {
    print "exemplum v0.1.0"
}
```

See also: [`command`](command.md), [`imperia`](imperia.md), [`option`](option.md), [`operand`](operand.md), [`args`](args.md), [`description`](description.md), [`global`](global.md), [`versio`](versio.md), [`alias`](alias.md).

Fetch list: https://faberlang.dev/agents/index.md
