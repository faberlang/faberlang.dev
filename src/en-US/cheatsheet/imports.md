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

```faber
importa ex "norma:consolum" consolum

incipit {
    nota "ready"
}
```

## From a local file {#local}

A relative path imports a sibling module. No extension.

```faber
importa ex "./auxilium" saluta

incipit {
    nota "ready"
}
```

## Importing a specific item {#items}

The name after the source is the item, not the module — so you import exactly
what you use.

```faber
importa ex "norma:textus" textus

incipit {
    nota "ready"
}
```

## Aliasing {#aliasing}

`ut` renames on the way in.

```faber
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

```faber
importa ex "norma:textus" publica textus

incipit {
    nota "ready"
}
```

Use `publica` only when you deliberately intend to widen your module's surface.

## At a glance {#summary}

| Form | Effect |
|---|---|
| `importa ex "norma:consolum" consolum` | Standard library module |
| `importa ex "./auxilium" saluta` | Item from a sibling file |
| `importa ex "./auxilium" saluta ut greet` | …bound under a different name |
| `importa ex "norma:textus" publica textus` | Imported and re-exported |

Related: [Your first package](/start/projects.html) for how modules sit inside
a package · [Packages with Cista](/toolchain/packages.html) for dependency
resolution
