# Contributing to CIM Pattern

First off, **thank you** for considering contributing to CIM Pattern! This project exists because teams are drowning in information, and we need better cognitive operating systems.

This document will help you get started.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

---

## Code of Conduct

### Our Pledge

- **Be respectful** - Ideas are more important than egos
- **Be constructive** - "This doesn't work" + "here's why" + "here's a fix"
- **Be honest** - If something is broken, say it
- **Be collaborative** - This is peeragogy, not hierarchy

### Not Tolerated

- Personal attacks
- Trolling or harassment
- Publishing private information
- Corporate politeness that masks real problems

**Enforcement:** Violations will result in warnings → temporary ban → permanent ban.

**Report issues:** protocols@pyragogy.org

---

## How Can I Contribute?

### 🐛 Reporting Bugs

**Before submitting:**
- Check [existing issues](https://github.com/pyragogy/protocols/issues)
- Try the latest version
- Read the [FAQ](docs/FAQ.md)

**When submitting:**

Use this template:

```markdown
**Bug Description:**
[Clear, concise description]

**Steps to Reproduce:**
1. Calculate Zc with values X, Y
2. Run command Z
3. See error

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happened]

**Environment:**
- OS: [e.g., macOS 13.2]
- Python version: [e.g., 3.11.1]
- Tool: [CLI / Web calculator / Slack integration]

**Additional Context:**
[Screenshots, logs, etc.]
```

---

### 💡 Suggesting Features

**Good feature requests:**
- Solve a real problem you've experienced
- Include a use case
- Consider implementation complexity
- Align with project goals

**Template:**

```markdown
**Problem:**
[What pain point does this solve?]

**Proposed Solution:**
[Your idea]

**Alternatives Considered:**
[Other approaches you've thought about]

**Use Case:**
[Concrete example of how this would be used]
```

**Where to suggest:**
- Small features: [GitHub Issues](https://github.com/pyragogy/protocols/issues)
- Big features: [GitHub Discussions](https://github.com/pyragogy/protocols/discussions)

---

### 📖 Improving Documentation

Documentation improvements are **highly valued**. Look for:

- Typos and grammar
- Unclear explanations
- Missing examples
- Outdated information
- Translation opportunities

**Easy wins:**
- Add examples to existing docs
- Fix broken links
- Improve code comments
- Add screenshots/diagrams

**Process:**
1. Fork repo
2. Edit .md files
3. Submit PR with clear description

---

### 🔧 Contributing Code

We need help with:

**High Priority:**
- Curator AI implementation (Claude API integration)
- Notion/Linear plugins
- More language bindings (JS, Go, Rust)
- Test coverage
- CI/CD pipeline

**Medium Priority:**
- Dashboard visualizations
- Slack bot improvements
- Metrics collection automation
- Performance optimizations

**Low Priority:**
- Additional calculators
- Theme customizations
- Export formats

---

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- Text editor (VS Code recommended)
- (Optional) Node.js 18+ for web tools

### Setup Steps

1. **Fork and clone:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/protocols.git
   cd protocols
   ```

2. **Create branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Test existing tools:**
   ```bash
   # Test CLI
   python tools/zc-calculator/zc_cli.py --help
   
   # Test web calculator
   open tools/zc-calculator/index.html
   ```

4. **Make changes:**
   - Edit files
   - Add tests (if applicable)
   - Update documentation

5. **Test your changes:**
   ```bash
   # Run tests (when we have them)
   python -m pytest tests/
   
   # Manual testing
   python tools/zc-calculator/zc_cli.py --vgen 50 --bsocial 30
   ```

---

## Pull Request Process

### Before Submitting

- [ ] Code works locally
- [ ] Documentation updated (if needed)
- [ ] No new warnings/errors
- [ ] Follows style guidelines
- [ ] Added examples (if new feature)

### PR Template

```markdown
## Description
[What does this PR do?]

## Motivation
[Why is this change needed?]

## Changes Made
- [ ] Added feature X
- [ ] Fixed bug Y
- [ ] Updated docs Z

## Testing
[How did you test this?]

## Screenshots (if applicable)
[Add screenshots for UI changes]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
```

### Review Process

1. Maintainer reviews within 72 hours
2. Feedback provided (if needed)
3. You address feedback
4. Approved and merged

**Merge criteria:**
- Solves stated problem
- No breaking changes (or justified + documented)
- Code quality acceptable
- Documentation included

---

## Style Guidelines

### Python

**Follow PEP 8** with these preferences:
- Line length: 100 characters (not 80)
- Use type hints for function signatures
- Docstrings for all public functions
- Comments explain "why," not "what"

**Example:**

```python
def calculate_zc(v_generation: float, b_social: float) -> float:
    """
    Calculate Cognitive Impedance ratio.
    
    Args:
        v_generation: Information generation rate (items/hour)
        b_social: Social processing bandwidth (capacity/hour)
    
    Returns:
        Zc ratio (float)
    
    Raises:
        ValueError: If b_social is <= 0
    """
    if b_social <= 0:
        raise ValueError("B_social must be greater than 0")
    
    return v_generation / b_social
```

### JavaScript

**Modern ES6+:**
- Use `const`/`let`, not `var`
- Arrow functions preferred
- Template literals for strings
- Async/await over callbacks

**Example:**

```javascript
const calculateZc = (vGeneration, bSocial) => {
  if (bSocial <= 0) {
    throw new Error('B_social must be greater than 0');
  }
  return vGeneration / bSocial;
};
```

### Markdown

- Use ATX-style headers (`#` not underlines)
- Code blocks with language specification
- Tables for structured data
- Lists for sequential information

### Git Commits

**Format:**
```
[type]: [short description]

[optional body]
[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Examples:**

```
feat: add Notion plugin for Zc tracking

Implements real-time Zc monitoring in Notion databases.
Adds configuration UI and webhook handler.

Closes #42
```

```
fix: CLI calculator crash on zero B_social

Added validation check before division.
Returns clear error message.
```

---

## Community

### Where to Connect

- **GitHub Issues** - Bug reports, feature requests
- **GitHub Discussions** - Questions, ideas, showcases
- **Discord** - Real-time chat *(coming soon)*
- **Email** - protocols@pyragogy.org

### Getting Help

Stuck on something? Ask!

1. Check [docs/](docs/)
2. Search [existing issues](https://github.com/pyragogy/protocols/issues)
3. Ask in [Discussions](https://github.com/pyragogy/protocols/discussions)
4. Join Discord *(coming soon)*

### Recognition

Contributors are recognized in:
- [CONTRIBUTORS.md](CONTRIBUTORS.md)
- [CHANGELOG.md](CHANGELOG.md) (for significant contributions)
- GitHub Contributors page
- Project README (for major features)

---

## Project Priorities (Q1 2026)

### High Priority

1. **Curator AI** - Automated Zc monitoring
2. **Integration plugins** - Notion, Linear, Slack
3. **Test coverage** - Unit + integration tests
4. **Academic validation** - Partner with universities

### Medium Priority

1. **Dashboard** - Web-based metrics visualization
2. **Mobile support** - Responsive calculator
3. **Multi-language** - i18n for docs

### Low Priority

1. **Themes** - Dark mode, custom colors
2. **Export formats** - CSV, JSON, PDF
3. **Advanced analytics** - Trend prediction

---

## Questions?

- Read the [FAQ](docs/FAQ.md)
- Check [Discussions](https://github.com/pyragogy/protocols/discussions)
- Email: protocols@pyragogy.org

---

**Thank you for making CIM Pattern better!**

Every bug report, every doc fix, every feature—it all helps teams work better in the age of AI.

[← Back to README](README.md)
