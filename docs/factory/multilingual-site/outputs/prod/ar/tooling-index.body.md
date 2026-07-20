تغطي سلسلة أدوات Faber ثلاث أدوات: واجهة سطر الأوامر `faber` للبناء
والاختبار، ومترجم Radix لتوليد الشفرات، ومدير الحزم Cista لحل التبعيات.

## أداة بناء Faber {#faber-cli}

واجهة المطور الرئيسية. بناء وتحقق وتشغيل واختبار وتنسيق وشرح —
كل ذلك عبر أمر واحد. [اقرأ المزيد ←](/tooling/faber-build-tool.html)

## مترجم Radix {#radix}

خلفية المترجم. يُنزِل مصدر Faber عبر HIR ← MIR ← AIR إلى
مسارات أهداف متعددة. [اقرأ المزيد ←](/tooling/radix-compiler.html)

## مدير حزم Cista {#cista}

حل الحزم ومستودع الحزم العمومي. يدير بيانات `faber.toml`
وأقفال التبعيات. [اقرأ المزيد ←](/tooling/cista-package-manager.html)

## أهداف توليد الشفرات {#codegen-targets}

يُترجم Faber إلى Rust (افتراضي) وWASM وTypeScript وGo وGPU/WGSL.
لكل مسار هدف مسار IR الخاص به وربط وقت تشغيل خاص به.
[اقرأ المزيد ←](/tooling/codegen-targets.html)

## الأداء {#performance}

أداء مقاس للترجمة والتنفيذ عبر مسارات الأهداف.
[اقرأ المزيد ←](/tooling/performance.html)

## البرمجة النصية {#scripting}

استخدام Faber كلغة برمجة نصية بأمر `faber run`.
[اقرأ المزيد ←](/tooling/scripting.html)
