本頁是 Faber 首週工作的實用 CLI 對照表。請將它當作命令索引，當你需要旗標與編譯器管線細節時，再開啟詳細的 [Faber 建置工具](/tooling/faber-build-tool.html) 頁面。

## 每日迴圈 {#daily-loop}

| 指令 | 用途 |
|---|---|
| `faber check <package>` | 快速前端驗證：詞法分析、剖析、型別檢查、降階 |
| `faber build <package> -t rust` | 產出 Rust 專案供審閱或原生編譯 |
| `faber run <package>` | 建置並執行應用程式套件 |
| `faber test <package>` | 當套件定義測試介面時執行套件測試 |
| `faber explain <code>` | 讀取穩定的診斷說明 |

請從 `check` 開始。它是最省成本的指令，也是代理在提出產生程式碼為有效 Faber 之前應先執行的指令。

## Check {#check}

<<<FENCE 0>>>

通過 `check` 表示套件對編譯器前端而言在語法與語意上均可接受。這並不代表最終的原生工具鏈已被叫用。

## Build {#build}

<<<FENCE 1>>>

Rust 目標刻意設計為可審閱。產生的 Rust 是編譯器產物，而非真理來源；請編輯 Faber 套件並重新建置，而不要以手動方式修補產出的 Rust。

## Run {#run}

<<<FENCE 2>>>

對具有 `incipit` 進入點的應用程式套件使用 `run`。純函式庫套件應改為 `check` 與測試。

## 解釋診斷 {#explain}

<<<FENCE 3>>>

診斷家族是穩定的代稱：`LEX` 代表詞法錯誤，`PAR` 代表剖析器錯誤，`SEM` 代表語意／型別錯誤。在文件與代理報告中，請引用診斷代碼，而不要鬆散地改寫編譯器失敗。

## 讀者語系指令 {#reader-locale}

<<<FENCE 4>>>

讀者語系輸出是編譯器語意模型的渲染結果，而非瀏覽器階段的翻譯層。語系工作應在套件以標準形式通過 `check` 之後再進行。

## 下一步 {#next}

| 上一篇 | 下一篇 |
|---|---|
| [Hello, Faber](/start/hello.html) | [專案與範例](/start/projects.html) |
