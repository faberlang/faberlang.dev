撰寫最小但實用的 Faber 程式：建立一個格式化字串並列印它的套件進入點。

## 先備條件 {#prerequisites}

請先完成[安裝與下載](/start/install.html)。您應該已在 `PATH` 中擁有
`faber` 二進位檔，並且位於可以建立檔案的工作目錄中。

## 建立套件 {#create-package}

<<<FENCE 0>>>

## 檢查套件 {#check}

<<<FENCE 1>>>

`faber check` 會執行前端處理：詞法分析、語法分析、型別檢查，以及足以
擷取一般套件錯誤的降階處理，而不會建置原生二進位檔。如果命令失敗，請先
閱讀診斷代碼；Faber 診斷代碼設計為穩定的搜尋識別碼。

## 執行套件 {#run}

<<<FENCE 2>>>

預期輸出：

<<<FENCE 3>>>

## 剛才使用的內容 {#what-you-used}

| 原始碼 | 意義 |
|---|---|
| `functio salve(textus nomen) → textus` | 名為 `salve` 的函式、型別優先參數、文字回傳值 |
| `fixum textus msg ← ...` | 不可變繫結 |
| `"Salve, §!"(nomen)` | 使用顯示插值的格式字串 |
| `redde msg` | 回傳 |
| `incipit` | 套件進入點 |
| `nota m` | 列印備註／輸出值 |

## 地區設定證明 {#locale-proof}

上述程式是標準的拉丁文讀者呈現。讀者地區設定可以使用不同的關鍵字組
呈現相同的語意程式，同時保留字形與識別碼。在撰寫非拉丁文套件之前，請先從
[讀者地區設定](/features/reader-locale.html)中的完整證明開始。

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [安裝與下載](/start/install.html) | [您將使用的命令](/start/commands.html) |
