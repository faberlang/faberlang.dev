+++
translation_kind = "translated"

title = "Features"
section = "features"
order = 0
sources = []


prose_hash = "sha256:0a03c7c3429c7d92ec8f04a7f7ae92836e796fb82390834981ba707d1544c818"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "5caceea2571f6b2e9fc8ab9831fe8a5622d6397b"
source_locale = "en-US"
+++
Faber 的设计建立在三个标志性选择之上：类型在前的声明、拉丁语行为词汇，以及结构性字形。这些特性相互叠加——每一项都强化其余，使源码既可读、可检查，又能跨执行通道移植。

## 读者语言区域 {#reader-locale}

编译器即翻译器。读者语言区域包让同一份源码在不改变语义的前提下，以多种自然语言呈现。[了解更多 →](/features/reader-locale.html)

## 编译通道 {#compilation-lanes}

Faber 通过三层中间表示（HIR、MIR、AIR）下沉到多个目标后端，包括 Rust 运行时、WASM、TypeScript、Go 以及 GPU/WGSL。[了解更多 →](/features/compilation-lanes.html)

## 拉丁词汇与字形 {#latin-and-glyphs}

类型先于名称。拉丁词汇承载行为。结构性字形承载值流与类型形态。最终呈现的是意图，而非机制。[了解更多 →](/features/latin-and-glyphs.html)

## 九诫 {#commandments}

九条设计法则统辖着每一项语言决策，从关键字选取到错误处理。它们也是新特性的评审标准。[了解更多 →](/features/commandments.html)

## 规范形式与语法糖 {#canonical-vs-sugar}

每一种语法糖界面都有其规范展开形式。格式化工具可在二者之间转换。语法糖是便利，规范形式才是契约。[了解更多 →](/features/canonical-vs-sugar.html)

## 能力调用与帧 {#frames}

`ad` 原语提供基于能力的分派。帧类型定义了 Faber 代码与宿主提供者之间的 I/O 边界。[了解更多 →](/features/frames.html)

## 内联测试 {#testing}

测试套件与源码并存，使用三个关键字：`probandum`、`proba` 与 `adfirma`。无需单独的测试二进制文件。[了解更多 →](/features/testing.html)
