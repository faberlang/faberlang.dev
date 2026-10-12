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

<<<FENCE 0>>>
