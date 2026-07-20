此頁面是 Faber 工作第一週的實用 CLI 速查表。將其用作指令索引，需要旗標與編譯器管線細節時再開啟詳細的 [Faber 建置工具](/tooling/faber-build-tool.html) 頁面。

## 日常迴圈 {#daily-loop}

| 指令 | 用途 |
|---|---|
| `faber check <package>` | 快速前端驗證：詞法分析、語法分析、型別檢查、降層 |
| `faber build <package> -t rust` | 產生 Rust 專案以供審閱或原生編譯 |
| `faber run <package>` | 建置並執行應用程式套件 |
| `faber test <package>` | 當套件定義測試介面時執行套件測試 |
| `faber explain <code>` | 閱讀穩定的診斷說明 |

從 `check` 開始。這是最便宜的指令，代理在將生成的程式碼提議為有效 Faber 之前應先執行它。

## 檢查 {#check}

<<<FENCE 0>>>

通過檢查表示該套件在語法與語意上可被編譯器前端接受。這並不表示最終的原生工具鏈已被調用。

## 建置 {#build}

<<<FENCE 1>>>

Rust 目標刻意設計為可審閱。生成的 Rust 是編譯器產出物，而非事實來源；應編輯 Faber 套件並重新建置，而非手動修補產出的 Rust。

## 執行 {#run}

<<<FENCE 2>>>

對具有 `incipit` 進入點的應用程式套件使用 `run`。純函式庫套件應改為檢查與測試。

## 診斷說明 {#explain}

<<<FENCE 3>>>

診斷系列是穩定的識別碼：`LEX` 表示詞法錯誤、`PAR` 表示語法分析錯誤、`SEM` 表示語意／型別錯誤。在文件與代理報告中，應引用診斷代碼，而非含糊地轉述編譯器失敗。

## 讀者地區指令 {#reader-locale}

<<<FENCE 4>>>

讀者地區輸出是編譯器語意模型的呈現，而非瀏覽器端的翻譯層。地區化工作應在套件以規範形式通過檢查後進行。

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [Hello, Faber](/start/hello.html) | [專案與範例](/start/projects.html) |
