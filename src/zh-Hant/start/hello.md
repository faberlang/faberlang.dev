+++
translation_kind = "translated"

title = "Hello, Faber"
section = "hello"
order = 2
sources = []

prose_hash = "sha256:3a78129bf3787f7c726e39104c95fe9bde78855c4a9f63650410c5cef9610067"
code_hash = "sha256:1ee50be729b09d1bfba27a1f994ef4d1a47c73a645764f9d5986c9bab1aecfb8"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
撰寫最小但實用的 Faber 程式：建立一個格式化字串並將其列印出來的套件入口點。

## 先決條件 {#prerequisites}

請先完成[安裝與下載](/start/install.html)。你應該已將
`faber` 二進位檔放在 `PATH` 中，並在可建立檔案的工作目錄中開啟 shell。

## 建立套件 {#create-package}

```bash
mkdir salve-munde
cd salve-munde
mkdir src
cat > faber.toml <<'EOF'
[package]
name = "salve-munde"
version = "0.1.0"
EOF
cat > src/main.fab <<'EOF'
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
EOF
```

## 檢查它 {#check}

```bash
faber check .
```

`faber check` 會執行前端流程：詞法分析、剖析、型別檢查，以及足以
在不建立原生二進位檔的情況下捕捉一般套件錯誤的降低階段。
如果指令失敗，請先讀取診斷碼；Faber 診斷碼設計為穩定的搜尋索引。

## 執行它 {#run}

```bash
faber run .
```

預期輸出：

```text
Salve, munde!
```

## 你剛才使用的內容 {#what-you-used}

| 來源 | 意義 |
|---|---|
| `functio salve(textus nomen) → textus` | 名為 `salve` 的函式、型別優先的參數、文字回傳值 |
| `fixum textus msg ← ...` | 不可變繫結 |
| `"Salve, §!"(nomen)` | 帶有顯示插值的格式字串 |
| `redde msg` | 回傳 |
| `incipit` | 套件入口點 |
| `nota m` | 列印備註／輸出值 |

## 語系證明 {#locale-proof}

上方程式是規範的拉丁文讀者語系呈現。讀者語系可以使用不同的關鍵字包來
呈現相同的語意程式，同時保留字形與識別碼。在撰寫非拉丁文套件之前，請先從
[讀者語系](/features/reader-locale.html)的完整證明開始。

## 下一步 {#next}

| 上一頁 | 下一頁 |
|---|---|
| [安裝與下載](/start/install.html) | [你將使用的指令](/start/commands.html) |
