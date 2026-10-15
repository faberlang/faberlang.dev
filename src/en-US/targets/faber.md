+++
title = "Faber"
section = "targets"
order = 73
sources = []
+++

Canonical re-emission — the compiler printing the program back.

Part of the [HIR lane](/targets/hir.html). Every panel below is compiler output.

## How to read it {#reading}

The round trip. Reader-locale spellings and formatting normalise to the canonical surface, which is how a program written in one locale can be reviewed in another.

## Measured support {#support}

| Capable | Analyzable | Coverage |
|---|---|---|
| 431 | 431 | 100% |

From the [target matrix](/toolchain/target-matrix.html): how many corpus exempla lower to this target. Coverage is not a quality score — an emitter can lower a term and still erase a distinction.

No measured gaps in the scored sections.

## Typed tensors {#tensores}

Builds two shaped matrices, multiplies them, and reduces the product to a scalar. Exercises shape-bearing types and a reduction.

**Faber source**

```faber locale-tabs
incipit {
    sit lista<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    sit lista<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    sit tf32[2, 3] a ← flat_a ↦ tf32[2, 3]
    sit tf32[3, 4] b ← flat_b ↦ tf32[3, 4]
    sit tf32[2, 4] product ← a.matmul(b)
    sit f32 mean ← product.media()
    nota mean
}
```

**Faber** — 9 lines in, 9 out (1.0×)

```faber locale=la
incipit {
    sit lista<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    sit lista<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    sit tf32[2, 3] a ← flat_a ↦ tf32[2, 3]
    sit tf32[3, 4] b ← flat_b ↦ tf32[3, 4]
    sit tf32[2, 4] product ← a.matmul(b)
    sit f32 mean ← product.media()
    nota mean
}
```

## The error channel {#fallibilis}

A function that may fail, and a caller that catches. Shows how the `⇥` channel becomes each target's own error idiom.

**Faber source**

```faber locale-tabs
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}

incipit {
    fac {
        nota divide(10, 2)
    }
    cape err {
        mone err
    }
}
```

**Faber** — 13 lines in, 13 out (1.0×)

```faber locale=la
functio divide(numerus a, numerus b) → numerus ⇥ textus {
    si b ≡ 0 ergo iace "division by zero"
    redde a / b
}

incipit {
    fac {
        nota divide(10, 2)
    }
    cape err {
        mone err
    }
}
```

## Collections and iteration {#collectiones}

A list folded to a total with `itera ex`. The plainest possible read on how loops lower.

**Faber source**

```faber locale-tabs
functio summa(lista<numerus> numeri) → numerus {
    varia numerus total ← 0
    itera ex numeri sit n {
        total ← total + n
    }
    redde total
}

incipit {
    sit lista<numerus> valores ← [1, 2, 3, 4, 5]
    nota summa(valores)
}
```

**Faber** — 12 lines in, 12 out (1.0×)

```faber locale=la
functio summa(lista<numerus> numeri) → numerus {
    varia numerus total ← 0
    itera ex numeri sit n {
        total ← total + n
    }
    redde total
}

incipit {
    sit lista<numerus> valores ← [1, 2, 3, 4, 5]
    nota summa(valores)
}
```

---

[All targets](/targets/) · [Measured support per term](/toolchain/target-matrix.html)
