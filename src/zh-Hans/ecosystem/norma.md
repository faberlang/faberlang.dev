+++
translation_kind = "translated"

title = "Norma standard library"
section = "ecosystem"
order = 1
sources = [
  "radix/README.md (Standard Library section)",
  "sibling norma/ repository",
  "norma/exempla/",
  "radix/docs/stdlib/morphologia.md",
]


prose_hash = "sha256:f333d0ee78b78e5ad3ebfb1bfdda0a4069a9b7daf3579d8c55d6b83c668be833"
code_hash = "sha256:0ef63774f36a5e950889dcae691b2a9c5add05fe03c89c061ba60d829195f2ff"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Norma 是 Faber 的标准库。它通过 `norma:*` 路径提供扁平的拉丁命名模块。标准库声明是位于同级 `norma` 仓库中的 Faber 源代码。

## 模块 {#modules}

| 模块 | 领域 |
|--------|--------|
| `norma:solum` | 文件系统操作 |
| `norma:solum/path` | 纯路径名操作 |
| `norma:http` | HTTP 客户端 |
| `norma:processus` | 进程执行 |
| `norma:consolum` | 控制台 I/O（stdin、stdout、stderr） |
| `norma:json` | JSON 解析与序列化 |
| `norma:toml` | TOML 解析 |
| `norma:yaml` | YAML 解析 |
| `norma:valor` | 编解码器导航 |
| `norma:tensor` | 张量桥接助手 |
| `norma:tempus` | 时间与时长 |
| `norma:aleator` | 随机数 |

## Morphologia 命名约定 {#morphologia-naming-convention}

Norma 的所有方法名都遵循 morphologia 策略。拉丁语动词变位承载执行模式：

| 词干 | 同步 | 异步 | 含义 |
|------|------|-------|---------|
| `leg-` | `lege` | `leget` | 读取 |
| `scrib-` | `scribe` | `scribet` | 写入 |
| `quaer-` | — | `quaeret` | 查询（有限） |
| `quaer-` | — | `quaerent` | 查询（流式） |

所有权配对（就地修改 vs 拷贝输出）：

| 修改 | 拷贝输出 | 含义 |
|--------|----------|---------|
| `adde` | `addita` | 添加 |
| `inverte` | `inversa` | 反转 |
| `filtra` | `filtrata` | 过滤 |

## 用法 {#usage}

```faber locale=la
importa ex "norma:solum" privata solum

functio legeConfig() → textus {
    redde solum.lege("config.toml")
}
```
