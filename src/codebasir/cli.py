"""Command-line interface for CodeBasir."""

from __future__ import annotations

import argparse

from .analyzer import analyze_error


def main() -> None:
    """Run CodeBasir from the command line."""
    parser = argparse.ArgumentParser(
        description="CodeBasir - Understand your code. Fix your errors."
    )

    parser.add_argument(
        "error",
        nargs="+",
        help="Programming error message to analyze.",
    )

    args = parser.parse_args()
    error_message = " ".join(args.error)

    result = analyze_error(error_message)

    print()
    print("🧠 CodeBasir")
    print("─" * 40)
    print(f"النوع: {result['error_type']}")
    print(f"العنوان: {result['title_ar']}")
    print(f"الشرح: {result['explanation_ar']}")

    if result.get("cause_ar"):
        print(f"السبب المحتمل: {result['cause_ar']}")

    if result.get("solution_ar"):
        print(f"الحل المقترح: {result['solution_ar']}")

    if result.get("example"):
        print(f"مثال: {result['example']}")

    print(f"الخطورة: {result['severity']}")
    print()


if __name__ == "__main__":
    main()
