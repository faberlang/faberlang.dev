+++
title = "Imports"
section = "cheatsheet"
order = 38
sources = []
+++

The common sugar form is:

```text
importa ex "<source>" <name>
```

*Import this name from this source.* Imports do not re-export by default; use
`publica` when the imported name should be visible to consumers of your module.
The retired `privata` import marker is not valid.

## From the standard library {#stdlib}

Norma modules are named `norma:<module>`.

```faber locale=en
import from "norma:console" console

main {
    print "ready"
}
```

## From a local file {#local}

A relative path imports a sibling module. No extension.

```faber locale-tabs
importa ex "./auxilium" saluta

incipit {
    nota "ready"
}
```

## Importing a specific item {#items}

The name after the source is the item, not the module — so you import exactly
what you use.

```faber locale=en
import from "norma:text" text

main {
    print "ready"
}
```

## Aliasing {#aliasing}

`ut` renames on the way in.

```faber locale-tabs
importa ex "./auxilium" saluta ut greet

incipit {
    nota "ready"
}
```

Useful when two modules export the same name, or when the original reads
badly at the call site.

## Re-exporting {#publica}

`publica` imports *and* re-exports, so consumers of your module see the name
too. Imports without it remain private to the current module.

```faber locale=en
import from "norma:text" public text

main {
    print "ready"
}
```

Use `publica` only when you deliberately intend to widen your module's surface.

## The braced record form {#braced}

An import can also be written as a record. The field names are spelled by the
file's reader pack, so an English file writes `from`, `visibility`, `name` and
`as`, and a Latin file writes `ex`, `visibilitas`, `nomen` and `ut`.

```faber locale=en
import { from = "norma:text", visibility = public, name = text, as = t }
```

A field word from another locale is refused by name:
`import { ex = "norma:text" }` in an English file is `PARSE050
wrong_locale_import_field`.

## From the target language {#target-bound}

A target word before the specifier imports a module of the target language
itself, by its own name and verbatim. The program then belongs to that
target: `faber build -t python` emits `import math as m`, while every other
target, `faber run` and a plain `faber check` refuse it with
`SEM017 import_target_bound`.

```faber locale=en target=python
import python "math" m

main {
    print m.pi
}
```

A value from such a module flows into a scalar cell such as `f64` directly.
Storing it into a list, map or other structural cell needs an explicit `↦`;
without one it is `SEM010 import_conversion_required`.

```faber locale=en target=python
import python "math" m
import python "re" re

main {
    let f64 root ← m.sqrt(2.0)
    let list<string> words ← re.findall("[a-z]+", "a1b2") ↦ list<string>
    print root
    print words
}
```

## At a glance {#summary}

| Form | Effect |
|---|---|
| `importa ex "norma:console" console` | Standard library module |
| `importa ex "./auxilium" saluta` | Item from a sibling file |
| `importa ex "./auxilium" saluta ut greet` | …bound under a different name |
| `importa ex "norma:text" publica text` | Imported and re-exported |
| `importa python "math" m` (en `import python "math" m`) | Target-language module; Python builds only |

Related: [A program is a package](/language/behavior/packages.html) for how modules sit inside
a package · [Packages with Cista](/toolchain/packages.html) for dependency
resolution
