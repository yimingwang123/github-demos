---
applyTo: "**/*.py"
---
# GitHub Copilot Demo Project - AI Agent Instructions

## Project Overview

This is a **demonstration project** designed to showcase GitHub Copilot capabilities. The codebase intentionally contains issues (see `calculator.py`) for demonstrating AI-assisted fixes. The project structure follows GitHub best practices with CI/CD, Issue templates, and MCP integration.

**Key Files:**
- `calculator.py` - Core logic (intentionally has bugs for demo purposes)
- `tests/test_calculator.py` - pytest test suite
- `.vscode/mcp.json` - GitHub MCP Server configuration
- `.github/workflows/test.yml` - CI/CD with multi-version Python testing
- `DEMO_GUIDE.md` - Step-by-step demonstration instructions

## Architecture & Design Decisions

### Intentional "Flaws" (Do Not Auto-Fix Without Context)
The project contains deliberate issues for demonstration:
- `divide()` function lacks zero-division handling (Issue #1 demonstration)
- Functions missing type hints (Issue #2 demonstration)
- Incomplete test coverage for edge cases (Issue #3 demonstration)

**Before fixing**: Check if the user wants to preserve demo state or implement production fixes.

## Development Workflows

### Setup & Testing
```bash
# Initial setup (automated)
./setup.sh  # Creates venv, installs deps, runs tests

# Manual testing
source venv/bin/activate
pytest tests/ -v --cov=. --cov-report=term-missing
```

### GitHub Integration via MCP
This project uses MCP Server for GitHub integration. To interact with GitHub Issues/PRs:
```
@github List open issues in yimingwang123/github-demos
@github Create PR to fix issue #1
```

**MCP Configuration**: `.vscode/mcp.json` requires GitHub PAT with `repo`, `read:user`, `read:project` scopes.

## Code Conventions

### Python Standards
- **Type Hints**: All production functions require type annotations
  ```python
  def add(a: int | float, b: int | float) -> int | float:
  ```
- **Docstrings**: Use Google-style docstrings for all public functions
- **Error Handling**: Raise `ValueError` with descriptive messages (e.g., divide-by-zero)
- **PEP 8**: 4-space indentation, 2 blank lines between functions, sorted imports

### Testing Patterns (pytest)
- Test files: `tests/test_*.py`
- Coverage requirement: Each function needs ≥3 test cases (normal, edge, error)
- Example from `test_calculator.py`:
  ```python
  def test_add():
      assert add(2, 3) == 5      # Normal case
      assert add(-1, 1) == 0     # Edge: negatives
      assert add(0, 0) == 0      # Edge: zeros
  ```

### Commit Message Format
Follows `.github/instructions/commit.instructions.md`:
```
特性: Add type hints to calculator functions
修复文件: calculator.py

修复: Handle division by zero error
修复文件: calculator.py, tests/test_calculator.py
```

## CI/CD Integration

GitHub Actions workflow (`.github/workflows/test.yml`) runs on:
- Push to `main` or `develop` branches
- Pull requests targeting those branches
- Tests against Python 3.9, 3.10, 3.11
- Generates coverage reports (uploads to Codecov on Python 3.11)

## Project-Specific Patterns

### Demo Mode vs. Production Mode
- **Demo Mode** (default): Preserve intentional bugs for demonstration
- **Production Mode**: Apply fixes when user explicitly requests or creates PR

### Issue-Driven Development
Reference `ISSUE_TEMPLATES.md` and `DEMO_GUIDE.md` for typical workflows:
1. List issues via `@github`
2. Analyze issue context
3. Implement fix with tests
4. Create PR with descriptive commit message

### Dependencies
- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting
- No external calculation libraries (intentionally simple for demos)