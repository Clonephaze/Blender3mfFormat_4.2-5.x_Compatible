# Contributing

Thanks for your interest in contributing to **Blender 3MF Format (Blender 4.2+ compatible fork)**.

This repository is a maintained modernization of the original add-on (created by Ghostkeeper) to keep it working on modern Blender versions. Contributions here focus on **correctness, compatibility, and keeping import/export behavior predictable**.

## Where development happens

Development and issue tracking happens in **this** repository:

- https://github.com/Clonephaze/Blender3mfFormat---4.2-compatible

If you’re looking for the historical upstream, see:

- https://github.com/Ghostkeeper/Blender3mfFormat

## What to contribute

Good contributions include:

- Fixes for Blender 4.2+ API changes / regressions
- 3MF import/export correctness fixes (especially edge cases)
- Test coverage (unit or integration)
- Documentation improvements
- Small quality-of-life improvements that don’t change file semantics

Non-goals (usually):

- “Opinionated” transformations of scene data on import/export
- Silent data loss or auto-fixing invalid files without clearly reporting it
- Large refactors without a clear benefit or test coverage

## Bug reports

Before opening a new issue, please search existing issues first.

When reporting a bug, include:

1. **Blender version** (e.g. 4.2.3 LTS / 4.3.x / 4.4.x)
2. **OS** (Windows/macOS/Linux) and relevant hardware notes
3. **Steps to reproduce** (a minimal, reliable recipe)
4. **Expected vs actual behavior**
5. **Logs / traceback** (copy/paste in the issue)
6. If relevant, a **minimal .3mf sample file**

If your file contains sensitive data, don’t post it publicly. Instead, try to reproduce the issue with a sanitized/minimal file.

## Feature requests

Feature requests are welcome, but please keep the scope aligned with the project:

- The add-on’s purpose is to **load and save 3MF files**.
- Changes that modify geometry/materials beyond what the format requires should be kept minimal.

When requesting a feature, describe:

- The user problem being solved
- Why it belongs in the add-on (vs being handled elsewhere)
- Any references to the 3MF spec or examples from other tools

## Pull requests

Pull requests are welcome.

### Basic workflow

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Run tests (see below)
5. Open a PR with a clear description and screenshots/files when relevant

### Testing requirements

This project has both **unit tests** and **integration tests**.

#### Unit tests (fast, no Blender required)

From the repository root:

```bash
python -m unittest test
```

These tests mock Blender’s API and validate internal logic.

#### Integration tests (runs inside Blender)

These tests run with a real Blender installation and validate end-to-end import/export behavior.

Windows:

```powershell
.\test\run_integration_tests.ps1
```

macOS/Linux:

```bash
./test/run_integration_tests.sh
```

There is also a newer pytest-based integration suite under `tests/` (recommended for end-to-end checks). See `tests/README.md` for details.

### Code style

- Follow [Blender’s Python style guide](https://wiki.blender.org/wiki/Style_Guide/Python)
- PEP-8 compatible
- Keep changes focused and readable
- Prefer adding tests for bug fixes and behavior changes

### Commit messages

Write meaningful commit messages. Avoid generic messages like “Update file” or “Fix stuff”.

Good examples:

- `Fix material slot indexing when exporting empty slots`
- `Update import operator for Blender 4.2 depsgraph API`

### Changelog

Please don’t update `CHANGES.md` unless you’re asked to. Maintainers will handle release notes.

## Reviewing PRs is also contributing

If you’re not ready to code, you can still help by:

- Trying the add-on on your Blender version and reporting results
- Testing PR branches
- Improving docs
- Sharing minimal repro files for tricky import/export bugs
