# Faber in a first session

This is the short path from an installed `faber` command to a checked program. The pages linked below are the reference: come back to them when you need a rule or a complete list of terms.

## 1. Make a package

Run `faber init salve-munde`, then open the two files it creates. A package has a manifest and an entry source file.

`src/main.fab`:

```faber locale=en
fn salve(string nomen) → string {
    const string msg ← "Salve, §!"(nomen)
    return msg
}

main {
    const string m ← salve("munde")
    print m
}
```

Run `faber check .` to parse and type-check the package. Run `faber run .` to see `Salve, munde!`.

The declaration puts each type before its name. `fn` introduces a function; `→` gives its return type; `const` binds an immutable value; and `←` assigns its initializer. The `main` block is the program entry point.

For a complete package, including its manifest, see https://faberlang.dev/agents/program.md.

## 2. Change one thing at a time

Add a function and call it from `main`: https://faberlang.dev/agents/functions.md.

Give a value a type and choose an appropriate collection: https://faberlang.dev/agents/types.md.

Branch and repeat with `if`, `for`, and `while`: https://faberlang.dev/agents/control.md.

Return or recover from an error: https://faberlang.dev/agents/errors.md.

After each change, run `faber check .`. The compiler's diagnostic tells you what to fix; see https://faberlang.dev/agents/check.md for a deliberately rejected program.

## 3. Grow beyond one file

Split a program into modules, then use a package manifest to describe its structure:

- https://faberlang.dev/agents/modules.md
- https://faberlang.dev/agents/packages.md

When you need a library, start with the supported imports: https://faberlang.dev/agents/libraries.md.

## 4. Pick the spelling you want

Faber source can use any reader locale supported by its keyword pack. Each file uses one pack. The English spellings are used throughout this tutorial and the agent-facing examples. See https://faberlang.dev/agents/locales.md for the locale table and rules.

## 5. Look up a form

The topic pages explain common patterns. For a complete, generated reference, open https://faberlang.dev/agents/reference/index.md. The grammar overview is at https://faberlang.dev/agents/grammar.md.
