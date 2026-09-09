"""Core error analyzer for CodeBasir."""

from __future__ import annotations

import re
from typing import Any

from .errors import ERRORS


def analyze_error(error_message: str) -> dict[str, Any]:
    """
    Analyze a programming error and return a structured explanation.

    Args:
        error_message: Raw error message.

    Returns:
        A dictionary containing the detected error and its explanation.
    """
    message = error_message.strip()

   if not message:
    return {
        "found": False,
        "error_type": None,
        "title_ar": "رسالة الخطأ فارغة",
        "explanation_ar": "أرسل رسالة خطأ حتى يتمكن CodeBasir من تحليلها.",
        "cause_ar": None,
        "solution_ar": None,
        "example": None,
        "severity": "unknown",
        "raw_error": "",
    }

    for error_type, details in ERRORS.items():
        if re.search(rf"\b{re.escape(error_type)}\b", message):
            return {
                "found": True,
                "error_type": error_type,
                "language": details["language"],
                "title_ar": details["title_ar"],
                "explanation_ar": details["explanation_ar"],
                "cause_ar": details["cause_ar"],
                "solution_ar": details["solution_ar"],
                "example": details["example"],
                "severity": details["severity"],
                "raw_error": message,
            }

    return {
        "found": False,
        "error_type": "Unknown",
        "title_ar": "خطأ غير معروف",
        "explanation_ar": (
            "لم يتعرف CodeBasir على نوع الخطأ حاليًا."
        ),
        "cause_ar": (
            "قد يكون الخطأ من نوع غير مضاف إلى قاعدة المعرفة بعد."
        ),
        "solution_ar": (
            "راجع رسالة الخطأ كاملة، ويمكن إضافة هذا النوع إلى قاعدة CodeBasir."
        ),
        "example": None,
        "severity": "unknown",
        "raw_error": message,
    }
