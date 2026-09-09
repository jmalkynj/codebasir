"""Core error analyzer for CodeBasir."""

from __future__ import annotations

import re
from typing import Any, Dict, Optional

from .errors import ERRORS


def _detect_error_type(message: str) -> Optional[str]:
    """Detect a known error type from a raw error message."""
    for error_type in ERRORS:
        pattern = rf"(?<![A-Za-z0-9_]){re.escape(error_type)}(?![A-Za-z0-9_])"

        if re.search(pattern, message):
            return error_type

    return None


def _extract_location(message: str) -> Dict[str, Any]:
    """Extract the file path and line number from a Python traceback."""
    matches = re.findall(
        r'File "([^"]+)", line (\d+)',
        message,
    )

    if not matches:
        return {
            "filename": None,
            "line_number": None,
        }

    filename, line_number = matches[-1]

    return {
        "filename": filename,
        "line_number": int(line_number),
    }


def _extract_error_message(message: str, error_type: str) -> Optional[str]:
    """Extract the text that follows a known error type."""
    pattern = rf"(?m)^\s*{re.escape(error_type)}:\s*(.+)$"
    match = re.search(pattern, message)

    if not match:
        return None

    return match.group(1).strip()


def analyze_error(error_message: str) -> Dict[str, Any]:
    """
    Analyze a programming error and return a structured explanation.

    Args:
        error_message: Raw error message.

    Returns:
        A dictionary containing the detected error and its explanation.
    """
    if error_message is None:
        message = ""
    else:
        message = str(error_message).strip()

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
            "filename": None,
            "line_number": None,
            "error_message": None,
            "raw_error": "",
        }

    location = _extract_location(message)
    error_type = _detect_error_type(message)

    if error_type:
        details = ERRORS[error_type]

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
            "filename": location["filename"],
            "line_number": location["line_number"],
            "error_message": _extract_error_message(
                message,
                error_type,
            ),
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
        "filename": location["filename"],
        "line_number": location["line_number"],
        "error_message": None,
        "raw_error": message,
    }
