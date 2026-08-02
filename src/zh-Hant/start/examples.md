+++
translation_kind = "translated"

title = "Examples"
section = "examples"
order = 5
sources = [
  "examples/README.md",
  "examples/ai-workbench/",
  "examples/vivilite/",
  "examples/ai-workbench/ (README.md, package, harness)",
  "examples/coreutils/ (38 packages, README.md, campaign docs)",
  "examples/coreutils/packages/echo/src/main.fab",
]
+++

## Examples

真正的 Faber 套件——不是玩具範例。原始碼位於公開的 [faberlang/examples](https://github.com/faberlang/examples) 儲存庫。

當您需要了解應用程式的結構、CLI 的連接方式，或語言語料庫的組織方式時，請使用這些範例。

### 如何執行範例 {#how-to-run}

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

### 應用程式套件 {#applications}

| 套件 | 角色 | 從這裡開始 |
|---|---|---|
| **AI Workbench** | 用於本機模型清單、嵌入與推論工作流程的多指令 CLI；含 Python 驗證工具 | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · 網站：[AI Workbench](/start/examples.html) |
| **ViviLite** | 以 Faber 原生實作的本機 mailspace CLI，用於代理協調指令；支援檔案後端與可選的 SQLite 工作線 | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | 重新實作常用工具的大型應用程式專案，並附有相容性驗證工具 | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU／系統工作負載階梯與契約 | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | 指令碼與核心介面示範 | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | 自動化草案套件 | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | 用於關鍵字重新映射的語系套件示範 | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | 套件儲存區實驗材料 | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

### 語言語料庫 {#corpus}

**corpus** 樹狀目錄是關鍵字與語法建構的參考資料：每個建構各有一個目錄，其中包含許多小型 `.fab` 程式。

它是本網站所生成 [Corpus](/corpus/) 頁面的真實來源。

| 介面 | URL |
|---|---|
| 原始碼樹 | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| 生成文件 | [/corpus/](/corpus/) |
| 生態系統說明 | [語言語料庫](/libraries/corpus.html) |

### 標準函式庫導覽 {#stdlib}

Norma 標準函式庫的 exempla 位於 **norma** 儲存庫，不在 `examples/` 之下：

- [faberlang/norma](https://github.com/faberlang/norma) — 若存在，請查看 `norma/exempla/`
- 網站：[Norma](/libraries/norma.html)

### 建議學習順序 {#order}

1. 安裝 CLI：[Install](/start/install.html)。
2. 略讀 [Quick tour](/start/)，了解語言的基本形態。
3. 對於任何您不熟悉的關鍵字，開啟 **corpus** 頁面（[Corpus hub](/corpus/)）。
4. 從頭到尾閱讀 **AI Workbench** 或 **ViviLite**，了解應用程式的結構。
5. 編輯時，使用 [Syntax](/language/) 與 [Tooling](/toolchain/) 作為參考。

### 代理路徑 {#agent-path}

- 技能：[examples](/.well-known/agent-skills/examples/SKILL.md)
- 技能：[corpus](/.well-known/agent-skills/corpus/SKILL.md)
- 索引：[`/llms.txt`](/llms.txt)

### 上一頁 {#previous}

| 上一頁 | 下一頁 |
|---|---|
| [專案與範例](/start/projects.html) | [功能](/language/) |

## AI Workbench

AI Workbench 是一個 Faber CLI 應用程式，用於本機模型清單、 中繼資料檢查、嵌入、索引與推論工作流程。它示範 Faber 建置具備實際 I/O、JSON 輸出與 Python 測試控制器驗證功能的大型多指令 CLI 應用程式。

### 套件 {#package}

`examples/ai-workbench/packages/faber-ai/`，包含以下 CLI 子命令：

- `model inspect` — 查詢本機模型別名、路由與狀態
- `embed` — 從文字輸入產生嵌入

### 命令 {#commands}

```bash
faber check examples/ai-workbench/packages/faber-ai
faber test examples/ai-workbench/packages/faber-ai
faber run examples/ai-workbench/packages/faber-ai -- model inspect basic/minilm --format json
```

### 驗證 {#validation}

AI Workbench 包含 20 多個 Python 測試控制器指令碼，會將 Faber 輸出與模型清單、推論、GPU 證據、工作階段生命週期及套件重複使用的固定資料對照，示範對已編譯 Faber 二進位檔進行跨語言驗證。

## Coreutils

Faber 以應用程式軌證明的方式重新實作 GNU coreutils。這些是真實的 CLI 程式，示範 Faber 如何使用 argv、stdio、結束碼與主機 I/O 建置可運作的二進位檔，並透過 parity harness 與主機上的 GNU 工具進行驗證。

### 已實作的工具 {#implemented-utilities}

**階段 1 — 腳手架 + true/false**  
`true`、`false`

**階段 2 — 共用通用輔助程式 + 內嵌測試**  
`echo`、`basename`、`dirname`、`printf`、`seq`

**階段 3 — 可為空的 stdin 切片**  
`cat`、`head`、`tail`、`wc`、`tac`、`uniq`、`fold`、`nl`、`expand`、  
`unexpand`、`sort`、`cut`、`grep`、`tr`、`tee`、`paste`

**已建立腳手架 — 階段 5+**  
`rm`、`cp`、`mv`、`mkdir`、`touch`、`pwd`、`readlink`、`realpath`、  
`join`、`comm`、`od`、`cksum`、`split`、`yes`、`printenv`

### 範例 — echo {#example--echo}

`echo` 套件示範 coreutils 各處使用的 Faber 模式：CLI 註解、選項剖析、使用 `probandum`/`proba`/`adfirma` 的內嵌測試，以及共用的通用模組：

```faber locale=la
importa ex "norma:consolum" privata consolum

functio echo_textus(lista<textus> words) → textus {
    redde ""
}

functio echo_novam_lineam(lista<textus> words) → bivalens {
    redde falsum
}

probandum "echo formatting" tag "coreutils" {
    proba "empty operands" {
        adfirma echo_textus([]) ≡ ""
    }
    proba "-n suppresses newline" {
        adfirma echo_novam_lineam(["-n", "hello"]) ≡ falsum
    }
}

@ cli "echo"
@ descriptio "GNU coreutils echo parity exemplum"
@ operandus ceteri textus words
incipit argumenta args {
    # ... CLI logic here
}
```

### 執行 {#running}

```bash
faber check coreutils/packages/echo
faber test coreutils/packages/echo
faber run coreutils/packages/echo -- hello world
```
