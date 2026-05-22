# Matrix Core Kernel v3.1 Post-Release Evidence Intake

## Purpose

This document defines how to import and verify evidence after the official `Matrix Core Release Asset` workflow is manually run.

## Expected release run

Repository: `triangel7777-tech/Matrix-Core-Kernel`

Workflow: `Matrix Core Release Asset`

Branch: `main`

Release tag:

```text
matrix-core-v2.7.0
```

## Required files from generated GitHub Release

Download these files from the official GitHub Release:

1. release ZIP
2. `release_asset.sha256`
3. `release_asset_proof.json`

## Hash verification

Compute SHA-256 for the downloaded release ZIP and verify it matches both proof files.

Required equality:

```text
sha256(downloaded_release_zip) == release_asset.sha256 == release_asset_proof.asset_sha256
```

## Official-asset clean install check

Use a fresh environment and install from the official published release ZIP.

Required proof fields:

- environment identifier
- operating system / runner
- Python version
- release asset URL or downloaded filename
- verified SHA-256
- install command
- installed package version
- CLI validation results
- proof log SHA-256

## Required CLI validations

After installing from the official release ZIP, run:

```text
matrix-core validate examples/complete_layered_structure_v0_2.json
matrix-core validate-all examples/policies
```

Both must return `ok: true` and `issue_count: 0`.

## Evidence files to complete

Complete records conforming to:

```text
schemas/release_asset_proof_v2_5.schema.json
schemas/official_asset_clean_install_proof_v2_5.schema.json
schemas/production_key_custody_statement_v2_5.schema.json
```

## Promotion rule

Full Level 6 remains blocked unless all of the following are present:

- official GitHub Release asset publication
- published release asset SHA-256 verification
- official-asset clean install proof
- production key custody statement

## Truth boundary

This intake document is not release proof. It only defines how release proof must be collected and validated.
