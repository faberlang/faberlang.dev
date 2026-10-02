+++
translation_kind = "translated"

title = "開始"
section = "start"
order = 0
sources = []

prose_hash = "sha256:f60d676c60b081effa2dcd0f99bf2d35b5194909f1a044c77f314843f88a147d"
code_hash = "sha256:c8e5b9b166f413d5889eae20e5f130ac1ca46737609acfd20560b9daf04acaa7"
source_commit = "b463c0bad3a1a09e83efc170965bb279f2528d6d"
source_locale = "en-US"
+++
Faber 是由模型來撰寫的語言，所以你不必手動安裝它。
把這個連結交給你的模型：

```text
https://faberlang.dev/install.md
```

你的模型會讀取該檔案，下載適合你機器的目前發行版本，驗證其檢查碼，並安裝 `faber` 指令。接著它會撰寫一個簡短的 hello 程式，並對它執行 `faber check`。這一切都發生在你自己的機器上，檢查通過後模型會向你回報。
