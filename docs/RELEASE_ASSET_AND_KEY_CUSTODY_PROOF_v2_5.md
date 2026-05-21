# Matrix Core Kernel v2.5 Release Asset and Key Custody Proof Plan

## Purpose

This document defines the remaining proof requirements before Matrix Core Kernel can be promoted from Level 6 candidate evidence component to a stronger release-readiness claim.

## Current verified evidence

- Live PR CI success exists.
- Workflow artifact generation exists.
- Clean install from workflow-generated source artifact exists.
- Installed-package CLI validation passed.
- Release-candidate manifest exists.
- Promotion dossier exists.

## Remaining blockers

1. Official GitHub Release asset publication.
2. SHA-256 verification of the published release asset.
3. External clean install from the official published release asset.
4. Production key custody evidence.
5. Optional independent external audit.
6. Optional production deployment evidence.

## Official release asset proof requirements

A valid release asset proof record must include:

- release tag
- release URL
- uploaded asset filename
- uploaded asset size
- uploaded asset SHA-256
- verifier identity or runner identity
- download timestamp
- hash verification command used
- hash verification result
- truth boundary statement

## External clean-install proof requirements

A valid clean-install proof from official release asset must include:

- fresh environment identifier
- Python version
- operating system / runner
- release asset URL
- asset SHA-256 verified before install
- install command
- import/version check
- CLI validation command outputs
- proof log SHA-256

## Production key custody proof requirements

A valid production key custody statement must include:

- key type and purpose
- custody owner or responsible role
- creation date
- storage location class, without leaking secrets
- signing authority policy
- rotation policy
- revocation policy
- incident response policy
- separation between development/test keys and production keys
- attestation that no private key material is committed to the repository

## Truth boundary

This document is a proof plan and template. It is not itself Level 6 proof, release publication proof, clean-install proof, production custody proof, external audit proof, or production deployment evidence.
