# Speculum document IR — HTML out of Faber

**Status:** draft revised after Head second reads (2026-07-17)  
**Repo:** `faberlang/faberlang.dev`  
**Scope:** Speculum site generator (`generator/`) — architecture + staged implementation  
**Related:** `CONTENT-PLAN.md`, `generator/src/html.fab`, `generator/src/document_ir.fab`, `generator/src/markdown.fab`, `radix/EBNF.md` (annotations + discretio), operator discussion Mind session 2026-07-17  
**Memo:** `eead6a2d` (fleet)  
**Head reviews absorbed:** head-cto `6bde87ac` / `c40511c5`; head-cxo `de48f431`; hand-4 Stage A land `46f719a`

---

## 1. Problem

Speculum converts Markdown and corpus records into static HTML for
https://faberlang.dev. Content sources are already clean (Markdown under
`src/en-US/`, machine files under `static/`). The **generator** embeds HTML as
string soup inside Faber:

| Module | Role | Rough markup load |
| --- | --- | --- |
| `html.fab` | Document chrome (head, renderbar, sidebar, footer, agent notice) | ~179 tag-like tokens |
| `markdown.fab` | MD → HTML body | ~94 tags (`p`, `h*`, `ul`, `table`, `pre`, …) |
| `corpus.fab` | Alias redirect full mini-document | ~20 tags (second DOCTYPE shell) |
| `span.fab` | `<code class="kw\|typ">` | small |

CSS is already out of Faber (`generator/www/speculum.css` only; generator must
not write CSS — CONTENT-PLAN). **HTML never got the same rule.**

Consequences:

1. Layout and language logic are mixed; chrome churn rewrites Faber.
2. Guillemet mega-templates with many `§` holes are hard to review and escape.
3. Agents editing Speculum must understand HTML class names and DOM structure.
4. Versioned strings (release download URLs, nav) live inside HTML blobs —
   same class of drift as hardcoding `1.1.1` across static files.

---

## 2. Goals

1. **No raw HTML markup in Speculum `.fab` sources** (lint/gate; allowlist none
   or a single serializer module temporarily).
2. **Document IR is Faber genera** — HIR-shaped values the compiler already
   understands (parse, typecheck, test).
3. **HTML is a rendering** of that IR — same “HIR is truth, surfaces are
   renderings” slogan as reader locale and Rust codegen.
4. **Dogfood Faber** — prefer language + Radix over foreign template engines
   *as the default end state*.
5. **Ship in stages** — chrome first; Markdown body second; no big-bang rewrite
   that blanks the live site.

### Non-goals (this design)

- Compiler-owned `@ web` / route / controller annotation families (explicitly
  out of `radix/EBNF.md` policy).
- Replacing Markdown authoring for prose pages.
- Multilingual Stage 6 / reader-locale UI chrome (orthogonal).
- `faber emit -t html` as a required first ship (optional later).
- Perfect 1:1 HTML5 coverage (void elements, raw HTML passthrough, SVG trees).

---

## 3. Vocabulary (critical)

English “annotation” collides with two different things:

| Concept | HTML | Faber |
| --- | --- | --- |
| **Property on a node** | `class`, `href`, `id` on an element | **Genus fields** or `Attr { nomen, valor }` on a value |
| **Declaration metadata** | (no direct equivalent) | **`@` annotations** → `HirAnnotation` on the next declaration |

**Rule:** HTML attributes are **properties of the element value**, not Faber
`@` applications on every node.

Faber `@ annotatio` contracts remain useful for **page / package metadata**
(like `@ cli` on an entry), not for DOM attribute soup.

---

## 4. Target architecture

```text
Markdown / frontmatter / corpus bundle
        │
        ▼
   Pagina (today)  ──stage B──►  Document IR (genera)
        │                              │
        │                     @ PaginaMeta (optional stage C)
        │                              │
        ▼                              ▼
   [legacy string path]          html(Document) → textus
        │                              │
        └──────────────┬───────────────┘
                       ▼
                     dist/*.html
```

### 4.1 Document IR (genera / discretio)

**Target (honest language shape — head-cto C1):** Faber already has ergonomic
tagged unions (`discretio` + `finge` / `discerne`; EBNF + corpus +
`examples/arena-handle`). The load-bearing IR type is **not** an open question:

```text
genus Attr {
    textus nomen      # "class", "href", "aria-label", …
    textus valor
}

discretio Node {
    Element { textus tag, lista<Attr> attrs, lista<Node> children },
    Text    { textus valor },           # escaped on serialize
    Raw     { textus valor },           # serializer boundary only; not chrome builders
    Frag    { lista<Node> children },
}

genus Document {
    Node root
    # page meta (locale, titulus, section, stylesheet, sources) may live on
    # Document fields or stay as parameters to shell builders — prefer
    # fields when they stop being thread-through noise.
}
```

**As-shipped Stage A land (hand-4 `46f719a` — transitional, not target):**

```text
genus Element {
    textus tag_name
    lista<Attr> attrs
    lista<Element> children
    textus content          # text when tag_name = ""  (magic convention)
    bivalens vacuum_tag     # void elements
}
genus Document { Element root }
```

This flat genus is simpler short-term (head-cxo C1 preference) but **encodes
sum cases as magic strings and inconsistent flags**. It is **debt**, not the
architecture target. **Stage A.1** must either migrate to `discretio Node` or
record an explicit counted debt ratchet that expires before Stage B (markdown
IR). Do not leave the design doc claiming sum types are unavailable.

**Attributes:**

- Open map via `lista<Attr>` (matches real HTML).
- Optional later: closed genera per tag as sugar over the same IR.

**Not IR:** CSS rules, full browser DOM APIs, reactive components.

### 4.2 Page metadata (`@ annotatio`)

Optional stage C — aligns frontmatter with language contracts:

```text
@ annotatio { target = functio }
genus PaginaMeta {
    textus section = ""
    textus titulus
    numerus order = 0
}

@ PaginaMeta { section = "syntax", titulus = "Types", order = 1 }
functio pagina_types() → Document { … }
```

Constraints from current language (EBNF):

- `@ annotatio` marks a **genus** as a contract schema.
- Applications: `@ Name { field = constant }`.
- v1 attachment target is primarily **`functio`**.
- Payload scalars: `textus`, `numerus`, `fractus`, `bivalens` (optional).

Until stage C, keep `+++` TOML frontmatter → `Pagina` fields; IR stage does not
block on annotation contracts.

### 4.3 Serialization

**Stage A–B (required):** pure Faber function

```text
functio html(Document doc) → textus
functio html_node(Node n) → textus
```

- **Escape text nodes and attribute values** (`&`, `<`, `>`, `"` at minimum).
  Centralize in the serializer only. Stage A done-when **must** include this
  (head-cto G1): either implement escape or an explicit, dated debt note —
  zero-escape ship is not “Stage A complete.”
- Void elements (`meta`, `link`, `br`, …): closed set in serializer; no end tags.
- Single module allowed to know tag spellings as **data** (`"div"`, `"a"`),
  not page layout.
- `Raw` is only for temporary MD-body HTML wrapping; chrome builders must not
  emit `Raw`.

**Stage D (optional):** `faber emit -t html` or JSON dump of IR + external
tool — only if multi-tool consumers appear. Not required to delete string soup.

### 4.4 Chrome builders

Replace guillemet HTML in `html.fab` with functions that return `Node` /
`Document`:

```text
functio shell(Pagina pag, Node main) → Document
functio sidebar(textus active_section) → Node
functio renderbar(textus locale) → Node
functio agent_notice() → Node
```

Nav links, release download URLs, machine-doc paths become **data**
(`lista` of `{ label, href }`) filled into IR — same place we should later
inject version placeholders.

### 4.5 Markdown path

**Stage B:** `markdown.fab` emits `Node` (or `lista<Node>` body), not HTML
strings. Headings, lists, tables, fences map to element constructors.

**Stage A:** may leave MD→HTML string temporarily if chrome-only IR is the
first land; body HTML then wraps as a single `Raw` node **only inside the
serializer boundary** — prefer not to expose `Raw` to chrome builders.

### 4.6 Corpus alias pages

Today `corpus.fab` builds a second full HTML document for redirects.
Target: same `Document` shell + small main node (`meta refresh` + link),
one chrome path.

---

## 5. Invariants

1. **IR is authority for structure.** HTML string is never edited as source of
   truth for chrome.
2. **No raw HTML in `.fab` outside the serializer module** (ratchet: start with
   chrome builders; expand gate).
3. **Attributes are fields/Attr pairs**, never Faber `@` applications on each
   node instance.
4. **`@ annotatio` is for declaration contracts** (page meta, later packages),
   not DOM.
5. **One stylesheet** remains `www/speculum.css`; generator still cannot write
   CSS.
6. **Live site must keep building** via `generator/scripts/build-site.sh`;
   `dist/` deploy pipeline unchanged at the GitHub Pages boundary.
7. **No compiler `@ web` family** without a separate language design campaign.

---

## 6. Migration stages

| Stage | Deliverable | Done when |
| --- | --- | --- |
| **A** | Document IR + `html()` + chrome as IR | Chrome guillemets gone; site builds; nav/download intact; **escape implemented or explicit debt**; IR types documented |
| **A.1** | Honesty ratchet (Heads) | `discretio Node` (or debt budget with expiry); centralized escape; void-element set explicit; optional `dist/` smoke baseline |
| **B** | Markdown → Node IR | `markdown.fab` emits Nodes; no HTML string emitters outside serializer |
| **C** | Optional `@ PaginaMeta` (or keep TOML) | Frontmatter maps to typed meta; documented choice |
| **D** | Optional emit backend / JSON IR dump | Only if a second consumer exists |
| **Gate** | Lint/test fails on HTML tags in disallowed modules | Local validate script first; CI when available |

**Landed:** hand-4 `40d7f985` / commit `46f719a` — Stage A chrome IR (flat Element).  
**A.1 closed:** hand-4 `798d087b` — `document_ir.fab` now models `discretio Node { Element, Text, Raw, Frag }`; serializer owns text/attribute escaping and the explicit HTML void-element set; `build-site.sh` regenerated `dist/` with smoke checks for `/`, `/start/install.html`, and 1.1.1 links.

**Next:** Stage B markdown-to-Node IR.

**Rollback:** keep previous `dist/` commit; generator is rebuilt offline (no
Faber in CI today).

---

## 7. Alternatives considered

### 7.1 External HTML templates (`.html` + substitute)

- **Pros:** layout in layout files; simple shell fill.
- **Cons:** second language; less dogfood; easy to reintroduce dual sources.
- **Verdict:** acceptable emergency escape, **not** default end state for this
  project.

### 7.2 HTML as nested `@` annotations

- **Pros:** feels “Faber-native” if you equate attribute ≈ annotation.
- **Cons:** attachment model is declaration metadata (`functio` v1), flat
  records, not recursive mixed content; fights EBNF and compiler policy.
- **Verdict:** **reject** for DOM trees. Use genera for trees; `@ annotatio`
  only for page-level contracts.

### 7.3 Keep string HTML, extract constants

- **Pros:** small diff.
- **Cons:** still HTML-in-language; does not fix review or lint story.
- **Verdict:** reject as architecture.

### 7.4 Closed genus per HTML tag (`Div`, `A`, `Nav`, …)

- **Pros:** stronger types; good autocomplete for a fixed set.
- **Cons:** large surface; HTML is open-ended for attrs.
- **Verdict:** optional sugar later over open `Element` + `Attr`.

---

## 8. Risks and open questions

| Risk / question | Notes | Preference |
| --- | --- | --- |
| Large nested genus literals | Ergonomics / compiler limits | Prefer builder functions over giant literals |
| Sum types for `Node` | Language support maturity | Start with tagged genus or separate constructors |
| Escaping bugs | XSS not a threat for static docs, correctness is | Centralize escape in serializer only |
| Attribute ordering / class merge | Stable tests? | Deterministic sort optional |
| Frontmatter vs `@ PaginaMeta` | Dual author surfaces | Keep TOML until Stage C earns contracts |
| Version strings in chrome | Still hardcoded in IR builders | Follow-up: single version source (CXO earlier note) |
| PKG001 / package I/O | Generator still shell-bridged for FS | Unchanged |

---

## 9. Success metrics

1. Zero (or serializer-only) HTML angle-bracket literals in chrome modules.
2. `build-site.sh` green; Pages deploy still from `dist/`.
3. Spot-check: `/`, `/start/install.html`, `/corpus/functio.html` structure and
   critical links.
4. New chrome work is expressed as IR builders + CSS classes in
   `speculum.css` only.
5. Heads agree this doc is the architecture target (or file explicit deltas).

---

## 10. Review asks (Heads)

Please second-read this draft and reply with:

1. **Corrections** — factual errors about Faber annotations, Speculum, or
   deploy constraints.
2. **Gaps** — missing stages, invariants, or failure modes.
3. **Simplifications** — what to cut from Stage A so it ships.
4. **Nacks** — anything that should be rejected before hand-4 implements.

Suggested lenses:

| Role | Lens |
| --- | --- |
| **head-cxo** | Purity / clean break — IR vs templates; attribute vs `@`; stage boundaries |
| **head-cto** | Correctness / honesty — can we ship Stage A without lying about capability; serializer risks; test bar |

---

## 11. References

- Live chrome: `generator/src/html.fab`
- MD emitter: `generator/src/markdown.fab`
- Types today: `generator/src/types.fab` (`Pagina`, `HtmlPagina`)
- Content architecture: `CONTENT-PLAN.md`
- Annotation contracts: `radix/EBNF.md` (Annotation contracts section)
- Annotation sugar: `radix/docs/design/annotation-sugar.md`
- Fleet memos: `eead6a2d` (direction), `20a125fb` (agent-rich site), `23bff4d0` (install honesty)

---

## 12. Head second-read summary (2026-07-17)

| Head | Verdict | Must absorb |
| --- | --- | --- |
| **head-cto** | Architecture OK; **not** Stage-A-done | **C1** use `discretio Node` (language has sums); **G1** escape in done-when; void set; dist baseline; nack genus-as-target without debt ratchet |
| **head-cxo** | Approve with corrections | Prefer documenting as-shipped flat Element for Stage A simplicity; escape honesty; lint gate; document `Document { root }` shape |
| **Mind resolution** | Target = `discretio Node`; flat Element = transitional debt; Stage **A.1** required before Stage B |

## 13. Revision history

| Date | Change |
| --- | --- |
| 2026-07-17 | Initial draft for Head review (Mind) |
| 2026-07-17 | Revise after CTO/CXO second reads; Stage A.1 honesty ratchet |
