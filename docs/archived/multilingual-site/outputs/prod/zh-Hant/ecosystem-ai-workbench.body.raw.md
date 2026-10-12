AI Workbench 是一個 Faber CLI 應用程式，用於本機模型清單、 中繼資料檢查、嵌入、索引與推論工作流程。它示範 Faber 建置具備實際 I/O、JSON 輸出與 Python 測試控制器驗證功能的大型多指令 CLI 應用程式。

## 套件 {#package}

`examples/ai-workbench/packages/faber-ai/`，包含以下 CLI 子命令：

- `model inspect` — 查詢本機模型別名、路由與狀態
- `embed` — 從文字輸入產生嵌入

## 命令 {#commands}

<<<FENCE 0>>>

## 驗證 {#validation}

AI Workbench 包含 20 多個 Python 測試控制器指令碼，會將 Faber 輸出與模型清單、推論、GPU 證據、工作階段生命週期及套件重複使用的固定資料對照，示範對已編譯 Faber 二進位檔進行跨語言驗證。
