撰寫最小但實用的 Faber 程式：一個會格式化字串並將其印出的套件進入點。

## 先決條件 {#prerequisites}

請先完成[安裝與下載](/start/install.html)。您應該已在 `PATH` 中擁有
`faber` 二進位檔，並且在可以建立檔案的工作目錄中開啟 Shell。

## 建立套件 {#create-package}

<<<FENCE 0>>>

## 檢查程式 {#check}

<<<FENCE 1>>>

`faber check` 會執行前端處理：詞法分析、剖析、型別檢查，以及足以擷取一般套件錯誤的降階處理，而不必建置原生二進位檔。
如果命令失敗，請先讀取診斷代碼；Faber 診斷資訊設計成穩定的搜尋識別項。

## 執行程式 {#run}

<<<FENCE 2>>>

預期輸出：

<<<FENCE 3>>>

## 您剛才使用的內容 {#what-you-used}

| 原始碼 | 意義 |
|---|---|
| `functio salve(textus nomen) → textus` | 名為 `salve` 的函式，型別優先的參數，回傳文字 |
| `fixum textus msg ← ...` | 不可變繫結 |
| `"Salve, §!"(nomen)` | 具有顯示插值的格式字串 |
| `redde msg` | 回傳 |
| `incipit` | 套件進入點 |
| `nota m` | 印出註記／輸出值 |

## 語系證明 {#locale-proof}

上面的程式是標準的拉丁文讀者呈現方式。讀者語系可以使用不同的關鍵字套件呈現相同的語意程式，同時保留字形與識別碼。在撰寫非拉丁文套件之前，請先從完整的[讀者語系](/features/reader-locale.html)證明開始。

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [安裝與下載](/start/install.html) | [您將使用的命令](/start/commands.html) |
