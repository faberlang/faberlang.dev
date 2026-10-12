真實的 Faber 套件，而非玩具式片段。原始碼存放於公開的
[faberlang/examples](https://github.com/faberlang/examples) 儲存庫。
當你需要了解應用程式的結構、CLI 如何接線，或語言語料庫如何組織時，請參考這些資源。

## 如何執行範例 {#how-to-run}

<<<FENCE 0>>>

確切的進入指令因套件而異——請閱讀每個套件的 `README.md`。

## 應用程式套件 {#applications}

| 套件 | 角色 | 從這裡開始 |
|---|---|---|
| **AI Workbench** | 多指令 CLI，用於本地模型清查、嵌入與推論工作流程；Python 驗證工具組 | [examples/ai-workbench](https://github.com/faberlang/examples/tree/main/ai-workbench) · 站台：[AI Workbench](/ecosystem/ai-workbench.html) |
| **ViviLite** | Faber 原生的本地郵件空間 CLI（檔案支援 + 選用的 SQLite 通道），用於代理協調指令 | [examples/vivilite](https://github.com/faberlang/examples/tree/main/vivilite) |
| **coreutils** | 較大型應用程式專案，重新實作常見公用程式並具備一致性驗證工具組 | [examples/coreutils](https://github.com/faberlang/examples/tree/main/coreutils) |
| **gpu-workload** | GPU / 系統工作負載階梯與契約 | [examples/gpu-workload](https://github.com/faberlang/examples/tree/main/gpu-workload) |
| **scripta / script-kernel** | 腳本與核心導向的範例 | [examples/scripta](https://github.com/faberlang/examples/tree/main/scripta) |
| **automation** | 自動化草案套件 | [examples/automation](https://github.com/faberlang/examples/tree/main/automation) |
| **reader-locale** | 用於關鍵字重新映射的地區套件範例 | [examples/reader-locale](https://github.com/faberlang/examples/tree/main/reader-locale) |
| **cista-lab** | 套件商店實驗室素材 | [examples/cista-lab](https://github.com/faberlang/examples/tree/main/cista-lab) |

## 語言語料庫 {#corpus}

**語料庫**（corpus）樹是關鍵字與結構的參考來源：每個結構一個目錄，內含許多小型的 `.fab` 程式。它是本站生成的 [語料庫](/corpus/) 頁面的真相來源。

| 表面 | URL |
|---|---|
| 原始碼樹 | [examples/corpus](https://github.com/faberlang/examples/tree/main/corpus) |
| 生成的文件 | [/corpus/](/corpus/) |
| 生態系說明 | [語言語料庫](/ecosystem/corpus.html) |

## 標準函式庫導覽 {#stdlib}

Norma 標準函式庫的範例存放於 **norma** 儲存庫，而非 `examples/` 之下：

- [faberlang/norma](https://github.com/faberlang/norma) — 若存在則為 `norma/exempla/`
- 站台：[Norma](/ecosystem/norma.html)

## 建議的學習順序 {#order}

1. [安裝](/start/install.html) CLI。
2. 瀏覽 [快速導覽](/start/) 以了解語言形態。
3. 針對任何你不認識的關鍵字，開啟 **語料庫** 頁面（[語料庫中樞](/corpus/)）。
4. 端對端閱讀 **AI Workbench** 或 **ViviLite** 以了解應用程式形態。
5. 編輯時將 [語法](/syntax/) 與 [工具](/tooling/) 作為參考資料。

## 代理路徑 {#agent-path}

- 技能：[examples](/.well-known/agent-skills/examples/SKILL.md)
- 技能：[corpus](/.well-known/agent-skills/corpus/SKILL.md)
- 索引：[`/llms.txt`](/llms.txt)

## 上一頁 {#previous}

| 上一頁 | 下一頁 |
|---|---|
| [專案與範例](/start/projects.html) | [功能](/features/) |
