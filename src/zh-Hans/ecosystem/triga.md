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
Triga 是一个可选的公共源代码库，提供几何、场景以及面向 GPU 的类型契约。在常规项目中，请在 `faber.toml` 中将 Triga 声明为 Cista 包依赖；Cista 会将解析后的源代码记录到 `faber.lock`，并由编译器从包存储中解析它。

`FABER_LIBRARY_HOME` 是一个解析器覆盖项，仅在被设置时用于本地开发。它不是使用 Triga 的主要产品路径。

Triga 提供以下类型与操作：

- 几何基元（点、向量、矩阵、变换）
- 场景图结构
- 与 Faber 系统通道对齐的面向 GPU 的类型契约

Triga 不是 Norma 的一部分。它是一个可选依赖，仅当包需要图形或几何相关工作时才选择引入。
