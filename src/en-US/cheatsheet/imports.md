+++
title = "Imports"
section = "cheatsheet"
order = 38
sources = []
+++

One shape covers every import:

```text
importa ex "<source>" privata <name>
```

*Import, from this source, privately, this name.* `privata` and `publica`
control whether the imported name is re-exported from your module.

## From the standard library {#stdlib}

Norma modules are named `norma:<module>`.

```faber
importa ex "norma:consolum" privata consolum

incipit {
    nota "ready"
}
```

## From a local file {#local}

A relative path imports a sibling module. No extension.

```faber
importa ex "./auxilium" privata saluta

incipit {
    nota "ready"
}
```

## Importing a specific item {#items}

The name after `privata` is the item, not the module — so you import exactly
what you use.

```faber
importa ex "norma:textus" privata textus

incipit {
    nota "ready"
}
```

## Aliasing {#aliasing}

`ut` renames on the way in.

```faber
importa ex "./auxilium" privata saluta ut greet

incipit {
    nota "ready"
}
```

Useful when two modules export the same name, or when the original reads
badly at the call site.

## Re-exporting {#publica}

`publica` imports *and* re-exports, so consumers of your module see the name
too.

```faber
importa ex "norma:textus" publica textus

incipit {
    nota "ready"
}
```

Use `privata` unless you deliberately intend to widen your module's surface.
`privata` is the one you want almost always.

## At a glance {#summary}

| Form | Effect |
|---|---|
| `importa ex "norma:consolum" privata consolum` | Standard library module |
| `importa ex "./auxilium" privata saluta` | Item from a sibling file |
| `importa ex "./auxilium" privata saluta ut greet` | …bound under a different name |
| `importa ex "norma:textus" publica textus` | Imported and re-exported |

Related: [Your first package](/start/projects.html) for how modules sit inside
a package · [Packages with Cista](/toolchain/packages.html) for dependency
resolution
