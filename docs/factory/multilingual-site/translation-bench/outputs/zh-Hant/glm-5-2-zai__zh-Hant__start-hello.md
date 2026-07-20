撰寫最小可用的 Faber 程式:一個套件進入點,負責格式化字串並將其印出。

## 先決條件 {#prerequisites}

請先完成[安裝與下載](/start/install.html)。你的 `PATH` 中應該已有 `faber` 執行檔,並且在一個可以建立檔案的工作目錄中開啟終端機。

## 建立套件 {#create-package}

<<<FENCE 0>>>

## 檢查它 {#check}

<<<FENCE 1>>>

`faber check` 會執行前端處理:詞法分析、剖析、型別檢查,以及足夠程度的降階,以便在不建構原生二進位檔的情況下捕捉常見的套件錯誤。如果指令失敗,請先閱讀診斷代碼;Faber 的診斷訊息設計為可供穩定搜尋的依據。

## 執行它 {#run}

<<<FENCE 2>>>

預期輸出:

<<<FENCE 3>>>

## 你剛剛使用的內容 {#what-you-used}

| 原始碼 | 意義 |
|---|---|
| `functio salve(textus nomen) → textus` | 名為 `salve` 的函式,型別優先參數,回傳文字 |
| `fixum textus msg ← ...` | 不可變繫結 |
| `"Salve, §!"(nomen)` | 帶顯示插值的格式字串 |
| `redde msg` | 回傳 |
| `incipit` | 套件進入點 |
| `nota m` | 印出附註/輸出值 |

## 語系驗證 {#locale-proof}

上方程式為標準的拉丁語系讀者呈現。讀者語系可以使用不同的關鍵字套件,在保留字形與識別碼的前提下,呈現同一個語意相同的程式。在撰寫非拉丁語系的套件之前,請先至[讀者語系](/features/reader-locale.html)閱讀完整驗證。

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [安裝與下載](/start/install.html) | [你將使用的指令](/start/commands.html) |
