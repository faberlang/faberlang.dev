+++
translation_kind = "translated"

title = "Codegen targets"
section = "tooling"
order = 1
sources = [
  "radix/docs/design/target-capability-matrix.md (40 KB)",
  "radix/README.md (Codegen Targets and HIR/MIR Split)",
  "faber targets CLI output",
]


prose_hash = "sha256:ceba78ab8cc04dea45e96377964059873b7b20582f3f069e74cdde8c65e72841"
code_hash = "sha256:efae27bbf8b10e74385b4ced2bb6b500d0ffc2dea16d0c43ef64b138ba88fc4f"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Faber 只有一种语言，但有多个编译契约。并非每个特性都必须下沉到每个目标。本页记录每个目标支持、擦除、警告或拒绝哪些特性。

## 策略动词 {#policy-verbs}

| 动词 | 含义 |
|------|---------|
| **支持（Support）** | 以预期语义下沉 |
| **擦除（Erase）** | 类型检查通过；代码生成丢弃目标特定语义 |
| **警告（Warn）** | 合法的 Faber；在目标上无效或行为降级 |
| **拒绝（Reject）** | 检查或发射失败并给出明确诊断 |
| **推迟（Defer）** | 解析/绑定通过；任何目标均未实现下沉 |
| **受限（Limited）** | 带有显式子集门控的稳定契约 |

## 目标表 {#target-table}

| 目标 | 通道 | 构建 | 运行 | 打包 | 策略 |
|--------|------|-------|-----|---------|--------|
| `rust` | HIR | 是 | 是 | 是 | **支持** |
| `fmir-text` | MIR | 是 | 是 | 是 | **支持** |
| `fmir` | MIR | 是 | 是 | 是 | **支持** |
| `fmir-bin` | MIR | 是 | 是 | 是 | **支持** |
| `faber` | HIR | 是 | 否 | 否 | **支持** |
| `ts` | HIR | 是 | 否 | 否 | **探测（Probe）** |
| `go` | HIR | 是 | 否 | 否 | **擦除** |
| `wasm` | MIR | 是 | 否 | 否 | **受限** |
| `wasm-text` | MIR | 是 | 否 | 否 | **受限** |
| `llvm-text` | MIR | 是 | 否 | 否 | **受限** |
| `metal-text` | MIR | 是 | 否 | 否 | **受限** |
| `wgsl-text` | MIR | 是 | 否 | 否 | **受限** |
| `sexp` | MIR | 是 | 否 | 否 | **受限** |

## 管道路由 {#pipeline-routing}

```
Source → Lex → Parse → Collect → Resolve → Lower → Typecheck → Analysis
                                                              ↓
                                    ┌─────────────────────────┴──────────┐
                                    │                                    │
                              HIR backends                        MIR backends
                                    │                                    │
            Rust · Faber · TS · Go            fmir · wasm · llvm · metal · wgsl · sexp
```

## 应用通道（HIR） {#application-lane-hir}

| 目标 | 测得基线 |
|--------|---------------|
| Rust | 生产路径。借用模式、CLI 生成、可失败的 Result 下沉。 |
| Faber | 规范源视图 / 往返。非执行后端。 |
| TypeScript | 288/318 已分析 · 268/318 类型检查有效 · 262/318 可运行 |
| Go | 146/216 通过。借用模式被擦除；`ad` 被拒绝。 |

## 系统通道（MIR） {#systems-lane-mir}

| 目标 | 测得基线 |
|--------|---------------|
| fmir* | 打包 MIR 镜像；运行器证明源独立性。 |
| wasm | 200/289 已发射 · 195/289 校验通过 · 171/289 桩宿主可运行 |
| llvm-text | 249/289 已发射 · 232/289 验证器有效 · 65/289 可运行 |
| metal-text | 设备安全内核子集；88 项聚焦测试。战役已暂停。 |
| wgsl-text | 通过 naga 30.x 校验。87 项聚焦测试。反射边车。 |
| sexp | 193 已发射 · 190 Racket 编译通过 · 190 Racket 运行通过。校验目标。 |

如需查看实时能力标志，请运行 `faber targets`。
