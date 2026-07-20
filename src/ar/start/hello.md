+++
translation_kind = "translated"

title = "Hello, Faber"
section = "hello"
order = 2
sources = []

prose_hash = "sha256:3a78129bf3787f7c726e39104c95fe9bde78855c4a9f63650410c5cef9610067"
code_hash = "sha256:1ee50be729b09d1bfba27a1f994ef4d1a47c73a645764f9d5986c9bab1aecfb8"
source_commit = "6572815c8c5595e60956471d75c4a60e67cba58f"
source_locale = "en-US"
+++
اكتب أصغر برنامج Faber مفيد: نقطة دخول حزمة تقوم بتنسيق نص وطباعته.

## المتطلبات الأساسية {#prerequisites}

أكمل [التثبيت والتحميل](/start/install.html) أولاً. ينبغي أن يكون لديك ثنائي `faber` في `PATH` وطرفية في دليل عمل يمكنك إنشاء ملفات فيه.

## إنشاء حزمة {#create-package}

```bash
mkdir salve-munde
cd salve-munde
mkdir src
cat > faber.toml <<'EOF'
[package]
name = "salve-munde"
version = "0.1.0"
EOF
cat > src/main.fab <<'EOF'
functio salve(textus nomen) → textus {
    fixum textus msg ← "Salve, §!"(nomen)
    redde msg
}

incipit {
    fixum textus m ← salve("munde")
    nota m
}
EOF
```

## التحقق منها {#check}

```bash
faber check .
```

يقوم `faber check` بتشغيل الواجهة الأمامية: التحليل المعجمي، والتحليل النحوي، وفحص الأنواع، والتبسيط بقدر كافٍ لاكتشاف أخطاء الحزمة الاعتيادية دون بناء ثنائي أصلي. إذا فشل الأمر، اقرأ رمز التشخيص أولاً؛ صُممت تشخيصات Faber لتكون مقابض بحث مستقرة.

## تشغيله {#run}

```bash
faber run .
```

الناتج المتوقع:

```text
Salve, munde!
```

## ما استخدمته للتو {#what-you-used}

| المصدر | المعنى |
|---|---|
| `functio salve(textus nomen) → textus` | دالة باسم `salve`، معامل نوعه نصي أولاً، إرجاع نصي |
| `fixum textus msg ← ...` | ربط غير قابل للتغيير |
| `"Salve, §!"(nomen)` | سلسلة منسقة مع استيفاء عرضي |
| `redde msg` | إرجاع القيمة |
| `incipit` | نقطة دخول الحزمة |
| `nota m` | طباعة قيمة (ملاحظة/ناتج) |

## إثبات اللغة {#locale-proof}

البرنامج أعلاه هو العرض المرجعي باللاتينية. يمكن لعروض القارئ تقديم نفس البرنامج الدلالي بحزم كلمات مفتاحية مختلفة مع الحفاظ على الرموز والمعرّفات. ابدأ بالإثبات الكامل في [لغة القارئ](/features/reader-locale.html) قبل كتابة حزم غير لاتينية.

## التالي {#next}

| السابق | التالي |
|---|---|
| [التثبيت والتحميل](/start/install.html) | [الأوامر التي ستستخدمها](/start/commands.html) |
