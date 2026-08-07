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

## Typed tensors {#tensores}

Builds two shaped matrices, multiplies them, and reduces the product to a scalar. Exercises shape-bearing types and a reduction.

**Faber source**

```faber
incipit {
    fixum lista<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    fixum lista<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    fixum tf32[] seed ← vacua
    fixum tf32[2, 3] a ← seed.strue(flat_a, [2, 3])
    fixum tf32[3, 4] b ← seed.strue(flat_b, [3, 4])
    fixum tf32[2, 4] product ← a.matmul(b)
    fixum f32 mean ← product.media()
    nota mean
}
```

**Faber** — 10 lines in, 10 out (1.0×)

```faber
incipit {
    fixum lista<f32> flat_a ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    fixum lista<f32> flat_b ← [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
    fixum tf32[] seed ← vacua
    fixum tf32[2, 3] a ← seed.strue(flat_a, [2, 3])
    fixum tf32[3, 4] b ← seed.strue(flat_b, [3, 4])
    fixum tf32[2, 4] product ← a.matmul(b)
    fixum f32 mean ← product.media()
    nota mean
}
```

## The error channel {#fallibilis}

A function that may fail, and a caller that catches. Shows how the `⇥` channel becomes each target's own error idiom.

**Faber source**

```faber
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

```faber
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

```faber
functio summa(lista<numerus> numeri) → numerus {
    varia numerus total ← 0
    itera ex numeri fixum n {
        total ← total + n
    }
    redde total
}

incipit {
    fixum lista<numerus> valores ← [1, 2, 3, 4, 5]
    nota summa(valores)
}
```

**Faber** — 12 lines in, 12 out (1.0×)

```faber
functio summa(lista<numerus> numeri) → numerus {
    varia numerus total ← 0
    itera ex numeri fixum n {
        total ← total + n
    }
    redde total
}

incipit {
    fixum lista<numerus> valores ← [1, 2, 3, 4, 5]
    nota summa(valores)
}
```

---

[All lanes](/targets/) · [Measured support per term](/toolchain/target-matrix.html)
