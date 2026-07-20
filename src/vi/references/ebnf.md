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
Ngữ pháp Faber chuẩn được định nghĩa trong kho Radix tại  
`radix/EBNF.md`. Đây là nguồn tham chiếu chính thức cho mọi cú pháp của ngôn ngữ.

Ngữ pháp bao quát:

- Cấu trúc từ vựng (glyph, từ khóa, literal, chú thích)
- Khai báo (`functio`, `genus`, `implendum`, `typus`, `discretio`, `ordo`)
- Câu lệnh (liên kết, điều khiển luồng, trả về, lặp)
- Biểu thức (lời gọi, toán tử, chuyển đổi, literal)
- Chú thích (`@` syntax)
- Chú thích CLI (`@ cli`, `@ optio`, `@ operandus`, `@ imperium`)
- Biểu thức kiểu (kiểu nguyên thủy, generic, dạng viết tắt)
- Hệ thống mô-đun (`importa`)

```ebnf
(* excerpt: function declaration *)
funcDecl = 'functio' ident genericParams? '(' paramList ')' ('→' type)? ('⇥' type)? block;
block    = '{' stmt* '}';
```
