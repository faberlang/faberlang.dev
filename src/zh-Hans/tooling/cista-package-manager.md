+++
translation_kind = "translated"

title = "Cista package manager"
section = "tooling"
order = 3
sources = [
  "cista/README.md",
]


prose_hash = "sha256:05d23a68f89274ac712edd9df74eceb081ecb757827aedd26e944afc3a23ab42"
code_hash = "sha256:8911c196f515c978b54a345902a35f102715550c60930e2efee379e50e6c7c1e"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
Cista 是 Faber 的包管理器。它负责包解析、依赖管理与公共包存储库。

## 概述 {#overview}

Cista 通过 `faber.toml` 清单管理 Faber 包。每个包声明其名称、入口点、目标后端与依赖项。

## 包清单 {#manifest}

```text
faber.toml

[nomen]
speculum-gen

[ingressus]
main.fab

[scopulus]
rust

[genus]
bin
```

`[nomen]` 字段是包名，`[ingressus]` 是入口模块，`[scopulus]` 选择代码生成目标，`[genus]` 声明包类型（`bin` 表示可执行文件，`lib` 表示库）。

## 依赖项 {#dependencies}

包声明依赖项，由 Cista 从包存储库解析。依赖解析会生成一个锁文件，确保构建的可复现性。

## 状态 {#status}

Cista 正在积极开发中。公共包注册表（`cista.dev`）是与站点实现相互独立的另一项工作。本地包解析适用于同一工作区内的包。
