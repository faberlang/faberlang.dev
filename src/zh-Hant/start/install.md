+++
translation_kind = "translated"


title = "Install and download"
section = "install"
order = 1
sources = []


prose_hash = "sha256:662becbb3dd5349058bcdfec9219fd07f6fe4217c2e5115c0aade45e0f17f0d4"
code_hash = "sha256:cc9de43077b1262ee3d9edfbd3bd56c4ae51bcca18d0316fa0bb95312f3033b7"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
從目前的預建版本中安裝 **Faber** CLI。編譯器前端已包含在 `faber` 二進位檔中；一般套件工作不需要另外安裝 Radix。

本頁以 Faber 1.2.0 的儲存庫版本發行成品為準。套件管理器的公式可能落後於儲存庫版本；如果 Homebrew 或其他管理器回報較舊的 Radix/Faber 版本，請在此安裝流程中優先使用下方的壓縮檔。

## 目前版本 {#current-release}

| 欄位 | 值 |
|---|---|
| **版本** | 1.2.0 |
| **標籤** | `faber-v1.2.0` |
| **發行頁面** | [GitHub 上的 faber-v1.2.0](https://github.com/faberlang/releases/releases/tag/faber-v1.2.0) |
| **所有版本** | [網站版本發行清單](/history/releases.html) |
| **授權條款** | MIT |

## 預建壓縮檔 {#archives}

| 平台 | 下載 | SHA-256 |
|---|---|---|
| **macOS arm64**（Apple Silicon） | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-aarch64-apple-darwin.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64**（glibc） | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-x86_64-unknown-linux-gnu.tar.gz) | [checksum](https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

壓縮檔會解壓縮至 `faber-v1.2.0-<target-triple>/faber`。checksum 檔案可能會列出原始建置路徑，因此請將第一個雜湊欄位與本機壓縮檔比對來驗證，不要依賴 `sha256sum -c` 的路徑比對。

### macOS arm64 {#macos}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
# place on PATH, e.g.:
sudo mv faber-v1.2.0-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

### Linux x64 {#linux}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.2.0-x86_64-unknown-linux-gnu/faber /usr/local/bin/
faber --version
```

## 驗證 {#verify}

```bash
faber --version
faber explain SEM001
```

你應該會看到 CLI 的版本列和診斷說明。如果找不到 `faber`，請確認包含該二進位檔的目錄已在 `PATH` 中。

## 第一次套件檢查 {#first-package}

將 CLI 加入 `PATH` 後，複製公開範例（或任何 Faber 套件）並執行型別檢查。產品套件會透過 `faber.lock` 從 Cista 儲存區解析相依性；本機原始碼 checkout 僅用於明確指定的函式庫開發覆寫。

```bash
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

更多套件：[範例](/start/examples.html)。CLI 介面：
[Faber 建置工具](/tooling/faber-build-tool.html)。

## Homebrew 狀態 {#homebrew}

Homebrew 的發佈目前尚未成為此安裝流程的依據。如果某個公式提供較舊的編譯器，例如 Radix 0.38.0，而本網站記錄的是 Faber 1.2.0，請將該公式視為落後版本，並使用預建版本壓縮檔。本頁的容器驗證閘門仍處於待完成狀態，直到公式發佈追上版本為止。

## 從原始碼建置 {#from-source}

預建版本是代理程式與大多數開發者的建議路徑。從原始碼建置需要私有的 Radix 編譯器樹，超出本頁範圍。除非你正在開發編譯器本身，否則請優先使用上述壓縮檔。

## 代理程式路徑 {#agent-path}

代理程式應載入 **install** skill 與代理程式索引，而不是擷取此 HTML：

- [`/llms.txt`](/llms.txt)
- [install skill](/.well-known/agent-skills/install/SKILL.md)
- [代理程式指南](/agents/index.md)

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [快速導覽](/start/) | [Hello, Faber](/start/hello.html) |
