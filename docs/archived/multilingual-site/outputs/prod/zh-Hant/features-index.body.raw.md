Faber 的設計建立在三項訊號選擇之上：型別優先宣告、拉丁文行為詞彙，以及結構符號。這些特性彼此疊加——每一項都強化其他項目，讓原始碼在各種執行通道之間保持可讀、可檢查且可攜。

## 讀者語系 {#reader-locale}

編譯器就是翻譯器。讀者語系套件讓相同的原始碼能以多種自然語言呈現，同時不改變語意。[閱讀更多 →](/features/reader-locale.html)

## 編譯通道 {#compilation-lanes}

Faber 會經過三種中間表示（HIR、MIR、AIR）降階至多個目標後端，包括 Rust 執行階段、WASM、TypeScript、Go 與 GPU/WGSL。[閱讀更多 →](/features/compilation-lanes.html)

## 拉丁詞彙與符號 {#latin-and-glyphs}

型別先於名稱。拉丁文字承載行為。結構符號承載值流與型別形狀。最終結果讀起來像意圖，而不是機制。[閱讀更多 →](/features/latin-and-glyphs.html)

## 誡命 {#commandments}

九項設計法則規範每一項語言決策，從關鍵字選擇到錯誤處理皆然。這些法則也是新功能的審查標準。[閱讀更多 →](/features/commandments.html)

## 正典與語法糖 {#canonical-vs-sugar}

每個語法糖表面都有一個正典展開形式。格式化工具可以在兩者之間轉換。語法糖提供便利；正典則是契約。[閱讀更多 →](/features/canonical-vs-sugar.html)

## 能力呼叫與框架 {#frames}

`ad` 原語提供以能力為基礎的分派。框架型別定義 Faber 程式碼與主機提供者之間的 I/O 邊界。[閱讀更多 →](/features/frames.html)

## 內嵌測試 {#testing}

測試套件與原始碼並存，使用三個關鍵字：
`probandum`、`proba` 與 `adfirma`。不需要獨立的測試二進位檔。[閱讀更多 →](/features/testing.html)
