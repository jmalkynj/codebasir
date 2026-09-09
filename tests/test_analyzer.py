from codebasir.analyzer import analyze_error


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


def test_type_error():
    result = analyze_error(
        "TypeError: unsupported operand type(s)"
    )

    assert result["found"] is True
    assert result["error_type"] == "TypeError"
    assert result["severity"] == "medium"


def test_value_error():
    result = analyze_error(
        "ValueError: invalid literal for int()"
    )

    assert result["found"] is True
    assert result["error_type"] == "ValueError"


def test_index_error():
    result = analyze_error(
        "IndexError: list index out of range"
    )

    assert result["found"] is True
    assert result["error_type"] == "IndexError"


def test_key_error():
    result = analyze_error(
        "KeyError: 'email'"
    )

    assert result["found"] is True
    assert result["error_type"] == "KeyError"


def test_attribute_error():
    result = analyze_error(
        "AttributeError: 'str' object has no attribute 'uppercase'"
    )

    assert result["found"] is True
    assert result["error_type"] == "AttributeError"


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
    assert result["severity"] == "unknown"
