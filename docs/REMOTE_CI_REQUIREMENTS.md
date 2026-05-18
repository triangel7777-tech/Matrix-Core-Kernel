# Remote CI Requirements

This document records the required GitHub Actions behavior for the Matrix Core Kernel remote executable spine.

## Required CI checks

1. Check out the pull request source.
2. Set up Python 3.11 or newer.
3. Install the package in editable mode.
4. Run the unit tests in `tests/`.
5. Run the Matrix Core CLI validator against `examples/complete_layered_structure_v0_2.json`.
6. Run the Matrix Core CLI policy validator against `examples/policies`.
7. Upload logs or retain workflow run evidence for import into the external proof dossier.

## Truth boundary

This Markdown file is a CI requirement record, not a live GitHub Actions workflow. Level 6 remains blocked until an actual repo-root workflow runs successfully and its evidence is imported.
