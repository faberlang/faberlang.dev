完成 hello-world 後，接著開始接觸真正的套件。Faber 以套件為導向；最快的學習方式，是檢查並閱讀那些操作面與你計畫使用的編譯器介面相同的現有套件。

## 公開儲存庫 {#repositories}

| 儲存庫 | 從這裡開始 | 原因 |
|---|---|---|
| [`faberlang/examples`](https://github.com/faberlang/examples) | `corpus/`、應用程式套件、tracks | 公開語料庫與應用程式範例 |
| [`faberlang/norma`](https://github.com/faberlang/norma) | `norma:*` 套件 | 標準函式庫原始碼 |
| [`faberlang/faber`](https://github.com/faberlang/faber) | CLI 包裝器 | 面向使用者的建置工具 |
| [`faberlang/cista`](https://github.com/faberlang/cista) | package-store CLI/lib | 套件管理介面 |
| [`faberlang/triga`](https://github.com/faberlang/triga) | `triga:*` 原始碼 | 圖形與幾何函式庫 |

## 複製學習工作區 {#clone-workspace}

<<<FENCE 0>>>

包含 `norma:*` 匯入的套件，會從 `faber.lock` 記錄的 Cista 套件儲存庫解析相依性。只有在你有意為函式庫開發使用本機解析器覆寫時，才使用 `FABER_LIBRARY_HOME`。

## 依照以下順序閱讀範例 {#read-order}

1. [快速導覽](/start/)：瞭解表面語法。
2. [Hello, Faber](/start/hello.html)：瞭解單一套件。
3. [語料庫](/corpus/)：每個關鍵字或建構各有一個頁面。
4. [範例](/start/examples.html)：瞭解較大型的應用程式。
5. [Faber 建置工具](/tooling/faber-build-tool.html)：瞭解 CLI 詳細資訊。

## 代理程式工作流程 {#agent-workflow}

代理程式不應僅根據說明文字推斷語法。請使用機器介面，然後驗證產生的程式碼：

<<<FENCE 1>>>

處理套件工作時，請在報告中引用儲存庫、套件路徑、命令與診斷碼。如果你在此網站中修改含有 Faber 程式碼區塊的文件，請在宣稱範例仍可編譯之前，先執行程式碼區塊驗證器。

## 開始軌道之後還有什麼 {#after-start}

| 目標 | 閱讀內容 |
|---|---|
| 學習語法 | [語法](/syntax/) |
| 瞭解語系 | [讀者語系](/features/reader-locale.html) |
| 使用編譯器 | [Faber 建置工具](/tooling/faber-build-tool.html)與 [Radix 編譯器](/tooling/radix-compiler.html) |
| 瀏覽建構 | [語料庫](/corpus/) |
| 使用函式庫進行建置 | [生態系](/ecosystem/) |

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [你將使用的命令](/start/commands.html) | [範例](/start/examples.html) |
