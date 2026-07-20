+++
translation_kind = "translated"

title = "Faber"
section = ""
order = 0
sources = []

prose_hash = "sha256:e63352acf54515593d9aeccf392881d72018d55e6b21d6e1ddd5a3979bef91b8"
code_hash = "sha256:a02ba6ea46d65efd212b09e097d3240402bfe1d46f89b993e389cd53ca1a9c9e"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
**Faber** 是一種以套件為導向的程式語言，具有拉丁文行為詞彙、小型規則文法，以及以型別為先的靜態型別系統。原始碼會透過 Radix 編譯器編譯為易於審查的 Rust 與原生二進位檔。其定義性的架構特徵是：意義存在於語意核心——HIR（高階中間表示）——而不是存在於任何特定的呈現方式中。

此名稱源自拉丁文 *maker* 或 *craftsman* 一詞。編譯器名為 Radix，源自拉丁文 *root*。此語言由 Ian Zepp 開發，並以 MIT 授權條款發布。

**第一次來到這裡？** 請先閱讀[安裝與下載](/start/install.html)，然後依序執行入門路線：[Hello](/start/hello.html)、[命令](/start/commands.html) 以及[專案](/start/projects.html)。

## 下載 Faber 1.1.1 {#download}

目前版本：**Faber 1.1.1**（標籤 `faber-v1.1.1`）。提供 macOS 與 Linux 的預建 CLI 封存檔；請解壓縮 `faber-v1.1.1-<target-triple>/faber` 二進位檔，並將其放入你的 `PATH`。

| 平臺 | 封存檔 | 校驗碼 |
|---|---|---|
| **macOS arm64**（Apple Silicon） | [faber-v1.1.1-aarch64-apple-darwin.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64**（glibc） | [faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz) | [sha256](https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-x86_64-unknown-linux-gnu.tar.gz.sha256) |

快速安裝（macOS arm64 範例）：

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.1.1/faber-v1.1.1-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.1.1-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

所有版本說明與資產：[github.com/faberlang/releases · faber-v1.1.1](https://github.com/faberlang/releases/releases/tag/faber-v1.1.1)。  
逐步說明：[安裝指南](/start/install.html)。完整歷史清單：[版本](/history/releases.html)。

| | |
|---|---|
| **典範** | 以套件為導向；語意分階段 |
| **型別** | 靜態、以型別為先；可空值透過 `T ∪ nihil` 表示 |
| **字元** | `← → ∴ ≡ ∪ ⇥` |
| **設計者** | Ian Zepp |
| **首次出現** | 2025 |
| **編譯器** | Radix（Rust） |
| **路徑** | 應用程式（HIR）· 系統（MIR） |
| **主要目標** | Rust → 原生二進位檔 |
| **讀者語言環境** | 已發布 7 種（la、ar、hi、vi、th-TH、zh-Hans、zh-Hant） |
| **標準函式庫** | Norma（`norma:*`） |
| **授權條款** | MIT |

## 從這裡開始 {#start-here}

| 路徑 | 對象 | 說明 |
|---|---|---|
| [安裝](/start/install.html) | 人類 | 下載、PATH，以及第一次執行 `faber check` |
| [Hello](/start/hello.html) | 人類 | 建立並執行 `salve-munde` |
| [命令](/start/commands.html) | 人類 + 代理程式 | 日常 CLI 迴圈：check、build、run、test、explain |
| [專案](/start/projects.html) | 人類 + 代理程式 | 從 hello-world 邁向實際套件 |
| [快速導覽](/start/) | 人類 | 五分鐘了解語言形貌 |
| [範例](/start/examples.html) | 人類 + 代理程式 | 實際套件：CLI 應用程式、郵件空間、GPU、語料庫 |
| [`/llms.txt`](/llms.txt) | 代理程式 | 機器索引——如果你是模型，請從這裡開始 |
| [代理程式指南](/agents/index.md) | 代理程式 | 如何學習 Faber 並發布套件 |
| [代理程式技能](/.well-known/agent-skills/index.json) | 代理程式 | 專注的技能指南（安裝、語言、範例……） |

## 入口網站狀態 {#portal-status}

此 `/` 頁面是英文網站的 Speculum Porta：一個不含語言環境的入口點，將使用者導向安裝／入門頁面，將代理程式導向機器介面，並在不進行瀏覽器時間協商的情況下說明語言環境套件狀態。第 7 階段是部分多語言驗證，不是完整的在地化網站：只有 `th-TH`、`zh-Hans`、`zh-Hant`、`vi`、`ar` 和 `hi` 擁有已生成的入口網站／入門著作切片與已生成的語料庫頁面，而著作內容仍回退至英文。

| 語言環境 | 狀態 | 備註 |
|---|---|---|
| `la` | 標準線上網站 | 完整生成的英文／拉丁文網站 |
| `th-TH` | 第 7 階段部分驗證 | 入口網站／入門著作切片與已生成的語料庫；英文內容回退；完整著作文檔待完成 |
| `zh-Hans` | 第 7 階段部分驗證 | 入口網站／入門著作切片與已生成的語料庫；英文內容回退；完整著作文檔待完成 |
| `vi` | 第 7 階段部分驗證 | 入口網站／入門著作切片與已生成的語料庫；英文內容回退；完整著作文檔待完成 |
| `zh-Hant` | 第 7 階段部分驗證 | 入口網站／入門著作切片與已生成的語料庫；英文內容回退；完整著作文檔待完成 |
| `ar` | 第 7 階段部分驗證 | 入口網站／入門著作切片與已生成的語料庫；英文內容回退；完整著作文檔待完成 |
| `hi` | 第 7 階段部分驗證 | 入口網站／入門著作切片與已生成的語料庫；英文內容回退；完整著作文檔待完成 |

標準拉丁文中的實際範例：

```faber
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
```

請參閱[讀者語言環境](/features/reader-locale.html)，瞭解同一個語意程式如何透過泰文、簡體中文、繁體中文、阿拉伯文、印地文與越南文套件呈現。

## 概覽 {#overview}

Faber 建立於一項核心洞見之上：中間表示是真實依據，任何目標或人類語言表面都不具特權。以拉丁文關鍵字撰寫的 Faber 程式，可以透過與轉換為 Rust、Go 或 WebAssembly 相同的機制，轉換為泰文、阿拉伯文或中文關鍵字——因為 HIR 才是權威，而每個輸出都是它的一種*呈現*。

此語言刻意採用三種彼此協作的訊號選擇：

- **以型別為先的宣告**——讓形狀朝向繫結閱讀：`textus nomen`，而不是 `nomen: textus`。
- **拉丁文行為詞**——宣告、敘述與生命週期：`functio`、`genus`、`fixum`、`redde`、`si`。
- **結構字元**——值流與型別接合：`←`（繫結）、`→`（回傳型別）、`∴`（緊湊分支）、`≡`（相等）、`∪`（聯集）。

結果是具有穩定文法形狀的原始碼，可供審查、轉換與降低，而不會失去讀者對意圖的感受。

## 文件 {#documentation}

| 區段 | 說明 |
|---|---|
| [歷史](/history/) | 開發時間軸、影響與版本歷史 |
| [版本](/history/releases.html) | 最新 Faber 下載，以及每個已發布的標籤與二進位檔 |
| [功能](/features/) | 讀者語言環境、編譯路徑、拉丁文詞彙、字元系統、設計原則 |
| [語法](/syntax/) | 完整參考：型別、函式、控制流程、錯誤、泛型、集合 |
| [工具](/tooling/) | Radix 編譯器流程、Faber CLI、程式碼生成目標、腳本 |
| [生態系](/ecosystem/) | Norma、Cista、Triga、coreutils、AI Workbench、語料庫 |
| [語料庫](/corpus/) | 從公開語料庫生成的關鍵字與結構頁面 |
| [參考資料](/references/) | EBNF 文法、設計文件、儲存庫 |

## 快速範例 {#quick-example}

一個展示 Faber 關鍵模式的簡單函式——以型別為先的參數、字元回傳型別、可空值聯集，以及拉丁文控制詞：

```text
functio divide(numerus a, numerus b) → numerus ∪ nihil {
    si b ≡ 0 ergo redde nihil
    redde a / b
}
```

## 即時呈現 {#live-rendering}

上方的 divide 函式預設以拉丁文套件呈現。編譯器可以在七種讀者語言環境中呈現相同的程式——泰文、簡體中文、繁體中文、阿拉伯文、印地文、越南文——每一種都會將關鍵字與型別重新對應至該語言，而字元與識別碼保持不變。這不是套用在頁面上的翻譯層；這就是編譯器用來產生在地化原始碼的相同機制。

請參閱[讀者語言環境](/features/reader-locale.html)文件，以取得完整說明。

## 儲存庫 {#repositories}

| 儲存庫 | 角色 |
|---|---|
| [faberlang/faber](https://github.com/faberlang/faber) | 公開使用者 CLI |
| [faberlang/releases](https://github.com/faberlang/releases) | 已標記的 CLI 發布資產 |
| [faberlang/faber-runtime](https://github.com/faberlang/faber-runtime) | 生成 Rust 的執行階段型別 |
| [faberlang/norma](https://github.com/faberlang/norma) | 標準函式庫原始碼 |
| [faberlang/cista](https://github.com/faberlang/cista) | 套件儲存 CLI／函式庫 |
| [faberlang/triga](https://github.com/faberlang/triga) | 圖形／幾何函式庫 |
| [faberlang/examples](https://github.com/faberlang/examples) | 語料庫、路線、應用程式套件 |
| [faberlang/faberlang.dev](https://github.com/faberlang/faberlang.dev) | 此文件網站 |
