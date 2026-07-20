五分鐘掌握 Faber 的輪廓：安裝 CLI、閱讀一個函式，然後開啟一個真實套件。若需要循序路徑，請依序閱讀：[安裝](/start/install.html) →
[Hello](/start/hello.html) → [命令](/start/commands.html) →
[專案](/start/projects.html)。

## 1. 安裝 CLI {#install}

從[安裝頁面](/start/install.html)下載您平臺的目前發行版（**1.1.1**），驗證壓縮檔的校驗碼，然後將解壓出的 `faber-v1.1.1-<target-triple>/faber` 二進位檔放到 `PATH` 上。確認：

<<<FENCE 0>>>

## 2. 函式的輪廓 {#shape}

型別優先的參數、符號回傳型別、拉丁控制字、可空聯集：

<<<FENCE 1>>>

| 記號 | 含義 |
|---|---|
| `functio` | 函式宣告 |
| `numerus a` | 型別在前，名稱在後 |
| `→` | 回傳型別 |
| `∪ nihil` | 可空（`T ∪ nihil`） |
| `si … ∴` | 緊湊分支 |
| `redde` | 回傳 |

## 3. 套件佈局 {#package}

套件是一個包含 `faber.toml` 與 `src/` 的目錄：

<<<FENCE 2>>>

常用命令：

<<<FENCE 3>>>

詳情請見：[Faber 建置工具](/tooling/faber-build-tool.html)。

## 4. 真實應用程式 {#applications}

不要停在 hello-world。公開的 **examples** 儲存庫包含多命令 CLI、本地郵件空間、GPU 工作負載追蹤，以及完整的語言語料庫。

| 套件 | 展示內容 |
|---|---|
| AI Workbench | 多命令 CLI、模型檢查、嵌入 |
| ViviLite | 檔案支援的郵件空間／代理協調 CLI |
| coreutils | 較大型的應用程式活動（對等測試框架） |
| gpu-workload | 系統／GPU 層級 |
| corpus | 每個語言結構一個目錄 |

在[範例頁面](/start/examples.html)瀏覽這些套件。

## 5. 若您是代理 {#agents}

1. 閱讀 [`/llms.txt`](/llms.txt)。
2. 開啟 [`/agents/index.md`](/agents/index.md)。
3. 從 [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json) 選擇一項技能。

## 起始軌道 {#start-track}

| 步驟 | 頁面 | 成果 |
|---|---|---|
| 1 | [安裝與下載](/start/install.html) | 將 Faber 1.1.1 放到 `PATH` 上並驗證 |
| 2 | [Hello, Faber](/start/hello.html) | 建立並執行 `salve-munde` |
| 3 | [你會用到的命令](/start/commands.html) | 學習 `check`、`build`、`run`、`test`、`explain` |
| 4 | [專案與範例](/start/projects.html) | 進入真實套件與語料庫頁面 |

## 下一步 {#next}

| 主題 | 連結 |
|---|---|
| 安裝與下載 | [安裝](/start/install.html) |
| Hello, Faber | [Hello](/start/hello.html) |
| 命令 | [命令](/start/commands.html) |
| 專案 | [專案](/start/projects.html) |
| 語法參考 | [語法](/syntax/) |
| 功能（區域設定、通道） | [功能](/features/) |
| 生態系程式庫 | [生態系](/ecosystem/) |
| 關鍵字語料庫 | [語料庫](/corpus/) |
