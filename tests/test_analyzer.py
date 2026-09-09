from codebasir.cli import main


def test_cli_known_error(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["codebasir", "NameError: name 'username' is not defined"],
    )

    main()

    output = capsys.readouterr().out

    assert "NameError" in output
    assert "الاسم غير معروف" in output
    assert "الحل المقترح" in output


def test_cli_unknown_error(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["codebasir", "SomeNewError: something went wrong"],
    )

    main()

    output = capsys.readouterr().out

    assert "Unknown" in output
    assert "خطأ غير معروف" in output


def test_cli_empty_error(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["codebasir", ""],
    )

    main()

    output = capsys.readouterr().out

    assert "رسالة الخطأ فارغة" in output
    assert "unknown" in output


def test_cli_traceback(capsys, monkeypatch):
    traceback_text = (
        'Traceback (most recent call last):\n'
        '  File "/home/jamal/app.py", line 42, in <module>\n'
        '    value = int("hello")\n'
        'ValueError: invalid literal for int() with base 10: \'hello\''
    )

    monkeypatch.setattr(
        "sys.argv",
        ["codebasir", traceback_text],
    )

    main()

    output = capsys.readouterr().out

    assert "ValueError" in output
    assert "الخطأ" in output or "القيمة" in output
    assert "/home/jamal/app.py" in output
    assert "42" in output
