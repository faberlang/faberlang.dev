真正的 Faber 套件 — 而非玩具範例片段。原始碼位於公開的
[faberlang/examples](https://github.com/faberlang/examples) 存放庫。
當你需要了解應用程式如何架構、CLI 如何接線、或語言語料庫如何組織時，可使用這些資源。

## 如何執行範例 {#how-to-run}

<<<FENCE 0>>>

確切的進入點指令因套件而異 — 請閱讀每個套件的 `README.md`。

## 應用程式套件 {#applications}

| 套件 | 角色 | 從這裡開始 |
|---|---|---|
| **AI Workbench** | 用於本地模型清單、嵌入及推論工作流程的多指令 CLI；Python 線束驗證 | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · 網站：[AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | Faber 原生本地郵件空間 CLI（檔案支援 + 可選 SQLite 通道），用於代理協調指令 | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | 較大型的應用程式戰役，使用對等線束重新實作常用工具 | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU / 系統工作負載階梯與合約 | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | 腳本與面向核心的展示 | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | 自動化草圖套件 | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | 用於關鍵字重映射的區域設定套件展示 | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | 套件存放庫實驗教材 | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## 語言語料庫 {#corpus}

**corpus** 樹是關鍵字與建構的參考：每個建構一個目錄，內含許多小型 `.fab` 程式。
它是本站產生的 [Corpus](/corpus/) 頁面的真實來源。

| 介面 | URL |
|---|---|
| 原始碼樹 | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| 產生的文件 | [/corpus/](/corpus/) |
| 生態系統說明 | [語言語料庫](/ecosystem/corpus.html) |

## 標準庫導覽 {#stdlib}

Norma 標準庫範例位於 **norma** 存放庫中，不在 `examples/` 下：

- [faberlang/norma](https://github.com/faberlang/norma) — 包含 `norma/exempla/`（如有）
- 網站：[Norma](/ecosystem/norma.html)

## 建議學習順序 {#order}

1. [安裝](/start/install.html) CLI。
2. 瀏覽[快速導覽](/start/)了解語言輪廓。
3. 針對不認識的關鍵字，開啟 **corpus** 頁面（[Corpus 中心](/corpus/)）。
4. 從頭到尾閱讀 **AI Workbench** 或 **ViviLite** 了解應用程式架構。
5. 編輯時使用 [語法](/syntax/) 與 [工具](/tooling/) 作為參考。

## 代理路徑 {#agent-path}

- 技能：[examples](/.well-known/agent-skills/examples/SKILL.md)
- 技能：[corpus](/.well-known/agent-skills/corpus/SKILL.md)
- 索引：[`/llms.txt`](/llms.txt)

## 上一頁 {#previous}

| 上一頁 | 下一頁 |
|---|---|
| [專案與範例](/start/projects.html) | [功能](/features/) |
