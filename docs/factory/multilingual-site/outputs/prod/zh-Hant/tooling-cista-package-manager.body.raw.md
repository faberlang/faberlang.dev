Cista 是 Faber 的套件管理器。它處理套件解析、
相依性管理，以及公開套件儲存庫。

## 概覽 {#overview}

Cista 管理由 `faber.toml` manifest 定義的 Faber 套件。每個
套件會宣告其名稱、進入點、目標後端，以及相依性。

## 套件 manifest {#manifest}

<<<FENCE 0>>>

`[nomen]` 欄位是套件名稱，`[ingressus]` 是進入點模組，
`[scopulus]` 選取程式碼產生目標，而 `[genus]` 宣告套件類型
（`bin` 代表可執行檔，`lib` 代表函式庫）。

## 相依性 {#dependencies}

套件會宣告由 Cista 從套件儲存庫解析的相依性。
相依性解析會產生鎖定檔，以確保可重現的建置。

## 狀態 {#status}

Cista 正在積極開發中。公開套件登錄庫
（`cista.dev`）是與網站實作分開的活動。在同一工作區內的套件，
本機套件解析已可運作。
