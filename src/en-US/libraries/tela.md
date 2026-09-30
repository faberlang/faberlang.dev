+++
title = "Tela — views and the browser seam"
section = "libraries"
order = 4
sources = [
  "sibling tela/ repository",
  "tela/AGENTS.md",
  "tela/faber.toml",
  "tela/src/tela.fab",
  "tela/src/validate.fab",
  "tela/src/dom.fab",
  "tela/src/browser.fab",
  "tela/src/canvas2d.fab",
]
+++

Tela is Faber's view library: typed HTML and SVG view values, a serializer that
turns them into markup, and the DOM and Canvas2D contracts that let a Faber
program talk to a browser. It is imported as `tela:*`. The name is the Latin
for *web, fabric*.

The idea is that a view is data, not a string. You build a tree of typed
values, Tela checks the tree, and only a valid tree becomes markup. Nothing is
concatenated by hand, so the usual ways of producing broken or unsafe HTML are
not available on the ordinary path.

The current package version is 0.0.0. Read the [status](#status) section before
planning work on it — it is early, and the protocol and the static renderer
are the part that works today.

## A first view {#first}

Build a value, serialize it. The text contains a bare `&`; Tela escapes it.

```faber mode=package
importa ex "tela:tela" tela

incipit {
    fixum tela.View greeting ← tela.element_view(tela.html_space(), "p", [tela.text_view("Fish & chips")])
    nota tela.html_view(greeting) vel "invalid"
}
```

This prints `<p>Fish &amp; chips</p>`. `html_view` returns text or null: if
any check on the tree fails, it returns null and emits nothing — never
partial markup.

## Design {#design}

- **A typed tree.** A `View` is one of three things: an element (tag, space,
  attributes, properties, children), a text node, or a fragment. There is no
  raw-markup variant in the ordinary path, so there is no way to smuggle
  unescaped markup in as a value.
- **One escape path.** Text and attribute values go through the same
  `escape` function. The set of escaped characters differs between text and
  attributes, but no serializer path concatenates an unescaped value.
- **Fail closed.** Before any markup is emitted the serializer checks the whole
  tree: tag and attribute names, the HTML or SVG namespace, and void-element
  structure. A failed check means no output at all.
- **Identity is explicit.** An element may carry a typed `Identity`, which the
  serializer writes as a `data-tela` attribute through the same escape path.
  Identity is never derived from position.
- **Deterministic by design.** The serializer is written so that the same tree
  gives the same bytes.

## Modules {#modules}

Each `tela:<stem>` import resolves to `src/<stem>.fab`. As with the other
libraries, import the leaf that owns what you use.

| Import | Owns |
|--------|------|
| `tela:tela` | The kernel: the `View` union, constructors, the HTML and CSS serializers, `escape`, themes and tokens |
| `tela:validate` | The lexical, namespace, and void-element checks the serializer runs first |
| `tela:reference` | A catalog of reference components built from the kernel: layout (stack, grid, prose), typography, and more |
| `tela:browser` | The mount, replace, and dispose lifecycle, and hydration of server-rendered markup |
| `tela:dom` | The DOM contract: elements, events, and the state objects for pointer, keyboard, focus, and resize |
| `tela:canvas2d` | The Canvas2D drawing contract: a context over an element, with transforms, rectangles, and styles |
| `tela:web` | The `WebController` annotation |

The kernel depends on nothing else: no Norma, no Triga, no generated runtime.

## Targets {#targets}

Tela's manifest lists two targets, `rust` and `ts`, and the DOM and Canvas2D
modules bind to a TypeScript host runtime through a bindings file. The
TypeScript route is the one the library was built around; the Rust route is
listed but does not build yet.

## Status {#status}

As of 2026-09-30:

| Layer | State |
|-------|-------|
| Library source | `faber check` passes on the package |
| View protocol and serializer | The example above runs and prints the expected markup |
| Validation | Fail-closed checks run before any emission |
| Reference components | A catalog exists; it is a reference set, not a finished design system |
| TypeScript output | Emission exists, but the repository's own TypeScript type check of the emitted code currently reports errors |
| Rust output | Not working: building the library for Rust currently fails to compile |
| Package assembly | Per-file emission only; assembling an installable package is not built yet |
| Proof suite | The repository's proof scripts are not all green today: several proof packages no longer check, and the determinism check fails to compile |
| Real browser | Mount and update behavior is exercised against a fake DOM written in Faber; there is no in-tree run in a real browser |
| Async | Not supported yet in handlers |

Use Tela to see how a typed view protocol looks in Faber, and to build static
markup with checked output. Do not plan on it as a finished UI framework.

Source: [github.com/faberlang/tela](https://github.com/faberlang/tela).
