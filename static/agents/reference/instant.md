# instant

Absolute point-in-time primitive with precision contract.

**Term** `instans` · **Section** KEYWORDS

## Syntax

```
instant | instant<ms> | instant<us> | instant<ns>
```

## What this teaches

- Absolute point-in-time primitive with precision contract.
- Related keywords: ↦, ⊥, string

## Common mistakes

- Using `instant ∷ T` (static ascription) instead of `instant ↦ T` (runtime conversion) — use `↦` for runtime datetime parsing and extraction (SEM016).

## Grammar

```
instans | instans<ms> | instans<us> | instans<ns>
tempus.now() → instans<ns>; downconvert at use site
valor ↦ instans<N> | instans ↦ textus
```

## Expected output

```
Smoke asserts exit 0 only.
```

## Example

```fab
import from "norma:time" tempus

fn epoch_wire(instant t) → string {
    return t ↦ string
}

main {
    # --- precision declarations from canonical nanosecond wall clock ---
    let instant<ns> nanos ← tempus.now()
    let instant secunda ← nanos ↦ instant
    let instant<ms> millis ← nanos ↦ instant<ms>
    let instant<us> micros ← nanos ↦ instant<us>

    # --- value ↦ instant: UTC wire and numeric offset normalize to same instant ---
    let value utc ← "1979-05-27T07:32:00Z"
    let value offset ← "1979-05-27T03:32:00-04:00"
    let instant parsed ← utc ↦ instant
    let instant normalized ← offset ↦ instant
    assert parsed ≡ normalized panic "offset ingest normalizes to UTC instant"

    # --- microsecond wire extracted from a value at declared precision ---
    let value carrier ← "1979-05-27T07:32:00.123456Z"
    let instant<us> fromToml ← carrier ↦ instant<us>
    assert (fromToml ↦ string) ≡ "1979-05-27T07:32:00.123456Z" panic "emit honors micros contract"

    # --- precision-tagged equality: distinct at ns, equal at ms ---
    let value leftWire ← "1979-05-27T07:32:00.123456Z"
    let value rightWire ← "1979-05-27T07:32:00.123999Z"
    let instant<ns> left ← leftWire ↦ instant<ns>
    let instant<ns> right ← rightWire ↦ instant<ns>
    assert left ≢ right panic "sub-millisecond bits differ at nanosecond precision"
    let instant<ms> leftMs ← left ↦ instant<ms>
    let instant<ms> rightMs ← right ↦ instant<ms>
    assert leftMs ≡ rightMs panic "same millisecond at declared ms precision"

    # --- cross-precision conversion: widen and narrow with observable truncation ---
    let instant<ns> fine ← parsed ↦ instant<ns>
    let instant<ms> coarse ← fine ↦ instant<ms>
    let instant seconds ← fine ↦ instant
    assert (seconds ↦ string) ≡ "1979-05-27T07:32:00Z" panic "narrow to seconds strips sub-second wire"
    let instant<ms> wider ← secunda ↦ instant<ms>
    assert wider ≤ millis panic "cross-precision comparison at coarser operand"

    # --- wire emit and parse-back through a value (same instant) ---
    let string wire ← epoch_wire(parsed)
    let value replayCarrier ← "1979-05-27T07:32:00Z"
    let instant roundtrip ← replayCarrier ↦ instant
    assert roundtrip ≡ parsed panic "wire parse-back matches UTC value extract"
    assert wire ≡ "1979-05-27T07:32:00Z" panic "seconds-precision wire emit"
    print wire, secunda, millis, micros, nanos, fromToml, coarse
}
```

See also: [`↦`](↦.md), [`⊥`](⊥.md), [`string`](textus.md).

Fetch list: https://faberlang.dev/agents/index.md
