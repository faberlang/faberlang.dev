## 系統提示片段（讀取器套件）

發出繁體中文讀取器地區設定的 Faber，宣告、控制流程、迴圈、回傳、布林值、常用基本型別，以及清單／映射集合在適當情況下使用中文關鍵字。保持 Faber 字形語法不變。僅使用繁體字（非簡體）。

## 說明

將下方散文從英文翻譯為目標地區語言。遵循下列規則：

- 只翻譯散文。請勿翻譯程式碼圍欄。
- 完整保留 {#anchors}（標題錨點）。
- 保留 Markdown 結構（標題、段落、清單）。
- 保留表格形狀（欄數、對齊）。
- 保留連結。路徑可維持絕對路徑（/start/...），因為產生器會加上地區語言路徑前置詞。
- 圍欄以 "<<<FENCE n>>>" 標記顯示。在輸出中保持這些標記不變。
- 回傳完整的內文，並保留標記在內。
- 只回傳翻譯後的 Markdown 內文（無 frontmatter、前言、備註或後記）。
- 全文使用繁體中文字元（繁體），絕不使用簡體（简体）。

## 英文原始內文

在 hello-world 之後，進入真正的套件。Faber 以套件為導向；最快的學習方式是查閱並閱讀現有套件，這些套件會使用你打算使用的編譯器表面。

## 公開儲存庫 {#repositories}

| 儲存庫 | 從這裡開始 | 用途 |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`、應用程式套件、學習軌道 | 公開語料庫與應用程式範例 |
| [`faberlang/norma`](https://github.com/faberlang/norma) | `norma:*` 套件 | 標準函式庫原始碼 |
| [`faberlang/faber`](https://github.com/faberlang/faber) | CLI 包裝器 | 面向使用者的建置工具 |
| [`faberlang/cista`](https://github.com/faberlang/cista) | 套件商店 CLI/函式庫 | 套件管理介面 |
| [`faberlang/triga`](https://github.com/faberlang/triga) | `triga:*` 原始碼 | 圖形與幾何函式庫 |

## 複製學習工作區 {#clone-workspace}

<<<FENCE 0>>>

含有 `norma:*` 匯入的套件會從 `faber.lock` 中記錄的 Cista 套件商店解析相依項目。僅在你刻意想為函式庫開發使用本機解析器覆寫時，才使用 `FABER_LIBRARY_HOME`。

## 依照此順序閱讀範例 {#read-order}

1. [快速導覽](/start/) 以了解表面語法。
2. [你好，Faber](/start/hello.html) 以了解單一套件。
3. [語料庫](/corpus/) 以逐個關鍵字或結構閱讀一頁。
4. [範例](/start/examples.html) 以了解較大型的應用程式。
5. [Faber 建置工具](/tooling/faber-build-tool.html) 以了解 CLI 細節。

## 代理工作流程 {#agent-workflow}

代理不應僅從散文推斷語法。請使用機器表面，然後驗證產生的程式碼：

<<<FENCE 1>>>

進行套件工作時，在報告中引用儲存庫、套件路徑、指令與診斷代碼。如果你在此網站中觸及含有圍欄 Faber 程式碼的文件，請在宣稱範例仍可編譯之前執行圍欄驗證器。

## 入門軌道之後的下一步 {#after-start}

| 目標 | 閱讀 |
|---|---|
| 學習語法 | [語法](/syntax/) |
| 了解地區設定 | [讀取器地區設定](/features/reader-locale.html) |
| 使用編譯器 | [Faber 建置工具](/tooling/faber-build-tool.html) 與 [Radix 編譯器](/tooling/radix-compiler.html) |
| 瀏覽結構 | [語料庫](/corpus/) |
| 使用函式庫建置 | [生態系統](/ecosystem/) |

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [你將使用的指令](/start/commands.html) | [範例](/start/examples.html) |
