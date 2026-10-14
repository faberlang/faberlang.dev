+++
title = "Triga — graphics and geometry"
section = "libraries"
order = 2
sources = [
  "sibling triga/ repository",
  "triga/docs/module-map.md",
  "triga/docs/api-shape-policy.md",
  "triga/corpus/README.md",
  "examples/triga-budapest/README.md",
  "examples/triga-drift-city/README.md",
]
+++

Triga is Faber's native graphics and geometry library: the typed contract
between compiled Faber output and a GPU runtime host. It provides math,
scene-graph, material, geometry, primitive, and resource types as public
`triga:*` modules.

Shapes model the [three.js](https://threejs.org/) abstractions for LLM
familiarity and migration ease, but Triga is **not** a binding to three.js —
these are native Faber types that define the same structural domain. In normal
projects, declare Triga as a Cista package dependency in `faber.toml`; Cista
records the resolved source in `faber.lock` and the compiler resolves it from
the package store. For local development, point the compiler at a checkout
with `--library-home <DIR>` or `[paths] library_home` in `faber.toml`; without
either, only the Norma library embedded in the binary is available.

Triga is not part of Norma. It is an optional dependency that packages opt
into when they need graphics or geometry work.

## Modules {#modules}

Each `triga:<stem>` import resolves to `src/<stem>.fab`, and a nested
`triga:<pkg>/<leaf>` import resolves to `src/<pkg>/<leaf>.fab`. The layout
follows Norma's flat-leaf pattern; there is **no type re-export**, so consumers
import the leaf that owns the class they use. The top-level `graph`,
`geometry`, `lighting`, `material`, `primitives` and `renderable` modules are
facades that point at their leaves.

| Import | Owns |
|--------|------|
| `triga:math` | `Box<N>`, `Quaternion`, `Euler`, `Color`, `Sphere`, `Plane`, `Ray`, transform payload, face-code tables, vector and matrix helpers over the language's `vector<f32, N>` and `matrix<f32, [R, C]>` |
| `triga:graph/object` | `Object`, `Scene` |
| `triga:graph/camera` | `PerspectiveCamera`, `OrthographicCamera`, projection facts |
| `triga:lighting/light` | `Light`, `AmbientLight`, `DirectionalLight`, `PointLight` |
| `triga:material/base` | `Material`, `TextureDescriptor`, pipeline facts |
| `triga:material/basic`, `lit`, `standard` | `UnlitMaterial`, `PhongMaterial`, `StandardMaterial` |
| `triga:renderable/mesh` | `Mesh`: an `Object`, a geometry and an optional material |
| `triga:face` | `FaceQuad` + unit/colored quad builders |
| `triga:geometry/data` | `Geometry`, `PrimitiveTopology`, `ColoredQuadMesh` |
| `triga:geometry/attribute`, `layout`, `bounds`, `batch` | Vertex attributes, vertex layout, bounding volumes, draw batches |
| `triga:primitives/basic` | Deterministic mesh generators (`plane`, `box`, `sphere`, `cylinder`, `cone`, `torus`, …) |
| `triga:scene` | `SceneStore`, `SceneHandle`, node kinds, traversal, visibility queries |
| `triga:resource` | `ResourceHandle` + lifecycle operations |
| `triga:shader` | Opaque `Texture2D` and `Sampler` types and their bound functions |
| `triga:triga` | Facade / module map only (no classes) |

```faber mode=package
importa ex "triga:math" math
importa ex "triga:geometry/data" data
importa ex "triga:primitives/basic" basic
importa ex "triga:lighting/light" light
importa ex "triga:material/base" base
importa ex "triga:resource" resource
```

## API shape {#api-shape}

Public operations on Triga's own classes are **receiver methods** with an
implicit `self` receiver. Free functions cover constructors (`quaternion`,
`box_from_min_max`, `matrix_perspective`), pure scalar helpers, primitive
generators, and graphics-domain work on the language's own `vector` and
`matrix` types, which cannot grow receivers.

The math carriers are the language types `vector<f32, N>` and
`matrix<f32, [R, C]>`; Triga has no `Vector3` or `Matrix4` class. Faber
morphologia governs receiver posture: the scene store is mutated in place on a
`var` receiver, while math values return a new value and leave the receiver
alone.

```faber mode=package
importa ex "triga:math" math

functio demo() → math.Quaternion {
    # Free function: a constructor, no receiver exists yet
    fixum vector<f32, 3> lo ← [0.0, 0.0, 0.0] ↦ vector<f32, 3>
    fixum vector<f32, 3> hi ← [2.0, 2.0, 2.0] ↦ vector<f32, 3>
    fixum math.Box<3> ∪ nihil bounds ← math.box_from_min_max(lo, hi)

    # Receiver method: returns a new Quaternion, receiver unchanged
    fixum math.Quaternion turn ← math.quaternion(0.0, 0.0, 0.0, 2.0)
    redde turn.normalized()
}
```

Names are English: carrier nouns (`Quaternion`, `Box`, `Object`, `Geometry`,
`f32`, `WebGPU`) and operation methods (`insert`, `attach`, `take`, `find`,
`contains`, `set_visible`). The material constructor is
`material_from_name(name)`, and `Attribute` values carry a
`float32_values()` payload projection for host upload.

## Design {#design}

- **Structure-of-arrays layout**: vertex attributes use flat `lista<f32>`
  payloads, not interleaved arrays. This maps directly to WGSL storage buffers
  and GPU buffer uploads.
- **Composition over inheritance**: `PerspectiveCamera.base` contains an
  `Object` rather than using type inheritance; `StandardMaterial.base`
  contains a `Material`; `Mesh.base` contains an `Object`.
- **Three.js field alignment**: field names use Faber's `snake_case`
  convention while the structural hierarchy follows three.js
  (`Object` → `Mesh`, `Material` → `StandardMaterial`).
- **Module seams**: Norma-style flat leaves — `math`, `face`, `scene`,
  `resource`, `shader` — with nested package dirs (`graph/`, `geometry/`,
  `lighting/`, `material/`, `primitives/`, `renderable/`) where a directory
  holds several modules.

## Exempla {#exempla}

Instructional demos live under `triga/exempla/`: `triga-scene-store.fab`
(stable heterogeneous scene store with `insert` / `attach` / `take` /
visibility queries), `triga-transforms.fab` (vector / matrix transform chains),
`triga-geometry-attributes.fab`, `triga-basics.fab`, plus three Hello Voxel
fixtures that exercise the `@vertex` / `@fragment` shader-surface path end to
end.

## Browser demos {#demos}

Triga ships browser-rendered demo scenes that exercise the `triga:*` surface
end-to-end: Faber scene facts → `faber build --package .` browser product →
direct WebGPU.

| Demo | Where | What it pressures |
|------|-------|-------------------|
| `webgl-geometries` | `triga/corpus/` | Every `triga:primitives` generator (plane, box, circle, sphere, cylinder, cone, torus), per-mesh colors, `Geometry` → interleaved host payload |
| `webgl-geometry-terrain` | `triga/corpus/` | Procedural mesh generation at scale (48² heightfield, ~4.6k triangles), value noise, central-difference normals, elevation color ramp |
| `webgl-animation-orbit`, `webgl-animation-water`, `webgl-animation-terrain` | `triga/corpus/` | Animated scenes: delta-driven frame updates, camera travel, shader-driven wave displacement, animated heightmap terrain |
| **Triga Budapest** | `examples/triga-budapest/` | Stylized Budapest Chain Bridge: Danube plane, bridge deck, portal towers, suspension chains, skyline blocks — scene facts, many meshes, camera projection, material intent by object color |
| **Triga Drift City** | `examples/triga-drift-city/` | Deterministic arcade-driving simulation: bounded city circuit, drift dynamics, collision response, chase camera, renderer-neutral Triga scene facts drawn by the WebGPU host |

Run the corpus demos with `cd triga/corpus && ./serve.sh` (builds every demo
and serves them at `http://127.0.0.1:8780/`). The Budapest and Drift City
apps live under `examples/` and serve locally via `./serve.sh` from each
directory. Each demo is a `browser-app` package whose `public/*.js` owns
WebGPU transport only — no simulation constants or draw policy.

Triga owns the source contracts. Each demo's `public/` JavaScript is the
browser transport: it acquires the WebGPU adapter and device, creates
resources, and encodes commands from compiled Faber WGSL and reflection
metadata. The browser seam for the DOM and Canvas2D is [Tela](/libraries/tela.html)
(`tela:dom`, `tela:canvas2d`).

## Status {#status}

| Layer | State |
|-------|-------|
| Math / transforms | Native Faber (`vector<f32, N>`, `matrix<f32, [R, C]>`, quaternions, …) |
| Scene store | Handles, graph edits, world transforms |
| Buffer geometry | SoA attributes, draw batches, vertex-layout reflection |
| Primitive generators | Deterministic plane/box/sphere/… mesh builders |
| Browser WebGPU path | The demos' own `public/` JavaScript consumes compiled graphics artifacts; Triga owns source contracts, not the browser runtime |
