五分鐘掌握 Faber 的樣貌：安裝 CLI、閱讀一個函式，再開啟一個真實套件。若要按順序學習，請依循：[安裝](/start/install.html) →
[Hello](/start/hello.html) →
[指令](/start/commands.html) →
[專案](/start/projects.html)。

## 1. 安裝 CLI {#install}

從[安裝頁面](/start/install.html)下載您平臺適用的最新發行版本（**1.1.1**），驗證壓縮檔的檢查碼，並將解壓縮後的 `faber-v1.1.1-<target-triple>/faber` 二進位檔放到您的 `PATH` 中。確認：

<<<FENCE 0>>>

## 2. 函式的樣貌 {#shape}

型別在前的參數、符號回傳型別、拉丁文控制字詞、可空聯集：

<<<FENCE 1>>>

| 訊號 | 意義 |
|---|---|
| `functio` | 函式宣告 |
| `numerus a` | 先型別，後名稱 |
| `→` | 回傳型別 |
| `∪ nihil` | 可空（`T ∪ nihil`） |
| `si … ∴` | 精簡分支 |
| `redde` | 回傳 |

## 3. 套件版面 {#package}

套件是一個帶有 `faber.toml` 與 `src/` 的目錄：

<<<FENCE 2>>>

常用指令：

<<<FENCE 3>>>

詳見：[Faber 建置工具](/tooling/faber-build-tool.html)。

## 4. 真實應用 {#applications}

不要停留在 hello-world。公開的 **examples** 儲存庫收錄了多指令的 CLI、本地端郵件空間、GPU 工作負載軌道，以及完整的語言語料庫。

| 套件 | 展示內容 |
|---|---|
| AI Workbench | 多指令 CLI、模型檢視、嵌入 |
| ViviLite | 以檔案為本的郵件空間／代理協調 CLI |
| coreutils | 較大型的應用程式活動（一致性測試架構） |
| gpu-workload | 系統／GPU 階梯 |
| corpus | 每個語言構造一個目錄 |

請至 [範例頁面](/start/examples.html) 瀏覽它們。

## 5. 若您是代理 {#agents}

1. 閱讀 [`/llms.txt`](/llms.txt)。
2. 開啟 [`/agents/index.md`](/agents/index.md)。
3. 從 [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json) 中挑選一項技能。

## 起步軌道 {#start-track}

| 步驟 | 頁面 | 成果 |
|---|---|---|
| 1 | [安裝與下載](/start/install.html) | 將 Faber 1.1.1 放到 `PATH` 並驗證 |
| 2 | [Hello, Faber](/start/hello.html) | 建立並執行 `salve-munde` |
| 3 | [您會用到的指令](/start/commands.html) | 學習 `check`、`build`、`run`、`test`、`explain` |
| 4 | [專案與範例](/start/projects.html) | 進入真實套件與語料庫頁面 |

## 下一步 {#next}

| 主題 | 連結 |
|---|---|
| 安裝與下載 | [安裝](/start/install.html) |
| Hello, Faber | [Hello](/start/hello.html) |
| 指令 | [指令](/start/commands.html) |
| 專案 | [專案](/start/projects.html) |
| 語法參考 | [語法](/syntax/) |
| 功能（在地化、軌道） | [功能](/features/) |
| 生態系函式庫 | [生態系](/ecosystem/) |
| 關鍵字語料庫 | [語料庫](/corpus/) |
