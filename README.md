# CodeBasir 🧠

> **Understand your code. Fix your errors.**

[![Tests](https://github.com/jmalkynj/codebasir/actions/workflows/tests.yml/badge.svg)](https://github.com/jmalkynj/codebasir/actions/workflows/tests.yml)
[![Release](https://img.shields.io/github/v/tag/jmalkynj/codebasir?label=release)](https://github.com/jmalkynj/codebasir/releases)
[![License](https://img.shields.io/github/license/jmalkynj/codebasir)](https://github.com/jmalkynj/codebasir/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)

CodeBasir is an open-source developer tool that helps programmers understand programming errors in a simple and clear way.

It analyzes error messages and provides explanations, possible causes, practical solutions, examples, severity levels, and traceback details.

## 🎯 Why CodeBasir?

Programming error messages can be difficult to understand, especially for beginners and developers who prefer simple explanations.

CodeBasir aims to make programming errors easier to understand by providing:

- Error type
- Clear explanation
- Possible cause
- Suggested solution
- Practical example
- Severity level
- Traceback file location
- Traceback line number
- Extracted error message

## 🚀 Project Status

CodeBasir is currently in the early development stage.

The first version focuses on analyzing common Python errors through a Python API and command-line interface (CLI).

## 🐍 Currently Supported Errors

The current version supports:

- `ModuleNotFoundError`
- `NameError`
- `SyntaxError`
- `TypeError`
- `ValueError`
- `IndexError`
- `KeyError`
- `AttributeError`

More error types and programming languages will be added in future releases.

## 🔍 Traceback Analysis

CodeBasir can also analyze Python traceback information.

For example:

```text
Traceback (most recent call last):
  File "/home/jamal/app.py", line 42, in <module>
    value = int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
```

CodeBasir can extract:

```text
Error type: ValueError
File: /home/jamal/app.py
Line: 42
Message: invalid literal for int() with base 10: 'hello'
```

This makes it easier to understand where an error happened and what caused it.

## 💡 Example

Given the following error:

```text
ModuleNotFoundError: No module named 'requests'
```

CodeBasir analyzes the error and provides information such as:

```text
Type: ModuleNotFoundError
Title: Module not found
Explanation: Python could not find the required library or module.
```

It can also provide a practical solution such as:

```bash
pip install requests
```

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/jmalkynj/codebasir.git
cd codebasir
```

Install the project:

```bash
python -m pip install -e .
```

To run the tests, install `pytest`:

```bash
python -m pip install pytest
```

## 💻 Command-Line Usage

After installation, run:

```bash
codebasir "NameError: name 'username' is not defined"
```

CodeBasir will analyze the error and display:

- Error type
- Explanation
- Possible cause
- Suggested solution
- Example
- Severity level
- File location when available
- Line number when available
- Extracted error message when available

## 🐍 Python Usage

CodeBasir can also be used directly from Python:

```python
from codebasir.analyzer import analyze_error

result = analyze_error(
    "NameError: name 'username' is not defined"
)

print(result)
```

For a complete traceback:

```python
from codebasir.analyzer import analyze_error

traceback_text = """
Traceback (most recent call last):
  File "/home/jamal/app.py", line 42, in <module>
    value = int("hello")
ValueError: invalid literal for int()
"""

result = analyze_error(traceback_text)

print(result["error_type"])
print(result["filename"])
print(result["line_number"])
print(result["error_message"])
```

## 🧪 Running Tests

Run the test suite with:

```bash
python -m pytest
```

The project uses GitHub Actions to automatically run tests across multiple Python versions.

## 📁 Project Structure

```text
codebasir/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── workflows/
│   │   └── tests.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── src/
│   └── codebasir/
│       ├── __init__.py
│       ├── analyzer.py
│       ├── cli.py
│       └── errors.py
├── tests/
│   ├── test_analyzer.py
│   └── test_cli.py
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
└── pyproject.toml
```

## 🗺️ Roadmap

### Phase 1 — Foundation

- [x] Python package structure
- [x] Error analyzer
- [x] Arabic error explanations
- [x] Command-line interface
- [x] Automated tests
- [x] GitHub Actions
- [x] MIT License

### Phase 2 — Error Knowledge Base

- [x] Add common Python errors
- [x] Improve error classification
- [x] Add practical examples
- [x] Add severity classification
- [x] Traceback file and line extraction
- [x] Error message extraction

### Phase 3 — Additional Programming Languages

- [ ] JavaScript
- [ ] TypeScript
- [ ] HTML/CSS
- [ ] JSON
- [ ] Git

### Phase 4 — Developer Experience

- [ ] English output
- [ ] Improved CLI interface
- [ ] Configuration options
- [ ] API interface
- [ ] Improved documentation

### Phase 5 — Community

- [x] Contribution guidelines
- [x] Issue templates
- [x] Pull request templates
- [x] Security policy
- [ ] Community-contributed error definitions

## 🤝 Contributing

Contributions are welcome.

You can help improve CodeBasir by:

- Adding new error definitions
- Improving Arabic explanations
- Adding tests
- Reporting bugs
- Suggesting new features
- Improving documentation

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a contribution.

## 🔐 Security

For information about reporting security vulnerabilities, please read [SECURITY.md](SECURITY.md).

## 📄 License

CodeBasir is open source software licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

**CodeBasir — Making programming errors easier to understand.**
