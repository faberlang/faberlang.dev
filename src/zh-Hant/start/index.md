+++
translation_kind = "translated"

title = "Quick tour"
section = "start"
order = 0
sources = []

prose_hash = "sha256:fb6f791ae0e9b73d0c92c2127726f558a2b845351779f80217616b8f55629ff0"
code_hash = "sha256:f9eb22ab8a2408fe0076d846dd4266cff4ded675ad8d63a5b2d9ee59c3e0156f"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
五分鐘掌握 Faber 的基本形貌：安裝 CLI、閱讀一個函式，然後開啟一個真正的套件。若要依序學習，請依循：[安裝](/start/install.html) → [Hello](/start/hello.html) → [命令](/start/commands.html) → [專案](/start/projects.html)。

## 1. 安裝 CLI {#install}

從[安裝頁面](/start/install.html)下載適用於您平台的目前版本（**1.1.1**），驗證壓縮檔校驗碼，並將解壓縮後的 `faber-v1.1.1-<target-triple>/faber` 二進位檔放入您的 `PATH`。確認：

```bash
faber --version
```

## 2. 函式的形貌 {#shape}

參數採型別優先、以字元表示回傳型別、使用拉丁文控制字詞，以及可為空的聯集：

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

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

```text
my-app/
  faber.toml
  src/
    main.fab
```

常用命令：

```bash
faber check my-app/
faber build my-app/ -t rust
faber run my-app/
faber test my-app/
```

詳細資訊請參閱：[Faber 建置工具](/tooling/faber-build-tool.html)。

## 4. 真實應用程式 {#applications}

不要停留在 hello-world。公開的 **examples** 儲存庫包含多命令 CLI、本機郵件空間、GPU 工作負載軌道，以及完整的語言語料庫。

| 套件 | 展示內容 |
|---|---|
| AI Workbench | 多命令 CLI、模型檢查、嵌入 |
| ViviLite | 以檔案為後端的郵件空間／代理協調 CLI |
| coreutils | 更大型的應用程式活動（相容性測試工具） |
| gpu-workload | 系統／GPU 階梯 |
| corpus | 每個語言結構各有一個目錄 |

請在[範例頁面](/start/examples.html)瀏覽這些內容。

## 5. 如果您是代理 {#agents}

1. 閱讀 [`/llms.txt`](/llms.txt)。
2. 開啟 [`/agents/index.md`](/agents/index.md)。
3. 從 [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json) 選擇一項技能。

## 開始學習軌道 {#start-track}

| 步驟 | 頁面 | 結果 |
|---|---|---|
| 1 | [安裝與下載](/start/install.html) | 將 Faber 1.1.1 放入 `PATH` 並完成驗證 |
| 2 | [Hello，Faber](/start/hello.html) | 建立並執行 `salve-munde` |
| 3 | [您將使用的命令](/start/commands.html) | 學習 `check`、`build`、`run`、`test`、`explain` |
| 4 | [專案與範例](/start/projects.html) | 開始使用真正的套件與語料庫頁面 |

## 接下來 {#next}

| 主題 | 連結 |
|---|---|
| 安裝與下載 | [安裝](/start/install.html) |
| Hello，Faber | [Hello](/start/hello.html) |
| 命令 | [命令](/start/commands.html) |
| 專案 | [專案](/start/projects.html) |
| 語法參考 | [語法](/syntax/) |
| 功能（地區設定、執行道） | [功能](/features/) |
| 生態系函式庫 | [生態系](/ecosystem/) |
| 關鍵字語料庫 | [語料庫](/corpus/) |
