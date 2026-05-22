# Matrix Core Kernel v2.8 Official Release Dispatch Handoff

## Purpose

This handoff defines the exact final manual execution needed to move from Level 6 candidate evidence component toward full release-asset proof.

## Confirmed state before this handoff

- Live PR CI success exists.
- Workflow artifact generation exists.
- Clean install from workflow-generated source artifact exists.
- Installed-package CLI validation passed.
- Release-candidate manifest exists.
- Promotion dossier exists.
- Release/key-custody proof contracts exist.
- Release workflow exists on `main` and supports manual dispatch with a required `release_tag` input.

## Manual GitHub UI execution

1. Open the repository: `triangel7777-tech/Matrix-Core-Kernel`.
2. Go to **Actions**.
3. Select workflow: **Matrix Core Release Asset**.
4. Choose **Run workflow**.
5. Use branch: `main`.
6. Enter release tag:

```text
matrix-core-v2.7.0
```

7. Run the workflow.
8. Wait for completion.
9. Open the generated GitHub Release.
10. Download all release assets:
    - release ZIP
    - `release_asset.sha256`
    - `release_asset_proof.json`

## Required verification after workflow completes

Compute SHA-256 of the published release ZIP and compare it to `release_asset.sha256` and `release_asset_proof.json`.

Required result:

```text
published_asset_sha256 == release_asset.sha256 == release_asset_proof.asset_sha256
```

## Required official-asset clean install

Use a fresh environment and install from the published GitHub Release ZIP, not from a workflow artifact.

Required checks:

```text
python -m venv official_release_venv
./official_release_venv/bin/python -m pip install --upgrade pip
./official_release_venv/bin/python -m pip install <published_release_zip_url_or_downloaded_zip>
./official_release_venv/bin/matrix-core validate examples/complete_layered_structure_v0_2.json
./official_release_venv/bin/matrix-core validate-all examples/policies
```

## Required evidence records

Complete these schemas after execution:

- `schemas/release_asset_proof_v2_5.schema.json`
- `schemas/official_asset_clean_install_proof_v2_5.schema.json`
- `schemas/production_key_custody_statement_v2_5.schema.json`

## Truth boundary

This handoff does not itself prove official release publication, published asset hash verification, official-asset clean install, production key custody, external audit, production deployment, empirical discovery, mathematical universality, or autonomous real-world operation.

Full Level 6 remains unclaimed until completed evidence records are produced, committed, and verified.
