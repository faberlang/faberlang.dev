## System prompt snippet (reader pack)

輸出採用讀者語系的繁體中文 Faber,並在宣告、控制流程、迴圈、回傳值、布林值、常見基本型別,以及適當時機的清單/映射集合使用中文關鍵字。保持 Faber 的符號語法不變。一律使用繁體字(非簡體字)。

## Instructions

將下列正文由英文翻譯為目標語系。請遵循以下規則:

- 僅翻譯正文,不要翻譯程式碼區塊。
- 完整保留 {#anchors}(標題錨點)。
- 保留 Markdown 結構(標題、段落、清單)。
- 保留表格形狀(欄數、對齊)。
- 保留連結。路徑可維持絕對路徑(/start/...),因為產生器會加上語系路徑前綴。
- 圍欄以 "<<<FENCE n>>>" 標記呈現。輸出中請保持這些標記不變。
- 回傳含標記的完整正文。
- 僅回傳翻譯後的 Markdown 正文(無 frontmatter、前言、備註或結語)。
- 全篇使用繁體中文(繁體),絕不使用簡體中文(简体)。

## English source body

完成 hello-world 後,接著進入真實套件。Faber 以套件為導向;最快的學習方式是檢查並閱讀既有的套件,這些套件會使用你打算採用的同一套編譯器介面。

## Public repositories {#repositories}

| 儲存庫 | 從這裡開始 | 原因 |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`、應用程式套件、學習軌 | 公開語料庫與應用程式範例 |
| [`faberlang/norma`](https://github.com/faberlang/norma) | `norma:*` 套件 | 標準函式庫原始碼 |
| [`faberlang/faber`](https://github.com/faberlang/faber) | CLI 封裝器 | 面向使用者的建置工具 |
| [`faberlang/cista`](https://github.com/faberlang/cista) | 套件庫 CLI/函式庫 | 套件管理介面 |
| [`faberlang/triga`](https://github.com/faberlang/triga) | `triga:*` 原始碼 | 圖形與幾何函式庫 |

## Clone a learning workspace {#clone-workspace}

<<<FENCE 0>>>

帶有 `norma:*` 匯入的套件會從 `faber.lock` 中記錄的 Cista 套件庫解析相依性。僅在你刻意要為函式庫開發進行本機解析器覆寫時,才使用 `FABER_LIBRARY_HOME`。

## Read examples in this order {#read-order}

1. [快速導覽](/start/)瞭解介面文法。
2. [Hello, Faber](/start/hello.html)瞭解單一套件。
3. [語料庫](/corpus/)每個關鍵字或結構各一頁。
4. [範例](/start/examples.html)瞭解較大的應用程式。
5. [Faber 建置工具](/tooling/faber-build-tool.html)瞭解 CLI 細節。

## Agent workflow {#agent-workflow}

代理程式不應僅憑正文推斷語法。請先使用機器介面,再驗證產生的程式碼:

<<<FENCE 1>>>

進行套件工作時,請在報告中引用儲存庫、套件路徑、指令與診斷代碼。若你修改了本站內含 Faber 圍欄程式碼的文件,請在宣稱範例仍可編譯之前執行圍欄驗證器。

## What comes after the start track {#after-start}

| 目標 | 閱讀 |
|---|---|
| 學習語法 | [語法](/syntax/) |
| 瞭解語系 | [讀者語系](/features/reader-locale.html) |
| 使用編譯器 | [Faber 建置工具](/tooling/faber-build-tool.html)與 [Radix 編譯器](/tooling/radix-compiler.html) |
| 瀏覽結構 | [語料庫](/corpus/) |
| 以函式庫建置 | [生態系](/ecosystem/) |

## Next {#next}

| 上一頁 | 下一頁 |
|---|---|
| [你會用到的指令](/start/commands.html) | [範例](/start/examples.html) |
