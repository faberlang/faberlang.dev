+++
translation_kind = "translated"

title = "开始"
section = "start"
order = 0
sources = []

prose_hash = "sha256:f60d676c60b081effa2dcd0f99bf2d35b5194909f1a044c77f314843f88a147d"
code_hash = "sha256:c8e5b9b166f413d5889eae20e5f130ac1ca46737609acfd20560b9daf04acaa7"
source_commit = "b463c0bad3a1a09e83efc170965bb279f2528d6d"
source_locale = "en-US"
+++
Faber 是由模型来编写的语言，所以你不必手动安装它。
把这个链接交给你的模型：

```text
https://faberlang.dev/install.md
```

你的模型会读取该文件，下载适合你机器的当前发布版本，校验其校验和，并安装 `faber` 命令。随后它会编写一个简短的 hello 程序，并对它运行 `faber check`。这一切都发生在你自己的机器上，检查通过后模型会向你报告。
