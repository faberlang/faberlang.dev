Faber 的基本輪廓，五分鐘上手：安裝 CLI、閱讀一個函式，然後開啟一個實際套件。若要依序進行，請按照：[安裝](/start/install.html) → [Hello](/start/hello.html) → [指令](/start/commands.html) → [專案](/start/projects.html)。

## 1. 安裝 CLI {#install}

從[安裝頁面](/start/install.html)下載適用於您平台的目前版本（**1.1.1**），驗證封存檔的校驗和，然後將解壓縮後的 `faber-v1.1.1-<target-triple>/faber` 二進位檔放到您的 `PATH` 上。確認：

<<<FENCE 0>>>

## 2. 函式的基本輪廓 {#shape}

參數採型別優先、使用 glyph 回傳型別、控制流程關鍵字維持拉丁文，並使用可為空的聯集型別：

<<<FENCE 1>>>

| 訊號 | 意義 |
|---|---|
| `functio` | 函式宣告 |
| `numerus a` | 先寫型別，再寫名稱 |
| `→` | 回傳型別 |
| `∪ nihil` | 可為空（`T ∪ nihil`） |
| `si … ∴` | 精簡分支 |
| `redde` | 回傳 |

## 3. 套件配置 {#package}

套件是一個包含 `faber.toml` 與 `src/` 的目錄：

<<<FENCE 2>>>

常用指令：

<<<FENCE 3>>>

詳細資訊請參閱：[Faber 建置工具](/tooling/faber-build-tool.html)。

## 4. 實際應用程式 {#applications}

不要只停留在 hello-world。公開的 **examples** 儲存庫包含多指令 CLI、本機 mailspace、GPU 工作負載軌道，以及完整的語言語料庫。

| 套件 | 展示內容 |
|---|---|
| AI Workbench | 多指令 CLI、模型檢視、嵌入 |
| ViviLite | 以檔案為後端的 mailspace／agent 協調 CLI |
| coreutils | 規模較大的應用程式活動（對等性測試架構） |
| gpu-workload | 系統／GPU 階梯 |
| corpus | 每個語言結構各有一個目錄 |

請在[examples 頁面](/start/examples.html)瀏覽這些內容。

## 5. 如果您是 agent {#agents}

1. 閱讀 [`/llms.txt`](/llms.txt)。
2. 開啟 [`/agents/index.md`](/agents/index.md)。
3. 從 [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json) 選擇一項技能。

## 開始路線 {#start-track}

| 步驟 | 頁面 | 結果 |
|---|---|---|
| 1 | [安裝與下載](/start/install.html) | 將 Faber 1.1.1 放到 `PATH` 上並驗證 |
| 2 | [Hello，Faber](/start/hello.html) | 建立並執行 `salve-munde` |
| 3 | [您會使用的指令](/start/commands.html) | 學習 `check`、`build`、`run`、`test`、`explain` |
| 4 | [專案與範例](/start/projects.html) | 進入實際套件與語料庫頁面 |

## 下一步 {#next}

| 主題 | 連結 |
|---|---|
| 安裝與下載 | [安裝](/start/install.html) |
| Hello，Faber | [Hello](/start/hello.html) |
| 指令 | [指令](/start/commands.html) |
| 專案 | [專案](/start/projects.html) |
| 語法參考 | [語法](/syntax/) |
| 功能（語系、lane） | [功能](/features/) |
| 生態系函式庫 | [生態系](/ecosystem/) |
| 關鍵字語料庫 | [語料庫](/corpus/) |
