+++
translation_kind = "translated"

title = "Commands you will use"
section = "commands"
order = 3
sources = []

prose_hash = "sha256:0e56e02cfc5bc616178712a8ff6e3d914b95257913dbd22db2e8e8aac3c0e72e"
code_hash = "sha256:adf615632f084c7edf7f1f0dfc205ee4912e8b497b19c9c96167bf9b97e443cc"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
這一頁是 Faber 第一週工作的實用 CLI 對照表。請先將它作為指令索引；需要旗標與編譯器管線詳細資訊時，再開啟[ Faber 建置工具](/tooling/faber-build-tool.html)頁面。

## 每日循環 {#daily-loop}

| 指令 | 用途 |
|---|---|
| `faber check <package>` | 快速前端驗證：詞法分析、剖析、型別檢查、降階 |
| `faber build <package> -t rust` | 輸出 Rust 專案，以供審查或原生編譯 |
| `faber run <package>` | 建置並執行應用程式套件 |
| `faber test <package>` | 在套件定義測試介面時執行套件測試 |
| `faber explain <code>` | 閱讀穩定的診斷說明 |

請從 `check` 開始。這是成本最低的指令，也是代理程式在提出產生的程式碼可視為有效 Faber 之前應執行的指令。

## Check {#check}

```bash
faber check .
faber check examples/ai-workbench/packages/faber-ai
```

通過檢查表示該套件在編譯器前端中符合語法與語意要求。這不表示已叫用最終的原生工具鏈。

## Build {#build}

```bash
faber build . -t rust
```

Rust 目標刻意保持可審查。產生的 Rust 是編譯器產物，不是唯一真實來源；請編輯 Faber 套件並重新建置，而不要手動修補輸出的 Rust。

## Run {#run}

```bash
faber run .
```

對於具有 `incipit` 進入點的應用程式套件，請使用 `run`。僅含函式庫的套件則應改為檢查與測試。

## Explain diagnostics {#explain}

```bash
faber explain SEM001
faber explain LEX006
```

診斷家族是穩定的識別代號：`LEX` 代表詞法錯誤，`PAR` 代表剖析器錯誤，`SEM` 代表語意／型別錯誤。在文件與代理程式報告中，請引用診斷代碼，而不要寬泛地改述編譯器失敗。

## Reader-locale commands {#reader-locale}

```bash
faber format --reader-locale=la path/to/file.fab
faber format --reader-locale=th-TH path/to/file.fab
faber emit -t faber --reader-locale=zh-Hans path/to/file.fab
```

讀者地區設定輸出是編譯器語意模型的呈現，不是瀏覽器執行時的翻譯層。地區設定工作應在套件以規範形式通過檢查後進行。

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [Hello, Faber](/start/hello.html) | [專案與範例](/start/projects.html) |
