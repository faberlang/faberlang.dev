本頁是 Faber 工作第一週的實用 CLI 對照表。請先將它作為指令索引，需要旗標與編譯器管線詳細資訊時，再開啟完整的 [Faber 建置工具](/tooling/faber-build-tool.html) 頁面。

## 每日流程 {#daily-loop}

| 指令 | 用途 |
|---|---|
| `faber check <package>` | 快速前端驗證：詞法分析、剖析、型別檢查、降階 |
| `faber build <package> -t rust` | 產生 Rust 專案，以供審查或原生編譯 |
| `faber run <package>` | 建置並執行應用程式套件 |
| `faber test <package>` | 當套件定義測試介面時，執行套件測試 |
| `faber explain <code>` | 閱讀穩定的診斷說明 |

請從 `check` 開始。這是成本最低的指令，也是代理程式在提出產生的程式碼可視為有效 Faber 之前應執行的指令。

## 檢查 {#check}

<<<FENCE 0>>>

通過 `check` 表示套件在語法與語意上都符合編譯器前端的要求。這不表示最終的原生工具鏈已經被呼叫。

## 建置 {#build}

<<<FENCE 1>>>

Rust 目標刻意設計成便於審查。產生的 Rust 是編譯器產物，不是真實來源；請編輯 Faber 套件並重新建置，而不是手動修補輸出的 Rust。

## 執行 {#run}

<<<FENCE 2>>>

對於具有 `incipit` 進入點的應用程式套件，請使用 `run`。只有函式庫的套件則應改為檢查與測試。

## 解釋診斷 {#explain}

<<<FENCE 3>>>

診斷系列是穩定的識別代號：`LEX` 代表詞法錯誤，`PAR` 代表剖析器錯誤，`SEM` 代表語意／型別錯誤。在文件與代理程式報告中，請引用診斷代碼，不要含糊地改述編譯器失敗。

## 讀者語系指令 {#reader-locale}

<<<FENCE 4>>>

讀者語系輸出是編譯器語意模型的呈現，不是瀏覽器執行期間的翻譯層。語系工作應在套件以規範形式通過 `check` 之後進行。

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [Hello, Faber](/start/hello.html) | [專案與範例](/start/projects.html) |
