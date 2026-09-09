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
}
