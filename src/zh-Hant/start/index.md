+++

title = "開始"
section = "start"
order = 0
sources = []

translation_kind = "translated"

prose_hash = "sha256:fb813c0842ab3507898c97a7f766728b584ea8188cd53534db006768b83372ce"
code_hash = "sha256:4e3dec0ba47836476297e320d6822e4528d0f7edb88f02133372d6375d79adae"
source_commit = "6658dc687c30abd27b12dc4307f8ffef48170d46"
source_locale = "en-US"
+++
Faber 是由模型來撰寫的語言，所以你只需把一個連結交給你的模型，就能完成安裝。

::agent-pass::

## 你的模型會做什麼 {#what-your-model-does}

1. 讀取該連結處的入口檔案，它說明 Faber 是什麼，以及每一步在哪裡。
2. 下載適合你機器的目前發行版本，並驗證其檢查碼。
3. 安裝 `faber` 指令。
4. 撰寫一個簡短的 hello 程式，並對它執行 `faber check`。

這一切都發生在你自己的機器上，檢查通過後模型會向你回報。

## 然後請它做點什麼 {#then-ask}

檢查通過後，就像和同事交談一樣和你的模型說話。下面每則提示詞都附有複製按鈕。

讓它寫一個程式並加以解釋：

```text prompt
用 Faber 寫一個簡短的程式，印出前十個平方數。用 faber check 檢查，用 faber run 執行，然後逐行向我解釋。
```

帶上你已有的程式碼：

```text prompt
我已經有這個函式：<在此貼上>。把它翻譯成 Faber，檢查它，然後用 faber build -t rust 為 Rust 建置，並告訴我有什麼變化。
```

用你的語言閱讀：

```text prompt
用 faber convert --to zh-Hant 產生一份以繁體中文書寫的 hello 程式副本。檢查這份副本，然後把兩個版本並排給我看。
```

看看編譯器對錯誤怎麼說：

```text prompt
故意給 hello 程式傳入型別錯誤的值來弄壞它。執行 faber check，把診斷唸給我聽，並對其代碼使用 faber explain，讓我明白它的意思。
```

## 延伸閱讀 {#read-along}

閱讀 Faber 不需要會寫 Faber。這些頁面展示你的模型寫出的內容，以及它為何是這個樣子。

- [概覽](/en-US/language/overview.html)：一個真實的程式、這門語言帶給你的東西，以及它編譯到哪裡。
- [速查表](/en-US/cheatsheet/)：語言的各種形式和 `faber` 指令，每個主題一頁簡短內容。
- [術語 A–Z](/corpus/az.html)：每個關鍵字和術語，附帶範例。
- [讀者語言](/language/reader-locales.html)：同一個程式，八種語言表面。
