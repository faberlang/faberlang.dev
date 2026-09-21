+++
title = "目標相容性"
section = "targets"
order = 2
sources = "faber/docs/EBNF_MATRIX.md · target-capability-matrix.md · faber targets"

translation_kind = "translated"
prose_hash = "sha256:6f4c9cd19262b07c8c3d4b18dd87f89f4321de822f6fab5c138a0b1c13f3dee1"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "abae3f195790fe8cfe9061376b8f66e3d08489b9"
source_locale = "en-US"
+++

Faber 是一種語言，但有多個編譯契約。本頁是**經測量的可降階能力矩陣**：
針對 corpus 中的每個術語，列出哪些目標可以將它降階，以及支援程度。

政策動詞（支援 / 消除 / 警告 / 拒絕 / 延後）與管線路由位於
[Codegen targets](/tooling/codegen-targets.html)。本頁是下方表格中的大型可掃描
列清單 — HIR 應用途徑目標與 MIR 系統途徑目標並列顯示。

即時 CLI 摘要：`faber targets`。

**渲染時間**：unknown，由 `faber/scripta/render-matrices.py` 基於 radix 測量 JSON 渲染 — **請勿編輯**。
**測量**：`emit_hir_target_matrix` + `emit_mir_target_matrix`（程序內完成，不使用外部 toolchain）。
**連結**：`corpus/index.toml` 中的 terms → exempla。

這是**官方產生的 grammar×target 支援矩陣**。它針對 exempla corpus 中的每個
term，報告**可降階能力** — target X 是否能將 grammar production Y 降階。
執行期語意（消除/警告/延後政策動詞）、各目標契約與管線路由位於
[Codegen targets](/tooling/codegen-targets.html)；該文件連回本頁以顯示這些列。

## 圖例

| 符號 | 意義 |
|---|---|
| ✓ | 完整支援 — 該術語的所有可分析 exempla 都能降階 |
| ◐ | 部分支援 — 部分 exempla 能降階，部分存在已測量的缺口 |
| ○ | 已規劃 — 尚未降階；使用整理後的覆寫檔 (`scripta/ebnf-matrix-overrides.toml`) |
| ✕ | 不支援 — 沒有 exempla 能降階；依預設事實，已測量的缺口確實存在 |
| — | 未測量 — 此途徑上沒有該術語的可分析 exempla |

> ✓ 表示使用此術語的 corpus exempla 能降階至目標。這**不**保證執行期語意
> 完全一致。某些目標會對特定建構進行*消除*或*警告*（例如 Go 會消除借用
> 模式 `de`/`in`/`ex`）— 這些仍在此顯示為 ✓，因為它們能降階。此細節請參閱
> 政策文件。

## Corpus 全域摘要（所有已註冊術語）

**應用途徑（HIR → 輸出的原始語言）**

| 目標 | 可支援 | 可分析 | % |
|---|---|---|---|
| rust | 340 | 344 | 99% |
| go | 319 | 344 | 93% |
| ts | 344 | 344 | 100% |
| faber | 344 | 344 | 100% |

**系統途徑（MIR → 裝置/IR 產物）**

| 目標 | 可支援 | 可分析 | % |
|---|---|---|---|
| llvm-text | 311 | 338 | 92% |
| wasm-text | 249 | 338 | 74% |
| wasm | 249 | 338 | 74% |
| sexp-struct | 272 | 338 | 80% |
| sexp | 272 | 338 | 80% |
| scena | 282 | 338 | 83% |

## 關鍵字 — 應用途徑

### 關鍵字

| 術語 | rust | go | ts | faber |
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

## 運算子 — 應用途徑

### 運算子群組

| 術語 | rust | go | ts | faber |
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

## 關鍵字 — 系統途徑

### 關鍵字

| 術語 | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
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

## 運算子 — 系統途徑

### 運算子群組

| 術語 | llvm-text | wasm-text | wasm | sexp-struct | sexp | scena |
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

## 其他術語（`existing-home` / 未指定）

### existing-home

| 術語 | rust | go | ts | faber |
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
