+++
translation_kind = "translated"

title = "Examples"
section = "examples"
order = 2
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
]

prose_hash = "sha256:fe9855413a019d0aebf6228e219c1fab4b694d7fa3fd7d7f7cacab4def2f3700"
code_hash = "sha256:7fce5618203f2537ec7b775252d4ce66501a659a385973e9ec6cc1414c49e9e6"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
真正的 Faber 套件——不是玩具範例。原始碼位於公開的 [faberlang/examples](https://github.com/faberlang/examples) 儲存庫。

當您需要了解應用程式的結構、CLI 的連接方式，或語言語料庫的組織方式時，請使用這些範例。

## 如何執行範例 {#how-to-run}

```bash
# CLI on PATH (see Install)
faber --version

# Clone examples
git clone https://github.com/faberlang/examples.git

# Type-check a package; dependencies resolve through faber.lock
# and the Cista package store.
faber check examples/ai-workbench/packages/faber-ai

# Build / run / test when the package supports it
faber build examples/ai-workbench/packages/faber-ai -t rust
faber test examples/ai-workbench/packages/faber-ai
```

實際的進入指令會因套件而異——請閱讀各套件的 `README.md`。

## 應用程式套件 {#applications}

| 套件 | 角色 | 從這裡開始 |
|---|---|---|
| **AI Workbench** | 用於本機模型清單、嵌入與推論工作流程的多指令 CLI；含 Python 驗證工具 | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · 網站：[AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | 以 Faber 原生實作的本機 mailspace CLI，用於代理協調指令；支援檔案後端與可選的 SQLite 工作線 | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | 重新實作常用工具的大型應用程式專案，並附有相容性驗證工具 | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU／系統工作負載階梯與契約 | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | 指令碼與核心介面示範 | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | 自動化草案套件 | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | 用於關鍵字重新映射的語系套件示範 | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | 套件儲存區實驗材料 | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## 語言語料庫 {#corpus}

**corpus** 樹狀目錄是關鍵字與語法建構的參考資料：每個建構各有一個目錄，其中包含許多小型 `.fab` 程式。

它是本網站所生成 [Corpus](/corpus/) 頁面的真實來源。

| 介面 | URL |
|---|---|
| 原始碼樹 | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| 生成文件 | [/corpus/](/corpus/) |
| 生態系統說明 | [語言語料庫](/ecosystem/corpus.html) |

## 標準函式庫導覽 {#stdlib}

Norma 標準函式庫的 exempla 位於 **norma** 儲存庫，不在 `examples/` 之下：

- [faberlang/norma](https://github.com/faberlang/norma) — 若存在，請查看 `norma/exempla/`
- 網站：[Norma](/ecosystem/norma.html)

## 建議學習順序 {#order}

1. 安裝 CLI：[Install](/start/install.html)。
2. 略讀 [Quick tour](/start/)，了解語言的基本形態。
3. 對於任何您不熟悉的關鍵字，開啟 **corpus** 頁面（[Corpus hub](/corpus/)）。
4. 從頭到尾閱讀 **AI Workbench** 或 **ViviLite**，了解應用程式的結構。
5. 編輯時，使用 [Syntax](/syntax/) 與 [Tooling](/tooling/) 作為參考。

## 代理路徑 {#agent-path}

- 技能：[examples](/.well-known/agent-skills/examples/SKILL.md)
- 技能：[corpus](/.well-known/agent-skills/corpus/SKILL.md)
- 索引：[`/llms.txt`](/llms.txt)

## 上一頁 {#previous}

| 上一頁 | 下一頁 |
|---|---|
| [專案與範例](/start/projects.html) | [功能](/features/) |
