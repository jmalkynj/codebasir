"""Built-in explanations for common programming errors."""

ERRORS = {
    "ModuleNotFoundError": {
        "language": "python",
        "type": "ModuleNotFoundError",
        "title_ar": "لم يتم العثور على الوحدة",
        "explanation_ar": (
            "Python لم يتمكن من العثور على المكتبة أو الوحدة المطلوبة."
        ),
        "cause_ar": (
            "غالبًا المكتبة غير مثبتة أو أن اسم الوحدة مكتوب بشكل غير صحيح."
        ),
        "solution_ar": (
            "ثبّت المكتبة المطلوبة باستخدام pip، ثم أعد تشغيل البرنامج."
        ),
        "example": "pip install requests",
        "severity": "medium",
    },
    "NameError": {
        "language": "python",
        "type": "NameError",
        "title_ar": "الاسم غير معروف",
        "explanation_ar": (
            "Python حاول استخدام متغير أو دالة أو اسم غير معرّف."
        ),
        "cause_ar": (
            "قد يكون الاسم مكتوبًا بشكل خاطئ أو لم يتم تعريفه قبل استخدامه."
        ),
        "solution_ar": (
            "تأكد من كتابة الاسم بشكل صحيح وتعريفه قبل استخدامه."
        ),
        "example": "print(username)",
        "severity": "medium",
    },
    "SyntaxError": {
        "language": "python",
        "type": "SyntaxError",
        "title_ar": "خطأ في صياغة الكود",
        "explanation_ar": (
            "Python لم يستطع فهم صياغة الكود."
        ),
        "cause_ar": (
            "قد يكون هناك قوس أو نقطتان أو علامة اقتباس مفقودة أو صياغة غير صحيحة."
        ),
        "solution_ar": (
            "راجع السطر المشار إليه في رسالة الخطأ وتأكد من صحة الصياغة."
        ),
        "example": "if user_logged_in:",
        "severity": "high",
    },
    "TypeError": {
        "language": "python",
        "type": "TypeError",
        "title_ar": "نوع البيانات غير صحيح",
        "explanation_ar": (
            "Python حاول تنفيذ عملية باستخدام نوع بيانات غير مناسب."
        ),
        "cause_ar": (
            "قد تحاول جمع أو مقارنة أو استخدام أنواع بيانات لا تدعم هذه العملية."
        ),
        "solution_ar": (
            "تأكد من أنواع البيانات وحوّلها إلى النوع المطلوب قبل تنفيذ العملية."
        ),
        "example": "age + '20'",
        "severity": "medium",
    },
    "ValueError": {
        "language": "python",
        "type": "ValueError",
        "title_ar": "قيمة غير صالحة",
        "explanation_ar": (
            "النوع المطلوب صحيح، لكن القيمة التي تم تقديمها غير مناسبة."
        ),
        "cause_ar": (
            "قد تكون القيمة خارج النطاق المتوقع أو لا يمكن تحويلها بالشكل المطلوب."
        ),
        "solution_ar": (
            "تحقق من القيمة قبل استخدامها وتأكد من توافقها مع العملية المطلوبة."
        ),
        "example": "int('hello')",
        "severity": "medium",
    },
    "IndexError": {
        "language": "python",
        "type": "IndexError",
        "title_ar": "الفهرس خارج النطاق",
        "explanation_ar": (
            "تمت محاولة الوصول إلى عنصر في قائمة أو مجموعة باستخدام فهرس غير موجود."
        ),
        "cause_ar": (
            "الفهرس أكبر من عدد العناصر أو أصغر من الحد المسموح."
        ),
        "solution_ar": (
            "تأكد من أن الفهرس ضمن حدود القائمة أو استخدم التحقق من طولها أولًا."
        ),
        "example": "items[10]",
        "severity": "medium",
    },
    "KeyError": {
        "language": "python",
        "type": "KeyError",
        "title_ar": "المفتاح غير موجود",
        "explanation_ar": (
            "تمت محاولة الوصول إلى مفتاح غير موجود داخل قاموس."
        ),
        "cause_ar": (
            "قد يكون اسم المفتاح مكتوبًا بشكل خاطئ أو لم تتم إضافته إلى القاموس."
        ),
        "solution_ar": (
            "تحقق من وجود المفتاح قبل الوصول إليه أو استخدم dict.get()."
        ),
        "example": "user['email']",
        "severity": "medium",
    },
    "AttributeError": {
        "language": "python",
        "type": "AttributeError",
        "title_ar": "الخاصية أو الدالة غير موجودة",
        "explanation_ar": (
            "تمت محاولة استخدام خاصية أو دالة غير موجودة في الكائن."
        ),
        "cause_ar": (
            "قد يكون اسم الخاصية خاطئًا أو أن نوع الكائن لا يدعم هذه الخاصية."
        ),
        "solution_ar": (
            "تحقق من نوع الكائن واسم الخاصية أو الدالة التي تحاول استخدامها."
        ),
        "example": "name.uppercase()",
        "severity": "medium",
    },
}
