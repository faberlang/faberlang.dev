+++
translation_kind = "translated"

title = "Errors and testing"
section = "language"
order = 4
sources = [
  "radix/README.md (Return and Error Channels)",
  "examples/corpus/iace/",
  "examples/corpus/fac/",
  "examples/corpus/cape/",
  "radix/docs/design/failable-conversio.md",
]
+++

## Error handling

Faber 将许多语言合并为同一种形状的三个相关概念区分开来：

| 构造 | 含义 |
|-----------|---------|
| `→ T` | 正常的成功返回通道 |
| `T ∪ nihil` | 成功值域中的缺失 |
| `⇥ E` | 用于错误的可恢复备用退出通道 |

### 正常返回 {#normal-return}

```faber
functio porta(numerus x) → numerus {
    si x < 0 ergo redde 0
    redde x * 2
}
```

### 可失败函数 {#failable-functions}

当函数可以通过错误通道退出时，使用 `⇥`：

```faber
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}
```

### 抛出异常 — iace {#throwing--iace}

`iace` 在错误通道上发送一个值：

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

### 恢复 — fac / cape {#recovery--fac--cape}

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

### 内联转换恢复 {#inline-conversion-recovery}

`⇥` 也可以在 `↦` 转换上指定内联恢复值：

```faber
fixum textus raw ← "42"
fixum _ n ← raw ↦ numerus ⇥ 0
```

### 仅效果可失败 {#effectonly-failable}

对于会出错但不返回成功值的函数，省略 `→ T`：

```faber
functio exigePositivum(numerus value) ⇥ textus {
    si value < 0 ergo iace "negative value"
}
```

### 当前状态 {#current-status}

`→`、`redde`、`⇥`、`iace` 以及 `fac` / `cape` 是现行的语法和检查器接口。针对完整 `⇥` / `iace` / `cape` 运行时行为的 Rust 和 Go 降阶（lowering）仍存在后端缺口——这些能通过类型检查，但尚未向所有目标生成可失败的运行时代码。

## Inline testing

Faber 在语言层面内置了一流测试框架，包含三个关键字：`probandum` 声明测试套件，`proba` 声明单个测试用例，`adfirma` 断言某个条件。测试与被测代码位于同一文件中，通过 `faber test` 运行，并支持与生产代码相同的编译流水线 —— 具备区域感知能力、类型检查和多目标支持。

### 三个关键字 {#keywords}

| 关键字 | 角色 | 近似等价物 |
|---------|------|------------------------|
| `probandum` | 声明具名测试套件 | `describe`, `#[cfg(test)] mod` |
| `proba` | 声明单个测试用例 | `it`, `#[test]` |
| `adfirma` | 在运行时断言某个条件 | `assert!`, `assert_eq!` |

#### probandum —— 测试套件 {#probandum-test-suite}

`probandum` 块对相关测试用例进行分组。套件可以嵌套，以层级方式组织测试：

```faber
probandum "arithmetica" {
    proba "unum plus unum" {
        adfirma 1 + 1 ≡ 2
    }

    proba "multiplicatio" {
        adfirma 3 * 4 ≡ 12
    }

    probandum "implicata" {
        proba "comparatio" {
            fixum _ x ← 10
            adfirma x ≥ 10
        }
    }
}
```

#### proba —— 测试用例 {#proba-test-case}

`proba` 块包含测试逻辑。它可以使用任意 Faber 代码 —— 变量绑定、函数调用、控制流 —— 并以一个或多个 `adfirma` 断言结束。测试可以通过可选的 `tag` 标记打标签，以便选择性执行：

```text
proba "echo formats operands with one space" tag "coreutils" {
    adfirma echo_textus(["hello", "world"]) ≡ "hello world"
}
```

#### adfirma —— 断言 {#adfirma-assertion}

`adfirma` 对一个布尔表达式求值，若为假则报告失败。可选的消息字符串在失败时提供上下文：

```faber
incipit {
    fixum _ x ← 10

    # Simple assertion
    adfirma x > 0

    # With custom message
    adfirma x ≡ 10 secus "x decem esse debet"

    # Multiple assertions in sequence
    fixum _ nomen ← "Marcus"
    adfirma nomen ≡ "Marcus"
    adfirma nomen ≠ "" secus "nomen vacuum non sit"
}
```

### 工作流 {#workflow}

测试通过 `faber test` 命令运行：

```text
faber test                        # run all tests in the current package
faber test examples/coreutils/packages/echo  # run tests for a specific package
```

由于测试与源代码位于同一个 `.fab` 文件中，因此没有独立的测试目录结构，没有测试模块声明，构建脚本在测试构建与生产构建之间也没有区别。编译器通过所用关键字来区分哪些块是测试代码、哪些是生产代码 —— `probandum` 和 `proba` 会被解析，但从生产构建中排除。

### 实战示例 {#real-world}

coreutils 的 `echo` 包在实践中展示了该测试框架的用法。测试与实现位于同一文件中，涵盖选项解析、转义扩展和边界情况：

```text
probandum "echo formatting" tag "coreutils" {
    proba "empty operands format as empty text" {
        fixum lista<textus> words ← vacua
        adfirma echo_textus(words) ≡ ""
    }

    proba "single operand is unchanged" {
        adfirma echo_textus(["hello"]) ≡ "hello"
    }

    proba "-E is a leading no-op option" {
        adfirma echo_textus(["-E", "hello", "world"]) ≡ "hello world"
    }

    proba "-n suppresses the trailing newline flag" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }

    proba "-e expands the declared escape subset" {
        adfirma echo_textus(["-e", "a\\nb"]) ≡ "a\nb"
        adfirma echo_textus(["-e", "a\\tb"]) ≡ "a\tb"
    }
}
```

### 设计说明 {#design}

若干设计选择使 Faber 的测试框架区别于传统方法：

- **无独立测试二进制文件。** 测试是同一源文件中的声明，而非独立的编译目标。编译器将测试块从生产输出中过滤掉。
- **以标签代替目录。** 测试通过 `tag` 标记而非目录结构来组织。一个测试可以属于多个组织维度，而无需被移动。
- **完整编译流水线。** 测试经过类型检查、分析，并具备区域感知能力 —— 同一个 `--reader-locale` 标志也适用于测试输出。
- **多目标。** 测试通过包所面向的任意后端运行 —— `faber test --interpret` 使用 MIR 步进器，`faber test` 使用编译后的 Rust。
- **嵌套套件。** `probandum` 块可以嵌套，镜像被测代码的结构。

### 参考 {#references}

1. `examples/corpus/probandum/` —— probandum 示例文件
2. `examples/corpus/proba/` —— proba 示例文件
3. `examples/corpus/adfirma/` —— adfirma 示例文件
4. `examples/coreutils/packages/echo/src/main.fab` —— 带标签的实战用法
