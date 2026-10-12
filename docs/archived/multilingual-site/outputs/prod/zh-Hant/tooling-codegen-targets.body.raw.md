Faber 只有一種語言，卻有許多編譯契約。並非每項功能都必須降階至每個目標。本頁說明各目標支援、消除、警告或拒絕哪些功能。

## 政策動詞 {#policy-verbs}

| 動詞 | 意義 |
|------|---------|
| **Support** | 以預期語意進行降階 |
| **Erase** | 通過型別檢查；程式碼生成會捨棄目標特定語意 |
| **Warn** | 合法的 Faber；在該目標上沒有作用，或行為有所降級 |
| **Reject** | 檢查或輸出會失敗，並提供明確診斷 |
| **Defer** | 可解析／繫結；尚未為任何目標實作降階 |
| **Limited** | 具有明確子集閘門的穩定契約 |

## 目標表 {#target-table}

| 目標 | 途徑 | 建置 | 執行 | 套件 | 政策 |
|--------|------|-------|-----|---------|--------|
| `rust` | HIR | yes | yes | yes | **Support** |
| `fmir-text` | MIR | yes | yes | yes | **Support** |
| `fmir` | MIR | yes | yes | yes | **Support** |
| `fmir-bin` | MIR | yes | yes | yes | **Support** |
| `faber` | HIR | yes | no | no | **Support** |
| `ts` | HIR | yes | no | no | **Probe** |
| `go` | HIR | yes | no | no | **Erase** |
| `wasm` | MIR | yes | no | no | **Limited** |
| `wasm-text` | MIR | yes | no | no | **Limited** |
| `llvm-text` | MIR | yes | no | no | **Limited** |
| `metal-text` | MIR | yes | no | no | **Limited** |
| `wgsl-text` | MIR | yes | no | no | **Limited** |
| `sexp` | MIR | yes | no | no | **Limited** |

## 管線路由 {#pipeline-routing}

<<<FENCE 0>>>

## 應用程式途徑（HIR） {#application-lane-hir}

| 目標 | 實測下限 |
|--------|---------------|
| Rust | 生產路徑。借用模式、CLI 生成、可失敗的 Result 降階。 |
| Faber | 標準來源檢視／往返轉換。不是執行後端。 |
| TypeScript | 已分析 288/318 · 型別檢查有效 268/318 · 可執行 262/318 |
| Go | 通過 146/216。借用模式會被消除；`ad` 會被拒絕。 |

## 系統途徑（MIR） {#systems-lane-mir}

| 目標 | 實測下限 |
|--------|---------------|
| fmir* | 套件 MIR 映像；執行器證明來源獨立性。 |
| wasm | 已輸出 200/289 · 驗證通過 195/289 · 樣板主機可執行 171/289 |
| llvm-text | 已輸出 249/289 · 驗證器有效 232/289 · 可執行 65/289 |
| metal-text | 裝置安全的核心子集；88 項聚焦測試。活動已暫停。 |
| wgsl-text | 使用 naga 30.x 驗證。87 項聚焦測試。反射旁載檔。 |
| sexp | 已輸出 193 · Racket 編譯 190 · Racket 執行 190。驗證目標。 |

如需即時能力旗標，請執行 `faber targets`。
