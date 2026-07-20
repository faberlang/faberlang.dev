*Faber 与操作系统所有 I/O 实现方式之间的接缝。*

`ad` 是 Faber 的底层能力调用原语——Faber 代码与外部世界之间的边界。它通过路由字符串标识的主机资源开启一次类型化对话（`sermo`），随后在方向性半流上交换结构化帧（`scrinium`）。主机内核将每条路由分发给一个可插拔的提供方 crate，由后者实现真正的 I/O——文件系统、网络、控制台、时间、随机数，或操作系统能做的任何其他事情。

## `ad` 原语 {#ad}

`ad` 是一个关键字，而非函数。它通过由 `ascii` 字面量和可选的开启数据命名的路由，开启一次不透明的对话：

<<<FENCE 0>>>

路由字符串遵循 `prefix:verb` 模式。主机内核仅匹配 **前缀**——提供方拥有该前缀下的所有动词：

<<<FENCE 1>>>

`ad` 不是外部函数接口。它不调用 C 函数，不加载动态库，也不嵌入内联汇编。它是一个结构化消息传递边界：Faber 发送类型化帧并接收类型化帧，而不关心提供方是用 Rust 实现、在进程内运行、委托给系统调用，还是转发到远程主机。

## 帧类型 {#types}

五个由编译器拥有的类型构成了帧系统：

| 类型 | 职责 | 关键接口 |
|------|------|-------------|
| `sermo` | 对话句柄——进行中的双向交换 | 由 `ad` 创建；通过 `↦ T` 耗尽或拆分为视图 |
| `scrinium<T>` | 帧封套——对话中的一条结构化消息 | 字段：`id`、`call`、`status`、`data`、`created_ms`、`from`、`trace` |
| `status` | 生命周期标记枚举 | `request`、`item`、`byte`、`bulk`、`done`、`error`、`cancel` |
| `meus<T>` | 出站半流——向提供方发送帧 | `da(T)`、`fini() → status` |
| `tuus<T>` | 入站半流——从提供方接收帧 | `accipe()`、`cursor()`、`exhauri()`、`fini()` |

### 使用方向性视图 {#using-directional-views}

<<<FENCE 2>>>

### 简单物化 {#simple-materialization}

对于常见情形——开启、发送开启数据、将所有响应帧耗尽为一个值——`sermo ↦ T` 会折叠对话：

<<<FENCE 3>>>

物化使用类型导向的收集器：`↦ textus` 拼接所有入站帧，`↦ json` 解析拼接后的负载，`↦ lista<T>` 将帧收集为列表。

## 主机提供方 {#providers}

效应族作为独立的提供方 crate 实现，位于 `faberlang/host-providers-rs` 之下。每个提供方拥有其前缀下的所有动词：

| 提供方 | 前缀 | I/O 领域 |
|----------|--------|------------|
| `solum` | `solum:*` | 文件系统：读、写、元数据、目录操作 |
| `processus` | `processus:*` | 进程执行：派生、管道、退出码 |
| `consolum` | `consolum:*` | 控制台 I/O：stdin、stdout、stderr |
| `tempus` | `tempus:*` | 时间：当前时间、休眠、计时器 |
| `aleator` | `aleator:*` | 随机数：熵、分布 |
| `http` | `http:*` | HTTP 客户端（Tier D，落地后提供） |

提供方是拥有各自依赖的独立 crate——`solum` 不引入 HTTP，`http` 不引入文件系统代码。每个提供方导出一个 `register()` 函数，由生成的主机清单在启动时调用。

## 分层栈 {#layers}

<<<FENCE 4>>>

编译器生成通用分发——它从不将提供方 crate 名称嵌入生成的代码。运行时提供 `HostDispatch` 和对话协议。内核（来自 `host-kernel-rs`）根据前缀将帧路由到正确的提供方。提供方（来自 `host-providers-rs`）执行真正的 I/O。

这意味着生成的 Faber 代码是 **提供方中立** 的。同一个编译二进制可以链接不同的提供方实现——用于生产的真实文件系统提供方、用于测试的模拟提供方——只需更改编译清单即可。

## 编译清单 {#manifest}

要链接哪些提供方，由生成的编译清单和 `faber.toml` 中的 `[dispatch]` 表控制：

<<<FENCE 5>>>

在创作阶段，缺失的提供方会产生运行时 `E_NO_ROUTE` 错误。在严格模式（未来）下，程序中的每个 `ad` 前缀都必须出现在编译清单中，并且编译器会验证提供方的能力清单覆盖所使用的路由。

## 架构 {#architecture}

主机平台分散在 `faberlang` 组织的三个仓库中：

| 仓库 | 职责 |
|------------|------|
| `host-kernel-rs` | 轻量路由器——拥有 `Frame`、`Conversation`、终端生命周期、前缀分发、结构化错误（`E_NO_ROUTE`）、能力清单聚合 |
| `host-native-rs` | 原生附加——worker、`register_providers` 启动钩子、生成的 `host_register.rs` 集成 |
| `host-providers-rs` | 提供方实现——按族划分 crate 的 Cargo 工作区（`solum`、`processus` 等） |

每个提供方 crate 拥有自己的原生依赖。`http` 提供方仅在启用 HTTP 时引入 `hyper` 和 `tokio`。`solum` 提供方使用标准文件 API，不引入任何额外的网络依赖。

> **同一路由，任意主机。** 由于 `ad` 基于路由字符串分发且提供方可插拔，同一份 Faber 源码可以目标为原生二进制（host-native-rs）、WASM 运行时（host-kernel 作为 Frame/Wasm 适配器）或 TypeScript Node.js 进程（host-providers-ts），而无需改动一行 Faber 代码。

## Norma 封装 {#stdlib}

大多数 Faber 代码不直接调用 `ad`。Norma 标准库将常见的 `ad` 路由封装在类型化函数中：

<<<FENCE 6>>>

这些封装函数提供类型安全、文档和错误处理，同时不掩盖 I/O 跨越 `ad` 边界这一事实。Norma 封装是开源的，位于 `norma/src/` 之下。

## 参考资料 {#references}

1. `radix/docs/design/frame-stream-types.md`——sermo、scrinium、status、meus、tuus 的完整规范
2. `radix/docs/design/host-provider-gateway.md`——轻量路由器架构、提供方契约、编译清单
3. `faberlang/host-kernel-rs/`——内核路由器实现
4. `faberlang/host-native-rs/`——原生附加与注册
5. `faberlang/host-providers-rs/`——提供方 crate（solum、processus、consolum、tempus、aleator、http）
6. `examples/corpus/ad/`——sermo exempla 文件
