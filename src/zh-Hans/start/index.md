+++

title = "开始"
section = "start"
order = 0
sources = []

translation_kind = "translated"

prose_hash = "sha256:fb813c0842ab3507898c97a7f766728b584ea8188cd53534db006768b83372ce"
code_hash = "sha256:4e3dec0ba47836476297e320d6822e4528d0f7edb88f02133372d6375d79adae"
source_commit = "6658dc687c30abd27b12dc4307f8ffef48170d46"
source_locale = "en-US"
+++
Faber 是由模型来编写的语言，所以你只需把一个链接交给你的模型，就能完成安装。

::agent-pass::

## 你的模型会做什么 {#what-your-model-does}

1. 读取该链接处的入口文件，它说明 Faber 是什么，以及每一步在哪里。
2. 下载适合你机器的当前发布版本，并校验其校验和。
3. 安装 `faber` 命令。
4. 编写一个简短的 hello 程序，并对它运行 `faber check`。

这一切都发生在你自己的机器上，检查通过后模型会向你报告。

## 然后请它做点什么 {#then-ask}

检查通过后，就像和同事交谈一样和你的模型说话。下面每条提示词都带有复制按钮。

让它写一个程序并解释：

```text prompt
用 Faber 写一个简短的程序，打印前十个平方数。用 faber check 检查，用 faber run 运行，然后逐行向我解释。
```

带上你已有的代码：

```text prompt
我已经有这个函数：<在此粘贴>。把它翻译成 Faber，检查它，然后用 faber build -t rust 为 Rust 构建，并告诉我有什么变化。
```

用你的语言阅读：

```text prompt
用 faber convert --to zh-Hans 生成一份用简体中文书写的 hello 程序副本。检查这份副本，然后把两个版本并排给我看。
```

看看编译器对错误怎么说：

```text prompt
故意给 hello 程序传入类型错误的值来弄坏它。运行 faber check，把诊断读给我听，并对其代码使用 faber explain，让我明白它的含义。
```

## 延伸阅读 {#read-along}

阅读 Faber 不需要会写 Faber。这些页面展示你的模型写出的内容，以及它为何是这个样子。

- [概览](/en-US/language/overview.html)：一个真实的程序、这门语言带给你的东西，以及它编译到哪里。
- [速查表](/en-US/cheatsheet/)：语言的各种形式和 `faber` 命令，每个主题一页简短内容。
- [术语 A–Z](/corpus/az.html)：每个关键字和术语，附带示例。
- [读者语言](/language/reader-locales.html)：同一个程序，八种语言表面。
