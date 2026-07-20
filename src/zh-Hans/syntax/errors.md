+++
translation_kind = "translated"

title = "Error handling"
section = "syntax"
order = 5
sources = [
  "radix/README.md (Return and Error Channels)",
  "examples/corpus/iace/",
  "examples/corpus/fac/",
  "examples/corpus/cape/",
  "radix/docs/design/failable-conversio.md",
]


prose_hash = "sha256:7b9b055ee1b8fc13b23faefb29514dd947982a0f768d911767255fdc0ee9f738"
code_hash = "sha256:81aa5174263eeb0a80a64870335680dec64748cbdb7896e4de78021d8c4f197f"
source_commit = "fdc930a3f4faf54690fd6e4f1342c94dee72c954"
source_locale = "en-US"
+++
Faber 将许多语言合并为同一种形状的三个相关概念区分开来：

| 构造 | 含义 |
|-----------|---------|
| `→ T` | 正常的成功返回通道 |
| `T ∪ nihil` | 成功值域中的缺失 |
| `⇥ E` | 用于错误的可恢复备用退出通道 |

## 正常返回 {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

## 可失败函数 {#failable-functions}

当函数可以通过错误通道退出时，使用 `⇥`：

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}
```

## 抛出异常 — iace {#throwing--iace}

`iace` 在错误通道上发送一个值：

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

## 恢复 — fac / cape {#recovery--fac--cape}

调用者使用 `fac` 块和 `cape` 处理程序进行局部恢复：

```faber
functio divide(numerus a, numerus b) → numerus {
    si b ≡ 0 {
        redde 0
    }
    redde a / b
}

functio tutum(numerus a, numerus b) → numerus {
    fac {
        redde divide(a, b)
    }
    cape err {
        mone err
        redde 0
    }
}
```

直接的可失败调用不是普通表达式。请将 `→ T ⇥ E` 函数的调用放在活动的 `fac` / `cape` 边界内。

## 内联转换恢复 {#inline-conversion-recovery}

`⇥` 也可以在 `↦` 转换上指定内联恢复值：

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

## 仅效果可失败 {#effectonly-failable}

对于会出错但不返回成功值的函数，省略 `→ T`：

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

## 当前状态 {#current-status}

`→`、`redde`、`⇥`、`iace` 以及 `fac` / `cape` 是现行的语法和检查器接口。针对完整 `⇥` / `iace` / `cape` 运行时行为的 Rust 和 Go 降阶（lowering）仍存在后端缺口——这些能通过类型检查，但尚未向所有目标生成可失败的运行时代码。
