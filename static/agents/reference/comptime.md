# comptime

Computes a module constant's value at build time.

**Term** `praefixum` · **Section** KEYWORDS

## Syntax

```
const <type> <name> = comptime { … return <value> }
```

## What this teaches

- A `comptime { … }` body is the initializer of a module constant. It runs once, during the build, and `return`s the value; the program only ever sees the finished literal.
- The body is ordinary Faber: loops, `if`, locals, collections, class values, and calls to pure functions.
- Module constants may read other module constants; the build evaluates them in dependency order.

## Common mistakes

- Using `comptime` outside a constant initializer — it is legal only as the whole initializer of `const T NAME = comptime { … }` (module level or block level) or of a class field default.
- The retired `comptime(expr)` form — a plain expression needs no marker: `const int N = 4 * 1024` already folds at compile time.
- Reaching I/O, `call`, or async code — the build rejects the constant and names the call chain that got there.

## Grammar

```
fixum_decl     :← 'fixum' type_annotation IDENTIFIER '=' const_init
const_init     :← expression
praefixum_expr :← 'praefixum' block_stmt
```

## Expected output

```
praefixum.expected — the values computed at build time.
```

## Example

```fab
class Punctum {
    const int x
    const int y
}

fn quadratum(int n) → int {
    return n * n
}

# A loop that calls a pure function.
const int SUMMA_QUADRATORUM = comptime {
    var int total ← 0
    for range 1‥11 const i {
        total ← total + quadratum(i)
    }
    return total
}

# A collection built at build time.
const list<int> PRIMI = comptime {
    var list<int> found ← empty
    for range 2‥30 const n {
        var bool isPrime ← true
        for range 2 ‥ n const d {
            if n % d ≡ 0 {
                isPrime ← false
            }
        }
        if isPrime {
            found.append(n)
        }
    }
    return found
}

# Text and a class value.
const string LINEA = comptime {
    var string stripe ← ""
    for range 0‥8 const i {
        stripe ← stripe + "="
    }
    return stripe
}

const Punctum ORIGO = comptime {
    return Punctum { x = SUMMA_QUADRATORUM % 10, y = -3 }
}

# A plain module constant reading a build-time one folds after it.
const int DUPLEX = SUMMA_QUADRATORUM * 2

main {
    print SUMMA_QUADRATORUM
    print PRIMI
    print LINEA
    print ORIGO.x
    print ORIGO.y
    print DUPLEX
}
```

See also: [`static`](static.md), [`embed`](embed.md), [`return`](return.md).

Fetch list: https://faberlang.dev/agents/index.md
