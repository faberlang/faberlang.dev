+++
translation_kind = "translated"

title = "Install and download"
section = "install"
order = 1
sources = []

prose_hash = "sha256:662becbb3dd5349058bcdfec9219fd07f6fe4217c2e5115c0aade45e0f17f0d4"
code_hash = "sha256:cc9de43077b1262ee3d9edfbd3bd56c4ae51bcca18d0316fa0bb95312f3033b7"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
从当前的预编译发行版安装 **Faber** CLI。编译器前端内置在 `faber` 二进制文件中;常规包工作不需要单独安装 Radix。

本页内容基于 Faber 1.2.0 的仓库发行工件编写。包管理器公式可能落后于仓库发行版;如果 Homebrew 或其他管理器报告较旧的 Radix/Faber 版本,请在此轨道上优先使用下方归档。

## 当前发行版 {#current-release}

| 字段 | 值 |
|---|---|
| **版本** | 1.2.0 |
| **标签** | `faber-v1.2.0` |
| **发行页面** | [GitHub 上的 faber-v1.2.0](https://github.com/faberlang/releases/releases/tag/faber-v1.2.0) |
| **全部发行版** | [站点发行版清单](/history/releases.html) |
| **许可证** | MIT |

## 预编译归档 {#archives}

| 平台 | 下载 | SHA-256 |
|---|---|---|
| **macOS arm64** (Apple Silicon) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-aarch64-apple-darwin.tar.gz) | [校验和](https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-aarch64-apple-darwin.tar.gz.sha256) |
| **Linux x64** (glibc) | [tar.gz](https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-x86_64-unknown-linux-gnu.tar.gz) | [校验和](https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-x86_64-unknown-linux-gnu.tar.gz.sha256) |

归档解压后为 `faber-v1.2.0-<target-triple>/faber`。校验和文件可能引用原始构建路径,因此请将首个哈希字段与本地归档进行比对验证,而非依赖 `sha256sum -c` 的路径匹配。

### macOS arm64 {#macos}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-aarch64-apple-darwin.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-aarch64-apple-darwin.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(shasum -a 256 faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
# place on PATH, e.g.:
sudo mv faber-v1.2.0-aarch64-apple-darwin/faber /usr/local/bin/
faber --version
```

### Linux x64 {#linux}

```bash
curl -fsSL -o faber.tgz \
  https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-x86_64-unknown-linux-gnu.tar.gz
curl -fsSL -o faber.tgz.sha256 \
  https://github.com/faberlang/releases/releases/download/faber-v1.2.0/faber-v1.2.0-x86_64-unknown-linux-gnu.tar.gz.sha256
expected=$(awk '{print $1}' faber.tgz.sha256)
actual=$(sha256sum faber.tgz | awk '{print $1}')
test "$actual" = "$expected"
tar -xzf faber.tgz
sudo mv faber-v1.2.0-x86_64-unknown-linux-gnu/faber /usr/local/bin/
faber --version
```

## 验证 {#verify}

```bash
faber --version
faber explain SEM001
```

你应该看到 CLI 的版本行和诊断说明。如果未找到 `faber`,请检查包含该二进制文件的目录是否已加入 `PATH`。

## 首个包检查 {#first-package}

将 CLI 加入 `PATH` 后,克隆公共示例(或任意 Faber 包)并进行类型检查。产品包通过 `faber.lock` 从 Cista 存储解析依赖;本地源码检出仅用于显式的库开发覆盖。

```bash
git clone https://github.com/faberlang/examples.git
faber check examples/ai-workbench/packages/faber-ai
```

更多包:[示例](/start/examples.html)。CLI 概览:[Faber 构建工具](/tooling/faber-build-tool.html)。

## Homebrew 状态 {#homebrew}

Homebrew 的发布尚不是此入门轨道的权威。如果某个公式服务于较旧的编译器(例如 Radix 0.38.0),而本站点记录的是 Faber 1.2.0,请将该公式视为滞后,并使用预编译发行归档。在公式发布跟上之前,本页的容器验证门禁仍为残留状态。

## 从源码构建 {#from-source}

预编译版是智能体和大多数开发者的推荐路径。从源码构建需要私有的 Radix 编译器树,不在本页讨论范围之内。除非你正在开发编译器本身,否则请优先使用上方归档。

## 智能体路径 {#agent-path}

智能体应加载 **install** 技能和智能体索引,而不是抓取此 HTML:

- [`/llms.txt`](/llms.txt)
- [install 技能](/.well-known/agent-skills/install/SKILL.md)
- [智能体指南](/agents/index.md)

## 下一步 {#next}

| 上一页 | 下一页 |
|---|---|
| [快速导览](/start/) | [Hello, Faber](/start/hello.html) |
