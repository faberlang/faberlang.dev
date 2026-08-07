+++
title = "Examples"
section = "examples"
order = 5
sources = []
+++

Real Faber packages, with their source on this site. Not snippets, and not a list of links asking you to go read someone else's repository.

| Project | What it is |
|---|---|
| [device-summa](/examples/device-summa.html) | A GPU device package: one compute kernel, run on real Metal or CUDA. |
| [gpu-workload — MLP forward](/examples/mlp-forward.html) | A neural-network forward pass as a device workload. |
| [coreutils — cat](/examples/cat.html) | The Unix `cat` utility, reimplemented in Faber with parity tests. |
| [AI Workbench](/examples/faber-ai.html) | A multi-command CLI for local model inventory, embeddings, and inference. |
| [arena-handle](/examples/arena-handle.html) | A generational arena with stable handles, done with pure value updates. |
| [triga-budapest](/examples/triga-budapest.html) | Geometry construction from the 3D scene rendered on the home page. |

Every package above lives in [faberlang/examples](https://github.com/faberlang/examples), which holds more than is shown here — coreutils in full, the whole GPU workload ladder, reader-locale demos, and the package-store lab.

## Running them {#running}

Once you have [installed Faber](/start/install.html):

```bash
git clone https://github.com/faberlang/examples.git
faber check examples/coreutils/packages/cat
faber run examples/coreutils/packages/cat
```

Entry commands vary by package; each has its own `README.md`. The daily command loop is on the [cheat sheet](/cheatsheet/commands.html).
