*Faber 與作業系統實作 I/O 的每種方式之間的接縫。*

`ad` 是 Faber 的低階能力呼叫原語，也是 Faber 程式碼與外部世界之間的邊界。它會與由路由字串識別的主機資源開啟具型別的對話（`sermo`），然後透過具方向性的半串流交換結構化框架（`scrinium`）。主機核心會將每個路由分派給可插拔的提供者 crate，由提供者實作實際的 I/O——檔案系統、網路、主控台、時間、隨機性，或作業系統能執行的任何其他操作。

## `ad` 原語 {#ad}

`ad` 是關鍵字，不是函式。它會使用 `ascii` 字面值命名的路由，以及選用的開啟器資料，開啟不透明的對話：

<<<FENCE 0>>>

路由字串遵循 `prefix:verb` 模式。主機核心只會比對**前綴**——該前綴下的所有動詞都由提供者負責：

<<<FENCE 1>>>

`ad` 不是外部函式介面。它不會呼叫 C 函式、載入動態函式庫，也不會嵌入行內組合語言。它是一個結構化訊息傳遞邊界：Faber 傳送具型別的框架並接收具型別的框架，而不需要知道提供者是以 Rust 實作、在同一行程內執行、委派給系統呼叫，或轉送至遠端主機。

## 框架型別 {#types}

五個由編譯器擁有的型別組成框架系統：

| 型別 | 角色 | 主要介面 |
|------|------|-------------|
| `sermo` | 對話控制代碼——進行中的雙向交換 | 由 `ad` 建立；透過 `↦ T` 排空，或分割成檢視 |
| `scrinium<T>` | 框架封套——對話中的一則結構化訊息 | 欄位：`id`、`call`、`status`、`data`、`created_ms`、`from`、`trace` |
| `status` | 生命週期標記列舉 | `request`、`item`、`byte`、`bulk`、`done`、`error`、`cancel` |
| `meus<T>` | 輸出半串流——將框架傳送給提供者 | `da(T)`、`fini() → status` |
| `tuus<T>` | 輸入半串流——從提供者接收框架 | `accipe()`、`cursor()`、`exhauri()`、`fini()` |

### 使用具方向性的檢視 {#using-directional-views}

<<<FENCE 2>>>

### 簡單具現化 {#simple-materialization}

對於常見情況——開啟、傳送開啟器、將所有回應框架排空至單一值——`sermo ↦ T` 會折疊對話：

<<<FENCE 3>>>

具現化會使用由型別決定的收集器：`↦ textus` 會串接所有輸入框架，`↦ json` 會剖析串接後的承載內容，`↦ lista<T>` 會將框架收集至清單。

## 主機提供者 {#providers}

效果族群由 `faberlang/host-providers-rs` 下的個別提供者 crate 實作。每個提供者都負責其前綴下的所有動詞：

| 提供者 | 前綴 | I/O 領域 |
|----------|--------|------------|
| `solum` | `solum:*` | 檔案系統：讀取、寫入、後設資料、目錄操作 |
| `processus` | `processus:*` | 行程執行：產生、管線、結束代碼 |
| `consolum` | `consolum:*` | 主控台 I/O：標準輸入、標準輸出、標準錯誤 |
| `tempus` | `tempus:*` | 時間：現在、休眠、計時器 |
| `aleator` | `aleator:*` | 隨機性：熵、分佈 |
| `http` | `http:*` | HTTP 用戶端（Tier D，落地後） |

提供者是具有自身相依性的個別 crate——`solum` 不會拉入 HTTP，`http` 也不會拉入檔案系統程式碼。每個提供者都會匯出 `register()` 函式，由產生的主機資訊清單在啟動時呼叫。

## 層堆疊 {#layers}

<<<FENCE 4>>>

編譯器會產生泛型分派——絕不會將提供者 crate 名稱嵌入產生的程式碼。執行環境提供 `HostDispatch` 與對話協定。核心（來自 `host-kernel-rs`）會根據前綴將框架路由至正確的提供者。提供者（來自 `host-providers-rs`）會執行實際的 I/O。

這表示產生的 Faber 程式碼是**與提供者無關的**。只要變更編譯資訊清單，同一個已編譯二進位檔就能連結至不同的提供者實作——正式環境使用真正的檔案系統提供者，測試使用模擬提供者。

## 編譯資訊清單 {#manifest}

要連結哪些提供者，由產生的編譯資訊清單與 `faber.toml` 的 `[dispatch]` 表格控制：

<<<FENCE 5>>>

在撰寫期間，缺少提供者會產生執行期 `E_NO_ROUTE` 錯誤。在嚴格模式（未來）中，程式內的每個 `ad` 前綴都必須出現在編譯資訊清單中，而且編譯器會驗證提供者的能力資訊清單涵蓋所使用的路由。

## 架構 {#architecture}

主機平台分散於 `faberlang` 組織中的三個儲存庫：

| 儲存庫 | 角色 |
|------------|------|
| `host-kernel-rs` | 輕量路由器——擁有 `Frame`、`Conversation`、終端生命週期、前綴分派、結構化錯誤（`E_NO_ROUTE`）、能力資訊清單彙整 |
| `host-native-rs` | 原生附加——工作執行緒、`register_providers` 啟動勾點、產生的 `host_register.rs` 整合 |
| `host-providers-rs` | 提供者實作——依每個族群分 crate 的 Cargo 工作區（`solum`、`processus` 等） |

每個提供者 crate 都擁有自身的原生相依性。只有在啟用 HTTP 時，`http` 提供者才會拉入 `hyper` 與 `tokio`。`solum` 提供者使用標準檔案 API，不需要額外的網路相依性。

> **相同路由，任何主機。** 由於 `ad` 會根據路由字串分派，而提供者是可插拔的，因此相同的 Faber 原始碼可以在不變更任何一行 Faber 程式碼的情況下，目標指向原生二進位檔（`host-native-rs`）、WASM 執行環境（作為 Frame/Wasm 配接器的主機核心），或 TypeScript Node.js 行程（`host-providers-ts`）。

## Norma 包裝器 {#stdlib}

大多數 Faber 程式碼不會直接呼叫 `ad`。Norma 標準函式庫會將常見的 `ad` 路由包裝成具型別的函式：

<<<FENCE 6>>>

這些包裝器函式提供型別安全、文件與錯誤處理，但不會掩蓋 I/O 穿越 `ad` 邊界的事實。Norma 包裝器採用開放原始碼，位於 `norma/src/` 下。

## 參考資料 {#references}

1. `radix/docs/design/frame-stream-types.md` — `sermo`、`scrinium`、`status`、`meus`、`tuus` 的完整規格
2. `radix/docs/design/host-provider-gateway.md` — 輕量路由器架構、提供者合約、編譯資訊清單
3. `faberlang/host-kernel-rs/` — 核心路由器實作
4. `faberlang/host-native-rs/` — 原生附加與註冊
5. `faberlang/host-providers-rs/` — 提供者 crate（`solum`、`processus`、`consolum`、`tempus`、`aleator`、`http`）
6. `examples/corpus/ad/` — `sermo` 範例檔案
