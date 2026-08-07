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
the package store. `FABER_LIBRARY_HOME` is a resolver override for local
development when set.

Triga is not part of Norma. It is an optional dependency that packages opt
into when they need graphics or geometry work. The current package version is
0.2.0.

## Modules {#modules}

Each `triga:<stem>` import resolves to `src/<stem>.fab`. The layout follows
Norma's flat-leaf pattern; there is **no type re-export**, so consumers import
the leaf that owns the genus they use.

| Import | Owns |
|--------|------|
| `triga:math` | `Vector2`…`Vector4`, `Matrix3`/`Matrix4`, `Quaternion`, `Euler`, `Color`, `Box3`, `Sphere`, `Plane`, `Ray`, transform payload, face-code tables, camera helpers |
| `triga:graph` | `Object3D`, `Scene`, `PerspectiveCamera`, `OrthographicCamera`, `Light` family |
| `triga:material` | `Material` family, `Mesh`, `MeshGeometry`, `TextureDescriptor` |
| `triga:face` | `FaceQuad` + unit/colored quad builders |
| `triga:geometry` | `BufferGeometry`, `BufferAttribute`, vertex-layout reflection, draw batches |
| `triga:primitives` | Deterministic mesh generators (`plane_geometry`, `box_geometry`, …) |
| `triga:scene` | `SceneStore`, `SceneHandle`, node kinds, traversal, `visibilia` |
| `triga:resource` | `ResourceHandle` + lifecycle free functions |
| `triga:triga` | Facade / module map only (no genera) |

```faber mode=package
importa ex "triga:math" privata math
importa ex "triga:graph" privata graph
importa ex "triga:material" privata material
importa ex "triga:geometry" privata geometry
importa ex "triga:primitives" privata primitives
importa ex "triga:scene" privata scene
importa ex "triga:resource" privata resource
```

## API shape {#api-shape}

Public operations on Triga genera are **receiver methods** with an implicit
`ego` receiver. Free functions survive only as constructors (`vector3`,
`box3_ex_minimo_et_maximo`, `matrix4_conspectus`), pure scalar helpers, and
primitive generators.

Faber morphologia applies: **Imperativus** mutates a `varia` receiver in
place, while **Perfectum** returns a new value and leaves the receiver alone.

```faber mode=package
importa ex "triga:math" privata math

# Perfectum — returns a new Box3, receiver unchanged
fixum math.Box3 bounds ← math.Box3 { min = math.vector3(0.0, 0.0, 0.0), max = math.vector3(2.0, 2.0, 2.0) }
fixum math.Box3 expanded ← bounds.inflata(1.0)

# Imperativus — mutates the varia receiver in place
varia math.Box3 mutable ← math.Box3 { min = math.vector3(0.0, 0.0, 0.0), max = math.vector3(1.0, 1.0, 1.0) }
mutable.infla(2.0)
```

Vocabulary is technical Latin: carrier nouns stay English where the standard
identity is the point (`Vector3`, `Matrix4`, `Quaternion`, `Box3`, `Ray`,
`BufferGeometry`, `f32`, `WebGPU`), while operation stems are Latinised
(`normata` normalize, `productum` dot product, `transversum` cross product,
`insere` insert, `adiunge` attach, `cape` get, `inveni` find, `continet`
contains, `visibilia` visible). The material constructor is
`materia_ex_nomine(name)`, and `BufferGeometry` attributes carry
`float32_values()` payload projection for host upload.

## Design {#design}

- **Structure-of-arrays layout**: vertex attributes and matrix storage use
  flat `lista<f32>`, not interleaved arrays. This maps directly to WGSL
  storage buffers and GPU buffer uploads.
- **Composition over inheritance**: `PerspectiveCamera.base` contains an
  `Object3D` rather than using type inheritance; `MeshStandardMaterial.base`
  contains a `Material`.
- **Three.js field alignment**: field names use Faber's `snake_case`
  convention while the structural hierarchy mirrors three.js
  (`Object3D` → `Mesh` → `Scene`, `Material` → `MeshStandardMaterial`).
- **Module seams**: Norma-style flat leaves — `math` / `graph` / `material` /
  `face` / `geometry` / `primitives` / `scene` / `resource` — with nested
  package dirs only when a directory holds 2–3+ modules.

## Exempla {#exempla}

Instructional demos live under `triga/exempla/`: `triga-scene-store.fab`
(stable heterogeneous scene store with `insere` / `adiunge` / `cape` /
`visibilia`), `triga-transforms.fab` (Vector3 / Matrix4 transform chains),
`triga-geometry-attributes.fab`, `triga-basics.fab`, plus three Hello Voxel
fixtures that exercise the `@vertex` / `@fragment` shader-surface path end to
end.

## Browser demos {#demos}

Triga ships browser-rendered demo scenes that exercise the `triga:*` surface
end-to-end: Faber scene facts → `faber build --package .` browser product →
direct WebGPU.

| Demo | Where | What it pressures |
|------|-------|-------------------|
| `webgl-geometries` | `triga/corpus/` | Every `triga:primitives` generator (plane, box, circle, sphere, cylinder, cone, torus), per-mesh colors, `BufferGeometry` → interleaved host payload |
| `webgl-geometry-terrain` | `triga/corpus/` | Procedural mesh generation at scale (48² heightfield, ~4.6k triangles), value noise, central-difference normals, elevation color ramp |
| **Triga Budapest** | `examples/triga-budapest/` | Stylized Budapest Chain Bridge: Danube plane, bridge deck, portal towers, suspension chains, skyline blocks — scene facts, many meshes, camera projection, material intent by object color |
| **Triga Drift City** | `examples/triga-drift-city/` | Deterministic arcade-driving simulation: bounded city circuit, drift dynamics, collision response, chase camera, renderer-neutral Triga scene facts drawn by the WebGPU host |

Run the corpus demos with `cd triga/corpus && ./serve.sh` (builds every demo
and serves them at `http://127.0.0.1:8780/`). The Budapest and Drift City
apps live under `examples/` and serve locally via `./serve.sh` from each
directory. Each demo is a `browser-app` package whose `public/*.js` owns
WebGPU transport only — no simulation constants or draw policy.

The sibling `hosts/webgpu-browser` repository is the browser-first WebGPU
product boundary: it acquires the adapter/device, creates resources, encodes
commands, and reads results back, consuming compiled Faber WGSL and MIR
reflection metadata. Triga owns the source contracts; the host owns the
browser runtime.

## Status {#status}

| Layer | State |
|-------|-------|
| Math / transforms | Stable native Faber (`Vector*`, `Matrix4`, quaternions, …) |
| Scene store | Stable handles, graph edits, world transforms; exempla green |
| Buffer geometry | SoA attributes, draw batches, vertex-layout reflection |
| Primitive generators | Deterministic plane/box/sphere/… mesh builders |
| Host WebGPU path | Sibling `hosts/webgpu-browser` consumes compiled graphics artifacts; Triga owns source contracts, not the browser runtime |
