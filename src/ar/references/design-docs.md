+++
translation_kind = "translated"

title = "Design documents"
section = "references"
order = 2
sources = [
  "radix/docs/design/README.md",
]


prose_hash = "sha256:c668ff445d22132defdedd2c1535366f6ce81513e0ae589bd1ab450683a06c3f"
code_hash = "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
source_commit = "593544bb65cdafba45a3a2c63b8c66148d65a4b3"
source_locale = "en-US"
+++
يحتوي مستودع Radix على وثائق التصميم المرجعية لكيفية عمل Faber
كلغة ومُصرّف. تقع هذه الوثائق تحت `radix/docs/design/`.

## الفهرس {#index}

| المجال | الملفات |
|------|-------|
| الأهداف والإنزال | `target-capability-matrix.md`، `lowering-routes.md`، `semantic-ownership.md` |
| الأنواع والسكر الصرفي | `numeric-type-sugar.md`، `comparison-operators.md`، `annotation-sugar.md` |
| دوال المجموعات الجوهرية | `lista-intrinsics.md`، `tabula-intrinsics.md`، `tensor-intrinsics.md`، `numerus-intrinsics.md`، `fractus-intrinsics.md`، `textus-intrinsics.md`، `intervallum-intrinsics.md`، `instans-intrinsics.md`، `copia-intrinsics.md` |
| التحويل | `conversio-valor.md`، `failable-conversio.md` |
| الأطر والتأثيرات | `frame-stream-types.md`، `host-provider-gateway.md` |
| القارئ والصياغة | `reader-locale.md`، `faber-canonical-surface.md` |
| الأنظمة / AIR | `air-dialect.md`، `aiml-foundation.md`، `systems-shaped-values.md` |
| سطح الأدوات | `faber-scripting.md` |
| الدَيْن التسميوي | `mixed-case-naming-debt.md` |

## وثائق تصميم المكتبة المعيارية {#stdlib-design-docs}

يحتوي الدليل `radix/docs/stdlib/` على:

| الوثيقة | الدور |
|-----|------|
| `morphologia.md` | سياسة التصريف لجميع أسماء دوال المكتبة المعيارية |
| `tensor-methods.md` | مرجع دوال المُستقبِل من نوع Tensor |
| `chorda-methods.md` | مرجع دوال Chorda (النص) |
| `mathesis-methods.md` | مرجع دوال الرياضيات |
| `tempus-methods.md` | مرجع دوال الزمن |
| `stdlib-mechanical-verbs.md` | سياسة الثالوث pange/solve/tempta |
