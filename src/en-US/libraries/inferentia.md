+++
title = "Inferentia — local inference"
section = "libraries"
order = 5
sources = [
  "sibling inferentia/ repository",
  "inferentia/README.md",
  "inferentia/faber.toml",
  "inferentia/src/main.fab",
  "inferentia/evidence/i-live-receipt.md",
]
+++

Inferentia is a local-first inference server written in Faber. It is meant to
load a GGUF language model from disk and serve it through a command-line tool
and a small HTTP API, on your own machine, with no outside service.

It is an application, not a library you import. It is listed here because it is
built on Gradus and Norma, which makes it a real test of both. It is in
development and is not a released product; read the [status](#status) section
first.

## Who owns what {#boundary}

Inferentia owns the product: configuration, the command line and API contracts,
the request lifecycle, streaming, and cancellation. The model itself is not
here.

- [Gradus](/libraries/gradus.html) owns the machine-learning semantics:
  admitting a GGUF file, the tokenizer, and the generation loop. Inferentia
  declares it as a dependency in `faber.toml`.
- [Norma](/libraries/norma.html) provides the HTTP server, headers, and
  server-sent events.
- `llama.cpp` is a reference oracle for comparing output. It is not a
  dependency.

The design stance is to fail closed: an unsupported architecture, quantization,
or tokenizer is an error with a typed cause, not a silent approximation.

## Commands {#commands}

The command line has two subcommands.

```text
inferentia serve --model <PATH> [options]
inferentia live  --model <PATH> [--prompt TEXT] [--ignore-eos]
```

`serve` binds an HTTP listener on the loopback interface. `live` loads a model,
generates one completion for a prompt, prints the token ids and the decoded
text, and exits.

| Option | Meaning |
|--------|---------|
| `-m, --model <PATH>` | Path to the GGUF file (required) |
| `--host <HOST>` | Bind host; loopback only, default `127.0.0.1` |
| `--port <PORT>` | Bind port; default `8080`, `0` picks a free port |
| `--max-tokens <N>` | Default output token ceiling; default `32` |
| `--max-prompt <N>` | Prompt-token admission bound; default is the model's limit |
| `--context <N>` | Session context ceiling; default is the model's limit |
| `--seed <N>` | Deterministic seed; default `1` |
| `--log-level <LEVEL>` | `info`, `warn`, or `error` on stderr |
| `--expected-digest <SHA256>` | `serve`: require the admitted model's digest to match |

Usage errors are reported before the listener binds.

## The HTTP API {#api}

`serve` answers three paths:

| Path | What it does |
|------|--------------|
| `/health` | Reports `starting`, then `ready` with the model identity, or `failed` with the typed cause |
| `/model` | The admitted model's identity facts, or `503` before the server is ready |
| `/generate` | Takes a JSON request, validates it against Gradus's admission rules, and returns JSON |

The server binds first and admits the model afterward, so `/health` can report
progress. `/generate` returns JSON by default. With `Accept: text/event-stream`
or `?stream=1` it sends one server-sent event per token; generation itself is
still a batch call, so this is a streaming format, not streaming compute.

## Status {#status}

As of 2026-09-30:

| Layer | State |
|-------|-------|
| Command line, configuration, and `/health`, `/model`, `/generate` | Written, in one source file of about 2,850 lines |
| Model admission, tokenizer, generation | Provided by Gradus |
| Package check | Does not pass today: Inferentia imports Gradus, which currently fails `faber check` |
| End-to-end result | The one recorded live run did not match its expected output (see below) |
| Hardware | The current work targets the CPU path. GPU execution is planned separately |
| Speed and quality | No claims. No measurements are published |
| Deployment and machine provisioning | A separate work stream |

**The recorded run.** On 2026-08-18 a live run loaded a 360-million-parameter
SmolLM2 model (Q4_K_M quantization) and generated with greedy decoding and a
fixed seed. The first
token matched the expected output; the second was the end-of-sequence token, so
generation stopped after two tokens instead of the expected sixteen. The
verdict was recorded as a failure. The run took about 22 minutes in a debug
build. The repository's evidence directory holds no later receipt.

Inferentia is a good place to read how a real Faber application is put
together, and an honest picture of where local inference stands. It is not yet
a tool to run models with.

Source: [github.com/faberlang/inferentia](https://github.com/faberlang/inferentia).
