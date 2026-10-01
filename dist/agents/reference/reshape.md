# reshape

Captured backtick templates for bound payloads.

**Term** `forma` · **Section** LITERALS

## Syntax

```
`template`(args)
```

## What this teaches

- backtick template syntax `template`(args) — captures template text and parameters into the builtin `forma` class
- indexed placeholders `§0` for repeated parameter references
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
    const string tenantId ← "tenant-42"
    const string plan ← "pro"
    const forma q ← `
        select id, email, plan
        from accounts
        where tenant_id = §
          and plan = §
    `(tenantId, plan)
    print q.template
    const forma indexed ← `where tenant_id = §0 or parent_tenant_id = §0`(tenantId, tenantId)
    print indexed.template
    const forma bare ← `select 1`
    print bare.template
}
```

See also: [`format`](format.md), [`string`](textus.md).

Fetch list: https://faberlang.dev/agents/index.md
