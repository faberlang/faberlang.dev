Faber 中的函式使用 `functio` 宣告，採用型別優先的參數語法，並使用字形回傳型別。

## 基本語法 {#basic-syntax}

<<<FENCE 0>>>

帶有錯誤通道：

<<<FENCE 1>>>

## 範例 {#examples}

<<<FENCE 2>>>

## 回傳值 {#return-values}

使用 `redde` 進行一般回傳：

<<<FENCE 3>>>

`vacuum` 回傳型別的裸 `redde`：

<<<FENCE 4>>>

## 借用與可變性（de、in、ex） {#borrowing-and-mutability}

Faber 使用參數上的簡短介系詞標記值的傳遞方式：

| 標記 | 意圖 | 常見的 Rust 降低方式 |
|--------|------|----------------------|
| *(無)* | 擁有值 | 以值傳遞的 `T` |
| `de` | 共用借用（唯讀） | `&T` |
| `in` | 可變借用 | `&mut T` |
| `ex` | 消耗（移入被呼叫者） | 以移動傳遞的 `T` |

<<<FENCE 5>>>

相同的詞（`de`、`ex`）也會在其他結構中重複使用——不要將每個 `ex` 都解讀為「消耗」：

| 表面語法 | 角色 |
|---------|------|
| 參數上的 `de textus name` | 共用借用 |
| 參數上的 `in numerus count` | 可變借用 |
| 參數上的 `ex textus buffer` | 移入被呼叫者 |
| `itera ex items fixum item` | 迭代值 |
| `itera de tabula fixum key` | 迭代鍵 |
| `ex source fixum x, ceteri rest` | 解構欄位 |
| `importa ex "path"` | 從模組匯入 |

## 進入點 {#entry-point}

程式的進入點是 `incipit`：

<<<FENCE 6>>>

## CLI 進入點 {#cli-entry-point}

對於 CLI 程式，`incipit argumenta` 會接收已解析的命令列引數：

<<<FENCE 7>>>

## 傳遞模式——`sponte` {#passing-mode-sponte}

`sponte` 標記可由呼叫者省略的參數：

<<<FENCE 8>>>
