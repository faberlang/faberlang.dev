真正的 Faber 套件，而非玩具範例。原始碼位於公開的
[faberlang/examples](https://github.com/faberlang/examples) 儲存庫。
當你需要瞭解應用程式的結構、CLI 的串接方式，或語言語料庫的組織方式時，
可以參考這些內容。

## 如何執行範例 {#how-to-run}

<<<FENCE 0>>>

確切的進入指令會依套件而異——請閱讀各套件的 `README.md`。

## 應用程式套件 {#applications}

| 套件 | 角色 | 從這裡開始 |
|---|---|---|
| **AI Workbench** | 用於本機模型清單、嵌入與推論工作流程的多指令 CLI；Python 驗證工具 | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · 網站：[AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | Faber 原生的本機 mailspace CLI（檔案後端，並可選用 SQLite 工作線），用於代理程式協調指令 | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | 以相容性測試工具重新實作常見工具的大型應用程式專案 | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU／系統工作負載階梯與契約 | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | 指令碼與核心介面示範 | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | 自動化草圖套件 | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | 用於關鍵字重新映射的語系套件示範 | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | 套件儲存區實驗材料 | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## 語言語料庫 {#corpus}

**corpus** 樹狀目錄是關鍵字與語法結構的參考資料：每個語法結構各有一個目錄，
其中包含許多小型 `.fab` 程式。它是本網站所產生之[語料庫](/corpus/)頁面的唯一真實來源。

| 介面 | URL |
|---|---|
| 原始碼樹 | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| 產生的文件 | [/corpus/](/corpus/) |
| 生態系統說明 | [語言語料庫](/ecosystem/corpus.html) |

## 標準函式庫導覽 {#stdlib}

Norma 標準函式庫的 exempla 位於 **norma** 儲存庫，而不在
`examples/` 底下：

- [faberlang/norma](https://github.com/faberlang/norma) — 若存在，請參閱 `norma/exempla/`
- 網站：[Norma](/ecosystem/norma.html)

## 建議學習順序 {#order}

1. [安裝](/start/install.html) CLI。
2. 掃讀[快速導覽](/start/)，瞭解語言的整體形貌。
3. 對於任何你不熟悉的關鍵字，開啟 **corpus** 頁面（[語料庫首頁](/corpus/)）。
4. 從頭到尾閱讀 **AI Workbench** 或 **ViviLite**，瞭解應用程式的形貌。
5. 編輯時，使用[語法](/syntax/)與[工具鏈](/tooling/)作為參考。

## 代理程式路徑 {#agent-path}

- 技能：[examples](/.well-known/agent-skills/examples/SKILL.md)
- 技能：[corpus](/.well-known/agent-skills/corpus/SKILL.md)
- 索引：[`/llms.txt`](/llms.txt)

## 上一頁 {#previous}

| 上一頁 | 下一頁 |
|---|---|
| [專案與範例](/start/projects.html) | [功能](/features/) |
