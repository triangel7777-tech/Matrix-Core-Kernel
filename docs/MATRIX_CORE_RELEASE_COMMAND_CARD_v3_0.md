# Matrix Core Release Command Card v3.0

## Status

Matrix Core Kernel is currently a Level 6 candidate evidence component, not full Level 6.

The repository already has live CI evidence, workflow artifact evidence, clean-install evidence from a workflow-generated source artifact, a release workflow on main, manual release dispatch support, and proof schemas.

## Manual release execution

Run this manually in GitHub:

1. Open `triangel7777-tech/Matrix-Core-Kernel`.
2. Open Actions.
3. Select Matrix Core Release Asset.
4. Click Run workflow.
5. Select branch `main`.
6. Enter release tag `matrix-core-v2.7.0`.
7. Run the workflow.
8. Wait for success.

## Post-run verification

After the workflow completes, open the generated GitHub Release and download:

- release ZIP
- `release_asset.sha256`
- `release_asset_proof.json`

Verify that the downloaded release ZIP hash matches both proof files.

## Official-asset clean install

Use a fresh environment and install from the official published release asset, not from a workflow artifact. Record the environment, Python version, install command, installed package version, CLI validation outputs, and proof log hash.

## Required proof schemas

Complete these records after execution:

- `schemas/release_asset_proof_v2_5.schema.json`
- `schemas/official_asset_clean_install_proof_v2_5.schema.json`
- `schemas/production_key_custody_statement_v2_5.schema.json`

## Truth boundary

This command card is not release proof, full Level 6 proof, production deployment proof, external audit proof, empirical discovery proof, mathematical universality proof, or autonomous real-world operation proof.

Full Level 6 remains blocked until official release publication, published asset verification, official-asset clean install, and custody evidence are complete.
