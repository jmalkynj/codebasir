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


def test_none_error():
    result = analyze_error(None)

    assert result["found"] is False
    assert result["error_type"] is None
    assert result["severity"] == "unknown"


def test_error_type_inside_larger_word_is_not_detected():
    result = analyze_error(
        "MyTypeErrorHandler: something went wrong"
    )

    assert result["found"] is False
    assert result["error_type"] == "Unknown"


def test_traceback_location_and_message():
    result = analyze_error(
        'Traceback (most recent call last):\n'
        '  File "/home/jamal/app.py", line 42, in <module>\n'
        '    value = int("hello")\n'
        'ValueError: invalid literal for int() with base 10: \'hello\''
    )

    assert result["found"] is True
    assert result["error_type"] == "ValueError"
    assert result["filename"] == "/home/jamal/app.py"
    assert result["line_number"] == 42
    assert "invalid literal for int()" in result["error_message"]


def test_traceback_uses_last_location():
    result = analyze_error(
        'Traceback (most recent call last):\n'
        '  File "/home/jamal/main.py", line 10, in <module>\n'
        '    helper()\n'
        '  File "/home/jamal/helper.py", line 27, in helper\n'
        '    items[10]\n'
        'IndexError: list index out of range'
    )

    assert result["found"] is True
    assert result["error_type"] == "IndexError"
    assert result["filename"] == "/home/jamal/helper.py"
    assert result["line_number"] == 27
    assert result["error_message"] == "list index out of range"
