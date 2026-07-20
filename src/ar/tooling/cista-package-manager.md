+++
translation_kind = "translated"

title = "Cista package manager"
section = "tooling"
order = 3
sources = [
  "cista/README.md",
]


prose_hash = "sha256:05d23a68f89274ac712edd9df74eceb081ecb757827aedd26e944afc3a23ab42"
code_hash = "sha256:8911c196f515c978b54a345902a35f102715550c60930e2efee379e50e6c7c1e"
source_commit = "e9c6438e27c431907e3fd2e19282ba34d09e5a90"
source_locale = "en-US"
+++
كستا هو مدير حزم فابر. يتولى حل الحزم وإدارة التبعيات ومخزن الحزم العام.

## نظرة عامة {#overview}

يدير كستا حزم فابر المعرَّفة ببيانات `faber.toml`. تُعرِّف كل حزمة اسمها ونقطة دخولها ووجهة الترجمة الخلفية وتبعياتها.

## بيان الحزمة {#manifest}

```text
faber.toml

[nomen]
speculum-gen

[ingressus]
main.fab

[scopulus]
rust

[genus]
bin
```

حقل `[nomen]` هو اسم الحزمة، و`[ingressus]` هو وحدة نقطة الدخول، و`[scopulus]` يحدد هدف توليد الشيفرة، و`[genus]` يُعرِّف نوع الحزمة (`bin` للبرامج التنفيذية، `lib` للمكتبات).

## التبعيات {#dependencies}

تُعرِّف الحزم تبعيات يحلها كستا من مخزن الحزم. يُنتج حل التبعيات ملف قفل يضمن بناءات قابلة للتكرار.

## الحالة {#status}

كستا قيد التطوير النشط. سجل الحزم العام (`cista.dev`) حملة منفصلة عن تنفيذ الموقع. يعمل حل الحزم المحلي للحزم داخل مساحة العمل نفسها.
