两个重要的转换运算符,一个用于运行时,一个用于编译时:

<<<FENCE 0>>>

## 运行时转换 — ↦ {#runtime-conversion}

使用 `↦` 进行运行时转换,尤其是可能失败的解析或强制转换。用 `⇥` 提供内联恢复:

<<<FENCE 1>>>

类型驱动的具象化:

<<<FENCE 2>>>

## 静态标注 — ∷ {#static-ascription}

使用 `∷` 进行显式静态类型标注。它是后置的,并且由目标类型驱动:

<<<FENCE 3>>>

## 空值合并 — vel {#nullish-coalescing}

当值为 `nihil` 时,使用 `vel` 进行空值合并:

<<<FENCE 4>>>
