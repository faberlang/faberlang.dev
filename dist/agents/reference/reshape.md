# reshape

Captured backtick templates for bound payloads.

**Term** `reshape` · **Section** LITERALS

## Syntax

```
`template`(args)
```

## What this teaches

- backtick template syntax `template`(args) — captures template text and parameters into the builtin `forma` class
- indexed placeholders `§0` — an indexed hole selects its argument and may repeat with one value
- templates without holes for static text

## Common mistakes

- Expecting template application to render the string inline — \`...\`(args) captures into a forma class, it does not interpolate into a string.

## Expected output

```
Raw template text lines showing preserved § holes.
```

## Example

```fab
main {
    let string tenantId ← "tenant-42"
    let string plan ← "pro"
    let forma q ← `
        select id, email, plan
        from accounts
        where tenant_id = §
          and plan = §
    `(tenantId, plan)
    print q.template
    let forma indexed ← `where tenant_id = §0 or parent_tenant_id = §0`(tenantId)
    print indexed.template
    let forma bare ← `select 1`
    print bare.template
}
```

See also: [`format`](format.md), [`string (type)`](string (type).md).

Fetch list: https://faberlang.dev/agents/index.md
