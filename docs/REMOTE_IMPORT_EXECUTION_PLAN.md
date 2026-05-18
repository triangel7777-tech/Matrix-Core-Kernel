# Matrix Core Kernel Remote Import Execution Plan

## Objective

Import the Matrix Core Kernel source distribution into this repository and execute the external proof path without overclaiming validation.

## Current remote state

- Repository: `triangel7777-tech/Matrix-Core-Kernel`
- Remote branch for initial import scaffold: `import-matrix-core-v1-2`
- Current local artifact: `matrix_core_kernel_v1_2.zip`
- Current claim level: Level 5 local deterministic validation plus remote marker/issue evidence
- Level 6: not claimed

## Required source import

The full source tree should be imported from `matrix_core_kernel_v1_2.zip`, including:

- `pyproject.toml`
- `src/matrix_core_kernel/`
- `.github/workflows/`
- `tests/`
- `examples/`
- `docs/`
- `reports/`
- release and checksum manifests

## External proof path

1. Import the repository-ready source tree.
2. Run GitHub Actions CI on pull request.
3. Merge only after CI passes.
4. Publish a release asset.
5. Verify release asset SHA-256.
6. Run clean install from published release asset.
7. Import CI, release, and clean-install evidence.
8. Build promotion dossier.
9. Evaluate Level 6 candidate gate.

## Truth boundary

This plan is not proof of external validation. Level 6 remains blocked until live CI, release asset verification, external clean-install proof, and production key custody evidence exist.
