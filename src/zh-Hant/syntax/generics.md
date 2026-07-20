+++
translation_kind = "translated"

title = "Generics"
section = "syntax"
order = 6
sources = [
  "radix/README.md (Type and Size Generics)",
  "examples/corpus/generic/",
  "examples/corpus/functio/generic-call-type-args.fab",
]


prose_hash = "sha256:9990cc03d072c0d67d45921582a38a850892a5fa65749ddcdbf419bd888c2db5"
code_hash = "sha256:81cc82cec9db7250893ad221ed6f2f50742a7e1280993bec2a774b12447404ec"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
函式、型別別名、`genus` 與 `implendum` 接受使用 `<T>` 語法的型別參數。

## 泛型函式 {#generic-functions}

```faber
functio identitas<T>(T valor) → T {
    redde valor
}

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde res.primus()
}
```

## 明確的呼叫點型別引數 {#explicit-callsite-type-arguments}

```faber
functio identitas<T>(T valor) → T { redde valor }

functio primum<T>(lista<T> res) → T ∪ nihil {
    redde nihil
}

fixum _ value ← identitas<numerus>(7)
fixum _ maybe ← primum<numerus>([value])
```

## 泛型 `genus` {#generic-genus}

```faber
genus Par<T> {
    T primus
    T secundus
}
```

## 大小參數 {#size-parameters}

`magnitudo` 會在泛型參數列表中宣告大小／索引參數：

```faber
functio crea<T, magnitudo N>() → tensor<T, [N]> {
    redde vacua
}
```
