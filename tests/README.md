# Blender 3MF Format - Test Suite

This directory contains all tests for the Blender 3MF addon, organized into two categories:

- **`unit/`** - Unit tests that test individual functions with mocked data
- **`integration/`** - Integration tests that use the real Blender `bpy` API

All tests run through Blender's Python environment using `blender --background --python`.

## 🚀 Quick Start

### Run All Tests (185 tests)
```powershell
# Run ALL tests - unit + integration (recommended)
python tests/run_all_tests.py

# Or run separately:
blender --background --python tests/run_unit_tests.py    # Unit tests (130, ~0.5s)
blender --background --python tests/run_tests.py         # Integration tests (55, ~3s)
```

### Run Specific Test Modules
```powershell
# Smoke tests only (fast)
blender --background --python tests/run_tests.py -- test_smoke

# Export tests only
blender --background --python tests/run_tests.py -- test_export

# Import tests only
blender --background --python tests/run_tests.py -- test_import

# Unicode tests only
blender --background --python tests/run_tests.py -- test_unicode
```

## 📋 Test Coverage

### Unit Tests (`tests/unit/`) - 130 tests
- **`test_export_unit.py`** - Export logic (materials, transforms, vertices, triangles)
- **`test_import_unit.py`** - Import logic (parsing, content types, materials)
- **`test_metadata.py`** - Metadata storage and retrieval
- **`test_preferences.py`** - Addon preferences handling

### Integration Tests (`tests/integration/`) - 55 tests
- **`test_smoke.py`** - Fast sanity checks (8 tests)
- **`test_export.py`** - Full export workflows (17 tests)
- **`test_import.py`** - Import and roundtrips (11 tests)
- **`test_unicode.py`** - Unicode handling (18 tests) - Chinese, Japanese, Korean, emoji

**Total: 185 tests**

## 📁 Structure

```
tests/
├── run_all_tests.py      # ⭐ Combined test runner (runs both suites)
├── run_tests.py          # Integration test runner
├── run_unit_tests.py     # Unit test runner
├── README.md
├── unit/                 # Unit tests
│   ├── mock/             # Mock helpers
│   │   └── bpy.py
│   ├── test_export_unit.py
│   ├── test_import_unit.py
│   ├── test_metadata.py
│   └── test_preferences.py
├── integration/          # Integration tests
│   ├── test_base.py      # Base test class
│   ├── test_smoke.py
│   ├── test_export.py
│   ├── test_import.py
│   └── test_unicode.py
└── resources/            # Test data files
    ├── only_3dmodel_file.3mf
    ├── corrupt_archive.3mf
    └── empty_archive.zip
```

## 🔧 Requirements

1. **Blender 4.2+** installed
2. **No external dependencies** - uses only Python/Blender built-ins (unittest)

## 🎯 Running Specific Tests

```powershell
# Run specific test file
blender --background --python tests/run_tests.py -- test_export

# Run single test class
python -m unittest tests.test_export.ExportMaterialTests

# Run single test method
python -m unittest tests.test_export.ExportMaterialTests.test_export_with_none_material

# Note: unittest discovery requires Blender in background mode
```

## 🧪 Test Coverage

Current integration test coverage (36 tests):

### Smoke Tests (8 tests, <2s)
- ✅ Blender version check
- ✅ Addon import and registration
- ✅ Operators available
- ✅ Basic export/import
- ✅ Scene cleanup
- ✅ Material helpers

### Export Tests (17 tests)
- ✅ Basic export (cube, multiple objects, empty scene)
- ✅ Materials (single, multiple, None slots, mixed)
- ✅ Archive structure (valid ZIP, XML, vertices, triangles)
- ✅ Transformations (location, rotation, scale, parent-child)
- ✅ Edge cases (non-mesh objects, no faces)
- ✅ Options (selection only, modifiers)

### Import & Roundtrip Tests (11 tests)
- ✅ Basic import (valid files, errors, corrupt files)
- ✅ Roundtrips (geometry, materials, dimensions preserved)
- ✅ API compatibility (PrincipledBSDFWrapper, depsgraph, loop_triangles)

## 📊 Test Philosophy

### Integration vs Unit

**These tests (tests/)**: Validate **user-facing behavior**
- Test through public Blender operators (`bpy.ops.export_mesh.threemf()`)
- Verify end-to-end workflows work correctly
- Catch regressions in real-world usage
- Run slower (~1.5s) but always accurate

**Legacy tests (test/)**: Validate **implementation details**
- Test internal methods (`unit_scale()`, `read_content_types()`, etc.)
- Use mocks because operators can't be directly instantiated
- Verify edge cases in parsers/formatters
- Run fast (<0.1s) but artificial

### Why Both?

Import3MF and Export3MF are Blender operators (bpy_struct) - they can't be instantiated like `Export3MF()` outside of Blender's operator system. Internal methods testing requires the legacy mock-based approach in `test/`.

## 🐛 Debugging Failed Tests

```powershell
# Run with verbose output and full tracebacks
.\tests\run_pytest.ps1 -Verbose

# Run Blender in foreground to see graphics (if needed)
blender --python tests/run_pytest.py -- -v -s tests/test_export.py::test_failing_test
```

## 🔄 Relationship with Legacy Tests

The `test/` directory (legacy unit tests) and `tests/` directory (integration tests) serve **complementary purposes**:

| Aspect | Legacy (`test/`) | Integration (`tests/`) |
|--------|------------------|------------------------|
| **What** | Internal implementation | User-facing functionality |
| **How** | Mocked bpy | Real bpy in Blender |
| **Speed** | Very fast (~0.5s total) | Slower (~1.5s total) |
| **Coverage** | 158 tests, edge cases | 36 tests, workflows |
| **When** | Algorithm development | Pre-commit validation |

**Use both**: Run legacy tests for quick iteration, integration tests before committing.

## 📚 Resources

- [pytest documentation](https://docs.pytest.org/)
- [Blender Python API](https://docs.blender.org/api/current/)
- [pytest markers](https://docs.pytest.org/en/stable/example/markers.html)
- [pytest fixtures](https://docs.pytest.org/en/stable/fixture.html)

## 🤝 Contributing

When adding new tests:

1. Use descriptive test names: `test_export_with_empty_material_slots`
2. Add appropriate markers: `@pytest.mark.material`
3. Use fixtures for setup/teardown
4. Write docstrings explaining what's being tested
5. Test edge cases and error conditions

For questions or issues, check the main project README or open an issue.
