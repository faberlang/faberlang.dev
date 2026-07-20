從目前的預編譯版本安裝 **Faber** CLI。編譯器前端已包含在 `faber` 二進位檔中；一般套件工作不需要另外安裝 Radix。

本頁以 Faber 1.1.1 的儲存庫釋出構件為依據。套件管理器的配方可能落後於儲存庫釋出版本；如果 Homebrew 或其他管理器回報較舊的 Radix/Faber 版本，請在此安裝路徑中優先使用下方的壓縮檔。

## 目前版本 {#current-release}

| 欄位 | 值 |
|---|---|
| **版本** | 1.1.1 |
| **標籤** | `faber-v1.1.1` |
| **釋出頁面** | [GitHub 上的 faber-v1.1.1](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1) |
| **所有版本** | [網站版本清單](/history/releases.html) |
| **授權條款** | MIT |

## 預編譯壓縮檔 {#archives}

| 平台 | 下載 | SHA-256 |
|---|---|---|
| **macOS arm64**（Apple Silicon） | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [檢查碼](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64**（glibc） | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [檢查碼](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

壓縮檔會解開至 `faber-v1.1.1-<target-triple>/faber`。檢查碼檔案可能會列出原始建置路徑，因此請將第一個雜湊欄位與本機壓縮檔比較，不要依賴 `sha256sum -c` 的路徑比對。

### macOS arm64 {#macos}

<<<FENCE 0>>>

### Linux x64 {#linux}

<<<FENCE 1>>>

## 驗證 {#verify}

<<<FENCE 2>>>

您應該會看到 CLI 的版本行和診斷說明。如果找不到 `faber`，請確認包含該二進位檔的目錄已加入 `PATH`。

## 第一次套件檢查 {#first-package}

將 CLI 加入 `PATH` 後，複製公開範例（或任何 Faber 套件）並執行型別檢查。產品套件會透過 `faber.lock` 從 Cista 儲存區解析相依性；本機原始碼檢出僅用於明確指定的函式庫開發覆寫。

更多套件：[範例](/start/examples.html)。CLI 介面：
[Faber 建置工具](/tooling/faber-build-tool.html)。

## Homebrew 狀態 {#homebrew}

Homebrew 發佈目前尚不是此入門路徑的權威來源。如果某個配方提供較舊的編譯器（例如 Radix 0.38.0），而本網站記錄的是 Faber 1.1.1，請將該配方視為落後版本，並使用預編譯版本壓縮檔。此頁面的容器驗證閘門在配方發佈追上之前仍屬待完成項目。

## 從原始碼建置 {#from-source}

預編譯版本是代理程式和大多數開發者的建議路徑。從原始碼建置需要私有的 Radix 編譯器樹，超出本頁範圍。除非您正在處理編譯器本身，否則請優先使用上述壓縮檔。

## 代理程式路徑 {#agent-path}

代理程式應載入 **install** 技能和代理程式索引，而不是擷取此 HTML：

- [`/llms.txt`](/llms.txt)
- [install 技能](/.well-known/agent-skills/install/SKILL.md)
- [代理程式指南](/agents/index.md)

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [快速導覽](/start/) | [Hello, Faber](/start/hello.html) |
