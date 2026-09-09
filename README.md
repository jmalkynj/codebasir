# CodeBasir 🧠

> **Understand your code. Fix your errors.**

CodeBasir is an open-source developer tool that helps programmers understand programming errors in a simple and clear way.

It analyzes error messages and provides explanations, possible causes, practical solutions, examples, and severity levels.

## 🎯 Why CodeBasir?

Programming error messages can be difficult to understand, especially for beginners and developers who prefer simple explanations.

CodeBasir aims to make programming errors easier to understand by providing:

- Error type
- Clear explanation
- Possible cause
- Suggested solution
- Practical example
- Severity level

## 🚀 Project Status

CodeBasir is currently in the early development stage.

The first version focuses on analyzing common Python errors through a Python API and command-line interface (CLI).

## 🐍 Currently Supported Errors

The current version supports:

- `ModuleNotFoundError`
- `NameError`
- `SyntaxError`

More error types and programming languages will be added in future releases.

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

## 🐍 Python Usage

CodeBasir can also be used directly from Python:

```python
from codebasir.analyzer import analyze_error

result = analyze_error(
    "NameError: name 'username' is not defined"
)

print(result)
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
│   └── workflows/
│       └── tests.yml
├── src/
│   └── codebasir/
│       ├── __init__.py
│       ├── analyzer.py
│       ├── cli.py
│       └── errors.py
├── tests/
│   └── test_analyzer.py
├── LICENSE
├── pyproject.toml
└── README.md
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

- [ ] Add more Python errors
- [ ] Improve error classification
- [ ] Add more practical examples
- [ ] Improve severity classification

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

- [ ] Contribution guidelines
- [ ] Issue templates
- [ ] Pull request templates
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

Please open an issue or submit a pull request to contribute.

## 📄 License

CodeBasir is open source software licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

**CodeBasir — Making programming errors easier to understand.**
