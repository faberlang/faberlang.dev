+++
translation_kind = "translated"

title = "EBNF grammar"
section = "references"
order = 1
sources = [
  "radix/EBNF.md",
]


prose_hash = "sha256:901fe46feace9eaea92780fc259f6ae17c168dba45fe1ff9c0ee95e8c4858ea2"
code_hash = "sha256:4f0d91b053057a4ac78a57bb7ecb6914b647b3bd8c5855e3696e48f2c32fc265"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
Faber 的正規文法定義於 Radix 儲存庫中的
`radix/EBNF.md`。
它是所有語言語法的正式依據。

此文法涵蓋：

- 詞法結構（字形、關鍵字、字面值、註解）
- 宣告（`functio`、`genus`、`implendum`、`typus`、`discretio`、`ordo`）
- 陳述式（繫結、控制流程、回傳、迭代）
- 運算式（呼叫、運算子、轉換、字面值）
- 註記（`@` 語法）
- CLI 註記（`@ cli`、`@ optio`、`@ operandus`、`@ imperium`）
- 型別運算式（原始型別、泛型、語法糖形式）
- 模組系統（`importa`）

```ebnf
(* excerpt: function declaration *)
funcDecl = 'functio' ident genericParams? '(' paramList ')' ('→' type)? ('⇥' type)? block;
block    = '{' stmt* '}';
```
