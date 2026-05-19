from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from matrix_core_kernel.validation import load_json, validate_cls_schema, validate_policy_directory


class MatrixCoreRemoteSpineTests(unittest.TestCase):
    def test_cls_has_all_layers(self):
        data = load_json(ROOT / "examples" / "complete_layered_structure_v0_2.json")
        result = validate_cls_schema(data)
        self.assertTrue(result.ok, result.as_dict())
        self.assertEqual({layer["id"] for layer in data["layers"]}, {-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

    def test_policy_directory_validates(self):
        result = validate_policy_directory(ROOT / "examples" / "policies")
        self.assertTrue(result.ok, result.as_dict())

    def test_cli_validate_cls(self):
        completed = subprocess.run(
            [sys.executable, "-m", "matrix_core_kernel.cli", "validate", str(ROOT / "examples" / "complete_layered_structure_v0_2.json")],
            cwd=ROOT,
            env={"PYTHONPATH": str(ROOT / "src")},
            text=True,
            capture_output=True,
            timeout=20,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_cli_validate_all(self):
        completed = subprocess.run(
            [sys.executable, "-m", "matrix_core_kernel.cli", "validate-all", str(ROOT / "examples" / "policies")],
            cwd=ROOT,
            env={"PYTHONPATH": str(ROOT / "src")},
            text=True,
            capture_output=True,
            timeout=20,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
