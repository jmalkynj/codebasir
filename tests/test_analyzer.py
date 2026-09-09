from src.codebasir.analyzer import analyze_error


def test_module_not_found_error():
    result = analyze_error(
        "ModuleNotFoundError: No module named 'requests'"
    )

    assert result["found"] is True
    assert result["error_type"] == "ModuleNotFoundError"
    assert "requests" in result["example"]


def test_name_error():
    result = analyze_error(
        "NameError: name 'username' is not defined"
    )

    assert result["found"] is True
    assert result["error_type"] == "NameError"


def test_syntax_error():
    result = analyze_error(
        "SyntaxError: invalid syntax"
    )

    assert result["found"] is True
    assert result["error_type"] == "SyntaxError"


def test_unknown_error():
    result = analyze_error(
        "SomeNewError: something went wrong"
    )

    assert result["found"] is False
    assert result["error_type"] == "Unknown"


def test_empty_error():
    result = analyze_error("")

    assert result["found"] is False
    assert result["error_type"] is None
