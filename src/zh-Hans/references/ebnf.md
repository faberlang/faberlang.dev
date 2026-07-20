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
Faber 的权威语法定义于 Radix 代码库中的 `radix/EBNF.md`。它是所有语言语法的正式权威。

该语法涵盖：

- 词法结构（字形、关键字、字面量、注释）
- 声明（functio、genus、implendum、typus、discretio、ordo）
- 语句（绑定、控制流、返回、迭代）
- 表达式（调用、运算符、转换、字面量）
- 注解（@ 语法）
- CLI 注解（@ cli、@ optio、@ operandus、@ imperium）
- 类型表达式（原语、泛型、糖化形式）
- 模块系统（importa）

```ebnf
(* excerpt: function declaration *)
funcDecl = 'functio' ident genericParams? '(' paramList ')' ('→' type)? ('⇥' type)? block;
block    = '{' stmt* '}';
```
