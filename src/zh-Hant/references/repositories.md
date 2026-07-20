+++
translation_kind = "translated"

title = "Repositories"
section = "references"
order = 3
sources = [
  "github.com/faberlang",
]


prose_hash = "sha256:1f00ec1ce77844348776b258be2b9246bf876b614a2849a0e8dcbb54a8dc82f0"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
Faber 由 `faberlang` 組織旗下的多個儲存庫共同開發。

## 公開儲存庫 {#public-repositories}

| 儲存庫 | 說明 |
|-----------|-------------|
| `faber` | 面向使用者的 CLI：check、build、run、test、format、explain |
| `faber-runtime` | 核心執行階段型別（Valor、張量、框架）；crate 名稱為 `faber` |
| `norma` | 標準函式庫原始碼（`norma:*` 模組） |
| `triga` | 選用的圖形／幾何函式庫 |
| `cista` | 套件管理員與儲存庫（實驗性） |
| `examples` | 語言語料庫、coreutils、AI Workbench、讀者語系套件 |
| `faberlang.dev` | 本網站 |

## 私有儲存庫 {#private-repositories}

| 儲存庫 | 說明 |
|-----------|-------------|
| `radix` | 編譯器：詞法分析、剖析、語意分析、HIR/MIR/AIR、診斷、程式碼生成 |

## 主機平台儲存庫 {#host-platform-repositories}

| 儲存庫 | 說明 |
|-----------|-------------|
| `host-kernel-rs` | 輕量路由器：Frame、Conversation、前綴分派、結構化錯誤 |
| `host-native-rs` | 原生掛接：工作執行緒、`register_providers` 掛鉤 |
| `host-providers-rs` | 提供者實作：solum、processus、consolum、tempus、aleator、http |
