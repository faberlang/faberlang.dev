# Zombie docs pass — 48h product delta (2026-08-07)

**Mode:** repair (high-priority public surfaces)  
**Window:** ~20–48h of GPU + HIR target/matrix work across radix/faber/hosts/runtime/examples  
**Evidence:** parallel explore agents + live floors in `faber/crates/exempla` + `radix/EBNF_MATRIX.md`

## Research summary

### GPU / device (known)

| Bucket | Status |
| --- | --- |
| Dual-backend device training (Metal + CUDA), MLP path, oracle comparison | **Proven now** |
| NVVM descriptor v2 + host launch adapter | Landed |
| RunPod matrix / rung-0 matmul on A100 | Engineering verification (optional site claim later) |
| BERT-tiny CUDA numeric (Stage 6) | **Not** claimable — last committed numeric FAIL; fix landed without re-run PASS |
| GPU inference GI0–GI2 CPU oracle | Engineering-real |
| End-to-end **device** inference | **Not shipped** |
| Multi-device / distributed | **Frontier** |

### HIR Go / TS (known)

| Target | Old site floor | Live exempla floor (2026-08-07) |
| --- | --- | --- |
| TypeScript | 288/318 · 268 typecheck · 262 runnable | 288 analysed · 289 emitted · 285 typecheck · **283 runnable** |
| Go | 146/216 pass | **251 pass** · 304 accepted outcomes |
| Matrix summary | rust 277/279, go 261, ts 273 | rust **278/280**, go **262**, ts **274**, faber **280** |

Also: modular-width TS words, Valor JSON-root, Go type/valor carriers, faber-owned postprocess on Go/browser builds, identifier sanitation.

## Repairs applied this pass

| Surface | Change |
| --- | --- |
| `src/en-US/index.md` | Removed primary-executable framing; sharpened GPU training/inference honesty; fixed 8-locale enumeration |
| `src/en-US/start/index.md` | 1.3.0 → **1.4.0** |
| `src/en-US/toolchain/compiling.md` | Go/TS floors; Rust “widest package surface”; Metal/CUDA vs WebGPU wording; TS/Go roles |
| `src/en-US/toolchain/radix.md` | Primary → projection / package surface ranking |
| `src/en-US/toolchain/cli.md` | Cargo “primary product path” softened |
| `src/en-US/toolchain/target-matrix.md` | Summary numbers from live `EBNF_MATRIX.md`; fixed dead `/tooling/codegen-targets` links |
| `generator/scripts/generate-landing.py` | No primary Rust; FLIB removed; HIR/locale rows fixed; LLVM note; training/inference copy |
| `dist/index.html` | Regenerated via `generate-landing.py` |
| `static/llms.txt`, `static/agents/index.md` | **1.4.0** install pins; `/` = landing, `/porta/` = chooser; first appeared 2025 |
| `dist/llms.txt`, `dist/agents/index.md`, `dist/llms-full.txt` | Synced |

## Follow-up (same day) — matrix % vs GPU product

Operator concern: `metal-text` / `wgsl-text` show **2%** while Metal/CUDA training
runs; no CUDA line.

**Root cause (known):** the EBNF matrix scores **every language corpus term**
against each **emit target**. `metal-text` and `wgsl-text` are **device-kernel
subset** emitters; most of the ~280 terms are host-language surface and correctly
do not lower. **CUDA is not an emit target** — it is `faber run --backend cuda`
on the llvm/NVVM→PTX device chain.

**Doc fix:** `target-matrix.md` summary rewritten into HIR / general-MIR /
kernel-subset tables + “how to read %” + CUDA column absence table.
`compiling.md` systems-lane section aligned.

**Follow-up 2:** Added public **Device kernel support** section on
`target-matrix.md` — product backends, workload families, expanding RunPod CUDA
card matrix (honest scope), links to examples. Cross-links from compiling + en-US
index.

## Residual (not fully repaired)

1. **`dist/en-US/** HTML** for authored pages still needs `build-site.sh` (requires Faber generator build — not run this session; Cargo-heavy).
2. **Full term tables** in `target-matrix.md` still lag row-by-row; only the **corpus-wide summary** was refreshed. Re-run matrix publish pipeline when convenient.
3. **Non-English locale** homepage/install/releases still pin 1.1.1 / 1.2.0.
4. **AGENTS.md** in this repo still describes `/` as the portal in places — should match landing.
5. Optional public claims **not** added: RunPod card list, SmolLM2 product name on landing (kept high-level on en-US inference section only).
6. Do **not** claim CUDA BERT-tiny PASS or device inference shipped.

## Operator next steps

```bash
cd faberlang.dev
bash generator/scripts/build-site.sh   # when ready to refresh dist/en-US HTML
# commit + push main for Pages deploy
```

## Related

- Workspace marketing: `../docs/marketing/` (launch already live on `@faberlang`)
