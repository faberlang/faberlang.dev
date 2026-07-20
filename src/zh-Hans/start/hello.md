+++
translation_kind = "translated"

title = "Hello, Faber"
section = "hello"
order = 2
sources = []

prose_hash = "sha256:3a78129bf3787f7c726e39104c95fe9bde78855c4a9f63650410c5cef9610067"
code_hash = "sha256:1ee50be729b09d1bfba27a1f994ef4d1a47c73a645764f9d5986c9bab1aecfb8"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
编写最小的可用 Faber 程序：一个格式化字符串并打印它的包入口点。

## 先决条件 {#prerequisites}

先完成[安装与下载](/start/install.html)。你的 `PATH` 中应当有一个 `faber` 二进制文件，并且在一个可以创建文件的工作目录中打开一个 shell。

## 创建包 {#create-package}

```bash
mkdir salve-munde
cd salve-munde
mkdir src
cat > faber.toml <<'EOF'
[package]
name = "salve-munde"
version = "0.1.0"
EOF
cat > src/main.fab <<'EOF'
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
EOF
```

## 检查它 {#check}

```bash
faber check .
```

`faber check` 运行前端：词法分析、语法分析、类型检查，以及足够深的中层降阶，以便在不构建原生二进制文件的情况下捕获普通的包错误。如果命令失败，请先阅读诊断代码；Faber 的诊断设计为稳定的搜索句柄。

## 运行它 {#run}

```bash
faber run .
```

预期输出：

```text
Salve, munde!
```

## 你刚刚用到的 {#what-you-used}

| 源码 | 含义 |
|---|---|
| `functio salve(textus nomen) → textus` | 名为 `salve` 的函数，类型在前的参数，文本返回值 |
| `fixum textus msg ← ...` | 不可变绑定 |
| `"Salve, §!"(nomen)` | 带显示插值的格式字符串 |
| `redde msg` | 返回 |
| `incipit` | 包入口点 |
| `nota m` | 打印提示/输出值 |

## 本地化证明 {#locale-proof}

上面的程序是规范的拉丁语读者渲染。读者本地化可以用不同的关键字包渲染同一个语义程序，同时保留字形和标识符。在编写非拉丁语包之前，请先阅读完整的证明：[读者本地化](/features/reader-locale.html)。

## 下一步 {#next}

| 上一页 | 下一页 |
|---|---|
| [安装与下载](/start/install.html) | [你将使用的命令](/start/commands.html) |
