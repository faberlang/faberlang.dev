+++
translation_kind = "translated"

title = "Triga graphics library"
section = "ecosystem"
order = 2
sources = [
  "sibling triga/ repository",
  "radix/README.md (mentions triga)",
]


prose_hash = "sha256:d2d83d9401309c449bba9b993db7ec74cdb97afc4e8cc1b2195e769c043f07a1"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Triga 是一個可選的公開原始碼函式庫，提供幾何、場景與面向 GPU 的型別契約。在一般專案中，請在 `faber.toml` 將 Triga 宣告為 Cista 套件相依項目；Cista 會將解析後的原始碼記錄在 `faber.lock` 中，而編譯器會從套件儲存區解析它。

設定 `FABER_LIBRARY_HOME` 時，它會覆寫本機開發所用的解析器。它不是使用 Triga 的主要產品路徑。

Triga 提供以下型別與操作：

- 幾何基本元件（點、向量、矩陣、轉換）
- 場景圖結構
- 與 Faber 系統層對齊、面向 GPU 的型別契約

Triga 不屬於 Norma。它是一個可選相依項目，套件只有在需要圖形或幾何處理時才會選擇加入。
