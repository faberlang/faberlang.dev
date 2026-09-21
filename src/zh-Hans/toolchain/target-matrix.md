+++
title = "目标兼容性"
section = "targets"
order = 2
sources = "faber/docs/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"

translation_kind = "translated"
prose_hash = "sha256:ce6e1560416ba88fe769242c8672a5122942625bd841f6cde67ba040df0554b7"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "abae3f195790fe8cfe9061376b8f66e3d08489b9"
source_locale = "en-US"
+++

Faber 是一门语言，但有多个编译契约。本页是**经过测量的可下沉能力矩阵**：
对于 corpus 中的每个术语，列出哪些目标可以下沉它，以及支持程度。

策略动词（支持 / 擦除 / 警告 / 拒绝 / 推迟）和管线路由位于
[Codegen targets](/tooling/codegen-targets.html)。本页是下面表格中的大型可扫描
行列表 — HIR 应用通道目标与 MIR 系统通道目标并列显示。

实时 CLI 摘要：`faber targets`。

**渲染时间**：unknown，由 `faber/scripta/render-matrices.py` 基于 radix 测量 JSON 渲染 — **请勿编辑**。
**测量**：`emit_hir_target_matrix` + `emit_mir_target_matrix`（进程内完成，不使用外部 toolchain）。
**连接**：`corpus/index.toml` 中的 terms → exempla。

这是**官方生成的 grammar×target 支持矩阵**。它报告 exempla corpus 中每个
term 的**可下沉能力** — target X 是否能够下沉 grammar production Y。运行时
语义（擦除/警告/推迟策略动词）、各目标契约和管线路由位于
[Codegen targets](/tooling/codegen-targets.html)；该文档链接回本页以查看这些行。

## 图例

| 符号 | 含义 |
|---|---|
| ✓ | 完全支持 — 该术语的所有可分析 exempla 都能下沉 |
| ◐ | 部分支持 — 部分 exempla 能下沉，部分存在已测量的缺口 |
| ○ | 计划中 — 尚未下沉；使用整理后的覆盖文件 (`scripta/ebnf-matrix-overrides.toml`) |
| ✕ | 不支持 — 没有 exempla 能下沉；按默认事实，已测量的缺口确实存在 |
| — | 未测量 — 此 lane 上没有该术语的可分析 exempla |

> ✓ 表示使用该术语的 corpus exempla 能够下沉到目标。它**不**保证运行时语义
> 完全相同。某些目标会对特定构造进行*擦除*或*警告*（例如 Go 会擦除借用
> 模式 `de`/`in`/`ex`）— 这些构造仍在此显示为 ✓，因为它们能够下沉。具体
> 差异请参阅策略文档。

## Corpus 总览（所有已注册术语）

**应用通道（HIR → 输出的源语言）**

| 目标 | 可支持 | 可分析 | % |
|---|---|---|---|
| rust | 340 | 344 | 99% |
| go | 319 | 344 | 93% |
| ts | 344 | 344 | 100% |
| faber | 344 | 344 | 100% |

**系统通道（MIR → 设备/IR 产物）**

| 目标 | 可支持 | 可分析 | % |
|---|---|---|---|
| llvm-text | 311 | 338 | 92% |
| wasm-text | 249 | 338 | 74% |
| wasm | 249 | 338 | 74% |
| sexp-struct | 272 | 338 | 80% |
| sexp | 272 | 338 | 80% |
| scena | 282 | 338 | 83% |

## 关键字 — 应用通道

### 关键字

| 术语 | rust | go | ts | faber |
|---|---|---|---|---|
| <a id="abstractus"></a>`abstractus` | ✓ | ✓ | ✓ | ✓ |
| <a id="ab"></a>`ab` | ✓ | ✓ | ✓ | ✓ |
| <a id="ad"></a>`ad` | ✓ | ✕ | ✓ | ✓ |
| <a id="adfirma"></a>`adfirma` | ✓ | ✓ | ✓ | ✓ |
| <a id="ante"></a>`ante` | ✓ | ✓ | ✓ | ✓ |
| <a id="atomic"></a>`atomic` | ✕ | ✓ | ✓ | ✓ |
| <a id="argumenta"></a>`argumenta` | ✓ | ✓ | ✓ | ✓ |
| <a id="bivalens"></a>`bivalens` | ✓ | ✓ | ✓ | ✓ |
| <a id="cape"></a>`cape` | ✓ | ✓ | ✓ | ✓ |
| <a id="casu"></a>`casu` | ✓ | ✓ | ✓ | ✓ |
| <a id="cede"></a>`cede` | ✓ | ✓ | ✓ | ✓ |
| <a id="ceteri"></a>`ceteri` | ✓ | ✓ | ✓ | ✓ |
| <a id="ceterum"></a>`ceterum` | ✓ | ✓ | ✓ | ✓ |
| <a id="clausura"></a>`clausura` | ✓ | ✓ | ✓ | ✓ |
| <a id="cli"></a>`cli` | ✓ | ✓ | ✓ | ✓ |
| <a id="copia"></a>`copia` | ✓ | ✓ | ✓ | ✓ |
| <a id="cura"></a>`cura` | ✓ | ✓ | ✓ | ✓ |
| <a id="curata"></a>`curata` | ✓ | ✓ | ✓ | ✓ |
| <a id="cursor"></a>`cursor` | ✓ | ✓ | ✓ | ✓ |
| <a id="custodi"></a>`custodi` | ✓ | ✓ | ✓ | ✓ |
| <a id="de"></a>`de` | ✓ | ✓ | ✓ | ✓ |
| <a id="descriptio"></a>`descriptio` | ✓ | ✓ | ✓ | ✓ |
| <a id="discerne"></a>`discerne` | ✓ | ✓ | ✓ | ✓ |
| <a id="discretio"></a>`discretio` | ✓ | ✓ | ✓ | ✓ |
| <a id="dum"></a>`dum` | ✓ | ✓ | ✓ | ✓ |
| <a id="ego"></a>`ego` | ✓ | ✓ | ✓ | ✓ |
| <a id="elige"></a>`elige` | ✓ | ✓ | ✓ | ✓ |
| <a id="errata"></a>`errata` | ✓ | ✓ | ✓ | ✓ |
| <a id="est"></a>`est` | ✓ | ✓ | ✓ | ✓ |
| <a id="ex"></a>`ex` | ✓ | ✓ | ✓ | ✓ |
| <a id="exitus"></a>`exitus` | ✓ | ✓ | ✓ | ✓ |
| <a id="fac"></a>`fac` | ✓ | ✓ | ✓ | ✓ |
| <a id="falsum"></a>`falsum` | ✓ | ✓ | ✓ | ✓ |
| <a id="fient"></a>`fient` | ✓ | ✓ | ✓ | ✓ |
| <a id="fiet"></a>`fiet` | ✓ | ✓ | ✓ | ✓ |
| <a id="figendum"></a>`figendum` | ✓ | ✓ | ✓ | ✓ |
| <a id="finge"></a>`finge` | ✓ | ✓ | ✓ | ✓ |
| <a id="fiunt"></a>`fiunt` | ✓ | ✓ | ✓ | ✓ |
| <a id="fixum"></a>`fixum` | ✓ | ✓ | ✓ | ✓ |
| <a id="fragilis"></a>`fragilis` | ✓ | ✓ | ✓ | ✓ |
| <a id="fractus"></a>`fractus` | ✓ | ✓ | ✓ | ✓ |
| <a id="functio"></a>`functio` | ✓ | ✓ | ✓ | ✓ |
| <a id="futura"></a>`futura` | ✓ | ✓ | ✓ | ✓ |
| <a id="futurum"></a>`futurum` | ✓ | ✓ | ✓ | ✓ |
| <a id="generis"></a>`generis` | ✓ | ✓ | ✓ | ✓ |
| <a id="genus"></a>`genus` | ✓ | ✓ | ✓ | ✓ |
| <a id="iace"></a>`iace` | ✓ | ✓ | ✓ | ✓ |
| <a id="iacit"></a>`iacit` | ✓ | ✓ | ✓ | ✓ |
| <a id="ignotum"></a>`ignotum` | ✓ | ✓ | ✓ | ✓ |
| <a id="immutata"></a>`immutata` | ✓ | ✓ | ✓ | ✓ |
| <a id="implet"></a>`implet` | ✓ | ✓ | ✓ | ✓ |
| <a id="importa"></a>`importa` | ✓ | ✓ | ✓ | ✓ |
| <a id="in"></a>`in` | — | — | — | — |
| <a id="incipiet"></a>`incipiet` | ✓ | ✓ | ✓ | ✓ |
| <a id="incipit"></a>`incipit` | ✓ | ✓ | ✓ | ✓ |
| <a id="inter"></a>`inter` | ✓ | ✓ | ✓ | ✓ |
| <a id="intra"></a>`intra` | ✓ | ✓ | ✓ | ✓ |
| <a id="instans"></a>`instans` | ✓ | ✓ | ✓ | ✓ |
| <a id="itera"></a>`itera` | ✓ | ◐ | ✓ | ✓ |
| <a id="lege"></a>`lege` | ✓ | ✓ | ✓ | ✓ |
| <a id="lineam"></a>`lineam` | ✓ | ✓ | ✓ | ✓ |
| <a id="lista"></a>`lista` | ✓ | ✓ | ✓ | ✓ |
| <a id="matrix"></a>`matrix` | ✓ | ✕ | ✓ | ✓ |
| <a id="mone"></a>`mone` | ✓ | ✓ | ✓ | ✓ |
| <a id="mori"></a>`mori` | ✓ | ✓ | ✓ | ✓ |
| <a id="nexum"></a>`nexum` | ✓ | ✓ | ✓ | ✓ |
| <a id="nihil"></a>`nihil` | ✓ | ✓ | ✓ | ✓ |
| <a id="numquam"></a>`numquam` | ✓ | ✓ | ✓ | ✓ |
| <a id="numerus"></a>`numerus` | ✓ | ✓ | ✓ | ✓ |
| <a id="non"></a>`non` | ✓ | ✓ | ✓ | ✓ |
| <a id="omitte"></a>`omitte` | ✓ | ✓ | ✓ | ✓ |
| <a id="omnia"></a>`omnia` | ✓ | ✓ | ✓ | ✓ |
| <a id="operandus"></a>`operandus` | ✓ | ✓ | ✓ | ✓ |
| <a id="optio"></a>`optio` | ✓ | ✓ | ✓ | ✓ |
| <a id="optiones"></a>`optiones` | ✓ | ✓ | ✓ | ✓ |
| <a id="ordo"></a>`ordo` | ✓ | ✓ | ✓ | ✓ |
| <a id="octeti"></a>`octeti` | ✓ | ✓ | ✓ | ✓ |
| <a id="implendum"></a>`implendum` | ✓ | ✓ | ✓ | ✓ |
| <a id="per"></a>`per` | ✓ | ✓ | ✓ | ✓ |
| <a id="perge"></a>`perge` | ✓ | ✓ | ✓ | ✓ |
| <a id="postpara"></a>`postpara` | ✓ | ✓ | ✓ | ✓ |
| <a id="postparabit"></a>`postparabit` | ✓ | ✓ | ✓ | ✓ |
| <a id="prae"></a>`prae` | ✓ | ✓ | ✓ | ✓ |
| <a id="praefixum"></a>`praefixum` | — | — | — | — |
| <a id="praepara"></a>`praepara` | ✓ | ✓ | ✓ | ✓ |
| <a id="praeparabit"></a>`praeparabit` | ✓ | ✓ | ✓ | ✓ |
| <a id="promissum"></a>`promissum` | ✓ | ✓ | ✓ | ✓ |
| <a id="privata"></a>`privata` | ✓ | ✓ | ✓ | ✓ |
| <a id="proba"></a>`proba` | ✓ | ✓ | ✓ | ✓ |
| <a id="probandum"></a>`probandum` | ✓ | ✓ | ✓ | ✓ |
| <a id="protecta"></a>`protecta` | — | — | — | — |
| <a id="publica"></a>`publica` | ✓ | ✓ | ✓ | ✓ |
| <a id="ratio"></a>`ratio` | ✓ | ✓ | ✓ | ✓ |
| <a id="redde"></a>`redde` | ✓ | ✓ | ✓ | ✓ |
| <a id="reddet"></a>`reddet` | ✓ | ✓ | ✓ | ✓ |
| <a id="repete"></a>`repete` | ✓ | ✓ | ✓ | ✓ |
| <a id="requirit"></a>`requirit` | ✓ | ✓ | ✓ | ✓ |
| <a id="reice"></a>`reice` | ✓ | ✓ | ✓ | ✓ |
| <a id="rumpe"></a>`rumpe` | ✓ | ✓ | ✓ | ✓ |
| <a id="scribe"></a>`scribe` | ✓ | ✓ | ✓ | ✓ |
| <a id="scriptum"></a>`scriptum` | ✓ | ✓ | ✓ | ✓ |
| <a id="secus"></a>`secus` | ✓ | ✓ | ✓ | ✓ |
| <a id="si"></a>`si` | ✓ | ✓ | ✓ | ✓ |
| <a id="sic"></a>`sic` | ✓ | ✓ | ✓ | ✓ |
| <a id="sin"></a>`sin` | ✓ | ✓ | ✓ | ✓ |
| <a id="sit"></a>`sit` | ✓ | ✓ | ✓ | ✓ |
| <a id="solum-in"></a>`solum_in` | ✓ | ✓ | ✓ | ✓ |
| <a id="solum"></a>`solum` | ✓ | ✓ | ✓ | ✓ |
| <a id="sparge"></a>`sparge` | ✓ | ✓ | ✓ | ✓ |
| <a id="sponte"></a>`sponte` | ✓ | ✓ | ✓ | ✓ |
| <a id="sub"></a>`sub` | — | — | — | — |
| <a id="selective-import"></a>`selective_import` | ✓ | ✓ | ✓ | ✓ |
| <a id="tacet"></a>`tacet` | ✓ | ✓ | ✓ | ✓ |
| <a id="tacebit"></a>`tacebit` | ✓ | ✓ | ✓ | ✓ |
| <a id="tabula"></a>`tabula` | ✓ | ✓ | ✓ | ✓ |
| <a id="tag"></a>`tag` | ✓ | ✓ | ✓ | ✓ |
| <a id="temporis"></a>`temporis` | ✓ | ✓ | ✓ | ✓ |
| <a id="tensor"></a>`tensor` | ✓ | ✓ | ✓ | ✓ |
| <a id="textus"></a>`textus` | ✓ | ✓ | ✓ | ✓ |
| <a id="typus"></a>`typus` | ✓ | ✓ | ✓ | ✓ |
| <a id="ubique"></a>`ubique` | ✓ | ✓ | ✓ | ✓ |
| <a id="usque"></a>`usque` | ✓ | ✓ | ✓ | ✓ |
| <a id="ut"></a>`ut` | ✓ | ✓ | ✓ | ✓ |
| <a id="varia"></a>`varia` | ✓ | ✓ | ✓ | ✓ |
| <a id="variandum"></a>`variandum` | ✓ | ✓ | ✓ | ✓ |
| <a id="vector"></a>`vector` | ✓ | ◐ | ✓ | ✓ |
| <a id="vacuum"></a>`vacuum` | ✓ | ✓ | ✓ | ✓ |
| <a id="verum"></a>`verum` | ✓ | ✓ | ✓ | ✓ |
| <a id="vide"></a>`vide` | ✓ | ✓ | ✓ | ✓ |

## 运算符 — 应用通道

### 运算符组

| 术语 | rust | go | ts | faber |
|---|---|---|---|---|
| <a id=""></a>`⊜` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∧` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`·` | ◐ | ◐ | ✓ | ✓ |
| <a id=""></a>`×` | ✓ | ○ | ✓ | ✓ |
| <a id=""></a>`⊗` | ✓ | ○ | ✓ | ✓ |
| <a id=""></a>`⊙` | ✓ | ◐ | ✓ | ✓ |
| <a id=""></a>`→` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`←` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↤` | ✓ | ✓ | ✓ | ✓ |
| <a id="aut"></a>`aut` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`![` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!.` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≠` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!(` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊻` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↦` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇒` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`‥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`…` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≡` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`=` | ✓ | ✓ | ✓ | ✓ |
| <a id="et"></a>`et` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≥` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≤` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↓` | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u16"></a>`modulus<u16>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u32"></a>`modulus<u32>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u64"></a>`modulus<u64>` | ✓ | ✕ | ✓ | ✓ |
| <a id="modulus-u8"></a>`modulus<u8>` | ✓ | ✕ | ✓ | ✓ |
| <a id="non-est"></a>`non est` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊚` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∨` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∪` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↑` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?[` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?.` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?(` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`§` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇐` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊘` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊛` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`¬` | ✓ | ✓ | ✓ | ✓ |
| <a id="vel"></a>`vel` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∷` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∴` | ✓ | ✓ | ✓ | ✓ |
| <a id="ergo"></a>`ergo` | ✓ | ✓ | ✓ | ✓ |

## 关键字 — 系统通道

### 关键字

| 术语 | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
| --- | --- | --- | --- | --- | --- | --- |
| <a id="abstractus"></a>`abstractus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ab"></a>`ab` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ad"></a>`ad` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| <a id="adfirma"></a>`adfirma` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ante"></a>`ante` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="atomic"></a>`atomic` | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| <a id="argumenta"></a>`argumenta` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="bivalens"></a>`bivalens` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cape"></a>`cape` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="casu"></a>`casu` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="cede"></a>`cede` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="ceteri"></a>`ceteri` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ceterum"></a>`ceterum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="clausura"></a>`clausura` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="cli"></a>`cli` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="copia"></a>`copia` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="cura"></a>`cura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="curata"></a>`curata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="cursor"></a>`cursor` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="custodi"></a>`custodi` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="de"></a>`de` | — | — | — | — | — | — |
| <a id="descriptio"></a>`descriptio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="discerne"></a>`discerne` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="discretio"></a>`discretio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="dum"></a>`dum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ego"></a>`ego` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="elige"></a>`elige` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="errata"></a>`errata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="est"></a>`est` | ✓ | ✕ | ✕ | ✕ | ✕ | ✓ |
| <a id="ex"></a>`ex` | ◐ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="exitus"></a>`exitus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fac"></a>`fac` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="falsum"></a>`falsum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fient"></a>`fient` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fiet"></a>`fiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="figendum"></a>`figendum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="finge"></a>`finge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fiunt"></a>`fiunt` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fixum"></a>`fixum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="fragilis"></a>`fragilis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="fractus"></a>`fractus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="functio"></a>`functio` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="futura"></a>`futura` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="futurum"></a>`futurum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="generis"></a>`generis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="genus"></a>`genus` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="iace"></a>`iace` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id="iacit"></a>`iacit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ignotum"></a>`ignotum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="immutata"></a>`immutata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="implet"></a>`implet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="importa"></a>`importa` | ✓ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id="in"></a>`in` | — | — | — | — | — | — |
| <a id="incipiet"></a>`incipiet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="incipit"></a>`incipit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="inter"></a>`inter` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id="intra"></a>`intra` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="instans"></a>`instans` | ✓ | ✕ | ✕ | ✕ | ✕ | ◐ |
| <a id="itera"></a>`itera` | ◐ | ◐ | ◐ | ◐ | ◐ | ✓ |
| <a id="lege"></a>`lege` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="lineam"></a>`lineam` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="lista"></a>`lista` | ◐ | ◐ | ◐ | ◐ | ◐ | ✓ |
| <a id="matrix"></a>`matrix` | ✕ | ✕ | ✕ | ✓ | ✓ | ✕ |
| <a id="mone"></a>`mone` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="mori"></a>`mori` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="nexum"></a>`nexum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="nihil"></a>`nihil` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="numquam"></a>`numquam` | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ |
| <a id="numerus"></a>`numerus` | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ |
| <a id="non"></a>`non` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="omitte"></a>`omitte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="omnia"></a>`omnia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="operandus"></a>`operandus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="optio"></a>`optio` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="optiones"></a>`optiones` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="ordo"></a>`ordo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="octeti"></a>`octeti` | ✓ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id="implendum"></a>`implendum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="per"></a>`per` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="perge"></a>`perge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="postpara"></a>`postpara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="postparabit"></a>`postparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="prae"></a>`prae` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="praefixum"></a>`praefixum` | — | — | — | — | — | — |
| <a id="praepara"></a>`praepara` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="praeparabit"></a>`praeparabit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="promissum"></a>`promissum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="privata"></a>`privata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="proba"></a>`proba` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="probandum"></a>`probandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="protecta"></a>`protecta` | — | — | — | — | — | — |
| <a id="publica"></a>`publica` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ratio"></a>`ratio` | — | — | — | — | — | — |
| <a id="redde"></a>`redde` | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ |
| <a id="reddet"></a>`reddet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="repete"></a>`repete` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="requirit"></a>`requirit` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id="reice"></a>`reice` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id="rumpe"></a>`rumpe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="scribe"></a>`scribe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="scriptum"></a>`scriptum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="secus"></a>`secus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="si"></a>`si` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sic"></a>`sic` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sin"></a>`sin` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sit"></a>`sit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="solum-in"></a>`solum_in` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="solum"></a>`solum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="sparge"></a>`sparge` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="sponte"></a>`sponte` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="sub"></a>`sub` | — | — | — | — | — | — |
| <a id="selective-import"></a>`selective_import` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tacet"></a>`tacet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tacebit"></a>`tacebit` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="tabula"></a>`tabula` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="tag"></a>`tag` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="temporis"></a>`temporis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| <a id="tensor"></a>`tensor` | ✓ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id="textus"></a>`textus` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="typus"></a>`typus` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ubique"></a>`ubique` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="usque"></a>`usque` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ut"></a>`ut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="varia"></a>`varia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="variandum"></a>`variandum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vector"></a>`vector` | ✓ | ◐ | ◐ | ◐ | ◐ | ✕ |
| <a id="vacuum"></a>`vacuum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="verum"></a>`verum` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vide"></a>`vide` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## 运算符 — 系统通道

### 运算符组

| 术语 | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
| --- | --- | --- | --- | --- | --- | --- |
| <a id=""></a>`⊜` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∧` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`·` | ◐ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id=""></a>`×` | ✓ | ○ | ○ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊗` | ○ | ○ | ○ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊙` | ◐ | ◐ | ◐ | ✓ | ✓ | ◐ |
| <a id=""></a>`→` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇥` | ✓ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`←` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↤` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="aut"></a>`aut` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`![` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`!.` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`≠` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`!(` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊻` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↦` | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ |
| <a id=""></a>`⇒` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`‥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`…` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≡` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`=` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="et"></a>`et` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≥` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`≤` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↓` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="modulus-u16"></a>`modulus<u16>` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="modulus-u32"></a>`modulus<u32>` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="modulus-u64"></a>`modulus<u64>` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id="modulus-u8"></a>`modulus<u8>` | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| <a id="non-est"></a>`non est` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊚` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∨` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∪` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`↑` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`?[` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`?.` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`?(` | ✕ | ✕ | ✕ | ✓ | ✓ | ✓ |
| <a id=""></a>`§` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⇐` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊘` | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ |
| <a id=""></a>`⊛` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`¬` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="vel"></a>`vel` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`∷` | ✓ | ✓ | ✓ | ◐ | ◐ | ✓ |
| <a id=""></a>`∴` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| <a id="ergo"></a>`ergo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## 其他术语（`existing-home` / 未指定）

### existing-home

| 术语 | rust | go | ts | faber |
|---|---|---|---|---|
| <a id="alias"></a>`alias` | ✓ | ✓ | ✓ | ✓ |
| <a id="arena"></a>`arena` | ✓ | ✓ | ✓ | ✓ |
| <a id=""></a>`@` | ✓ | ✓ | ✓ | ✓ |
| <a id="f16"></a>`f16` | ✕ | ✓ | ✓ | ✓ |
| <a id="forma"></a>`forma` | ✓ | ✓ | ✓ | ✓ |
| <a id="imperia"></a>`imperia` | ✓ | ✓ | ✓ | ✓ |
| <a id="imperium"></a>`imperium` | ✓ | ✓ | ✓ | ✓ |
| <a id="iuncta"></a>`iuncta` | ✓ | ✓ | ✓ | ✓ |
| <a id="manifest"></a>`manifest` | ✓ | ✓ | ✓ | ✓ |
| <a id="metior"></a>`metior` | ✓ | ✓ | ✓ | ✓ |
| <a id="named-holes"></a>`named-holes` | ✓ | ✓ | ✓ | ✓ |
| <a id="nondum"></a>`nondum` | ✓ | ✓ | ✓ | ✓ |
| <a id="objectum"></a>`objectum` | ✓ | ✓ | ✓ | ✓ |
| <a id="prima"></a>`prima` | ✓ | ✓ | ✓ | ✓ |
| <a id="string"></a>`string` | ✓ | ✓ | ✓ | ✓ |
| <a id="block-string"></a>`block-string` | ✓ | ✓ | ✓ | ✓ |
| <a id="targets"></a>`targets` | ✓ | ✓ | ✓ | ✓ |
| <a id="ultima"></a>`ultima` | ✓ | ✓ | ✓ | ✓ |
| <a id="versio"></a>`versio` | ✓ | ✓ | ✓ | ✓ |
