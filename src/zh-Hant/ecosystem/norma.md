+++
translation_kind = "translated"

title = "Norma standard library"
section = "ecosystem"
order = 1
sources = [
  "radix/README.md (Standard Library section)",
  "sibling norma/ repository",
  "norma/exempla/",
  "radix/docs/stdlib/morphologia.md",
]


prose_hash = "sha256:f333d0ee78b78e5ad3ebfb1bfdda0a4069a9b7daf3579d8c55d6b83c668be833"
code_hash = "sha256:0ef63774f36a5e950889dcae691b2a9c5add05fe03c89c061ba60d829195f2ff"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Norma 是 Faber 的標準函式庫。它提供以拉丁文命名的扁平模組，透過 `norma:*` 路徑存取。標準函式庫宣告是鄰近 `norma` 儲存庫中的 Faber 原始碼。

## 模組 {#modules}

| 模組 | 領域 |
|--------|--------|
| `norma:solum` | 檔案系統操作 |
| `norma:solum/path` | 純路徑名稱操作 |
| `norma:http` | HTTP 用戶端 |
| `norma:processus` | 程序執行 |
| `norma:consolum` | 主控台 I/O（標準輸入、標準輸出、標準錯誤） |
| `norma:json` | JSON 解析與序列化 |
| `norma:toml` | TOML 解析 |
| `norma:yaml` | YAML 解析 |
| `norma:valor` | 編解碼器導覽 |
| `norma:tensor` | 張量橋接輔助工具 |
| `norma:tempus` | 時間與持續時間 |
| `norma:aleator` | 隨機性 |

## Morphologia 命名慣例 {#morphologia-naming-convention}

Norma 遵循 morphologia 政策來命名所有方法。拉丁文動詞變化形式表示執行模式：

| 詞幹 | 同步 | 非同步 | 意義 |
|------|------|---------|---------|
| `leg-` | `lege` | `leget` | 讀取 |
| `scrib-` | `scribe` | `scribet` | 寫入 |
| `quaer-` | — | `quaeret` | 查詢（有限） |
| `quaer-` | — | `quaerent` | 查詢（串流） |

所有權配對（變更與複製輸出）：

| 變更 | 複製輸出 | 意義 |
|---------|----------|---------|
| `adde` | `addita` | 新增 |
| `inverte` | `inversa` | 反轉 |
| `filtra` | `filtrata` | 篩選 |

## 使用方式 {#usage}

```faber locale=la
importa ex "norma:solum" privata solum

functio legeConfig() → textus {
    redde solum.lege("config.toml")
}
```
