+++
translation_kind = "translated"

title = "AI Workbench"
section = "ecosystem"
order = 4
sources = [
  "examples/ai-workbench/ (README.md, package, harness)",
]


prose_hash = "sha256:3a8940d1ee168b9bdf75f40f70ce5e5eb6b6446f47510df9c3511b2d4d1bef33"
code_hash = "sha256:dc8f04249d6a95c65b63ba0ccd58c402d6f8ed47a96bc15da4b6ad844922d007"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
AI Workbench 是一個 Faber CLI 應用程式，用於本機模型清單、 中繼資料檢查、嵌入、索引與推論工作流程。它示範 Faber 建置具備實際 I/O、JSON 輸出與 Python 測試控制器驗證功能的大型多指令 CLI 應用程式。

## 套件 {#package}

`examples/ai-workbench/packages/faber-ai/`，包含以下 CLI 子命令：

- `model inspect` — 查詢本機模型別名、路由與狀態
- `embed` — 從文字輸入產生嵌入

## 命令 {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

## 驗證 {#validation}

AI Workbench 包含 20 多個 Python 測試控制器指令碼，會將 Faber 輸出與模型清單、推論、GPU 證據、工作階段生命週期及套件重複使用的固定資料對照，示範對已編譯 Faber 二進位檔進行跨語言驗證。
