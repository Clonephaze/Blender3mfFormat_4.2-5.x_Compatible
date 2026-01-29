"""
Test runner for Blender 3MF addon unit test suite.

These tests run inside Blender's Python environment but mock specific
behaviors for isolation and faster execution.

Run with: blender --background --python tests/run_unit_tests.py
"""

import sys
import unittest
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Add unit tests directory to path
TESTS_DIR = Path(__file__).parent
UNIT_DIR = TESTS_DIR / "unit"
sys.path.insert(0, str(UNIT_DIR))

# Parse command line args for test filtering
pattern = "test_*.py"
if len(sys.argv) > 1 and "--" in sys.argv:
    idx = sys.argv.index("--")
    if len(sys.argv) > idx + 1:
        arg = sys.argv[idx + 1]
        pattern = arg if arg.endswith(".py") else arg + ".py"

print(f"Discovering unit tests matching: {pattern}")

# Discover and run tests
if __name__ == "__main__":
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.discover(str(UNIT_DIR), pattern=pattern)

    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print(f"✅ ALL UNIT TESTS PASSED: {result.testsRun} tests")
    else:
        print("❌ UNIT TESTS FAILED")
        print(f"   Ran: {result.testsRun}")
        print(f"   Failures: {len(result.failures)}")
        print(f"   Errors: {len(result.errors)}")
    print("=" * 70)

    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
