+++
translation_kind = "translated"

title = "Design documents"
section = "references"
order = 2
sources = [
  "radix/docs/design/README.md",
]


prose_hash = "sha256:c668ff445d22132defdedd2c1535366f6ce81513e0ae589bd1ab450683a06c3f"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
Radix 儲存了說明 Faber 作為語言與編譯器運作方式的權威設計文件。這些文件位於
`radix/docs/design/`。

## 索引 {#index}

| 範疇 | 檔案 |
|------|-------|
| 目標與降低層級 | `target-capability-matrix.md`、`lowering-routes.md`、`semantic-ownership.md` |
| 型別與語法糖 | `numeric-type-sugar.md`、`comparison-operators.md`、`annotation-sugar.md` |
| 集合內建操作 | `lista-intrinsics.md`、`tabula-intrinsics.md`、`tensor-intrinsics.md`、`numerus-intrinsics.md`、`fractus-intrinsics.md`、`textus-intrinsics.md`、`intervallum-intrinsics.md`、`instans-intrinsics.md`、`copia-intrinsics.md` |
| 轉換 | `conversio-valor.md`、`failable-conversio.md` |
| 框架與效果 | `frame-stream-types.md`、`host-provider-gateway.md` |
| 讀取器與格式 | `reader-locale.md`、`faber-canonical-surface.md` |
| 系統／AIR | `air-dialect.md`、`aiml-foundation.md`、`systems-shaped-values.md` |
| 工具表面 | `faber-scripting.md` |
| 命名技術債 | `mixed-case-naming-debt.md` |

## 標準函式庫設計文件 {#stdlib-design-docs}

`radix/docs/stdlib/` 目錄包含：

| 文件 | 作用 |
|-----|------|
| `morphologia.md` | 所有標準函式庫方法名稱的變化政策 |
| `tensor-methods.md` | Tensor 接收器方法參考 |
| `chorda-methods.md` | Chorda（文字）方法參考 |
| `mathesis-methods.md` | Math 方法參考 |
| `tempus-methods.md` | 時間方法參考 |
| `stdlib-mechanical-verbs.md` | `pange`／`solve`／`tempta` 三元組政策 |
