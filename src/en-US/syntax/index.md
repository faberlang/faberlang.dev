+++
title = "Syntax and semantics"
section = "syntax"
order = 0
sources = []
+++

Faber syntax is built on three principles: types before names, Latin
words for behaviour, and structural glyphs for value flow. Every
declaration reads as intent first, mechanism second.

## Data types {#types}

Type-first declarations, numeric widths, tensors, lists, and GPU core
types. [Read more →](/syntax/types.html)

## Variables {#variables}

Bindings use `←` for value flow. Mutability is explicit through `varia`.
[Read more →](/syntax/variables.html)

## Functions {#functions}

Functions declare parameter types before names. Return types follow the
arrow. [Read more →](/syntax/functions.html)

## Control flow {#control-flow}

`si`/`ceterum` for branching, `dum` for iteration, `perge`/`rumpe` for
loop control. [Read more →](/syntax/control-flow.html)

## Errors {#errors}

Errors are typed values, not exceptions. The `aut` type carries success
or failure. [Read more →](/syntax/errors.html)

## Generics {#generics}

Type parameters on functions and structures. Constraints through trait
bounds. [Read more →](/syntax/generics.html)

## Collections {#collections}

Lists (`lista`), maps, and tensors for structured data.
[Read more →](/syntax/collections.html)

## Strings {#strings}

The `textus` type, template literals, and string operations.
[Read more →](/syntax/strings.html)

## Conversion {#conversion}

The `conversio` system for explicit type conversions.
[Read more →](/syntax/conversion.html)

## Glyphs {#glyphs}

Structural glyph reference: `←`, `→`, `‥`, `≡`, `≢`, and more.
[Read more →](/syntax/glyphs.html)

## Nullability {#nullability}

Absence is typed. The `forsitan` type and nullable annotations.
[Read more →](/syntax/nullability.html)
