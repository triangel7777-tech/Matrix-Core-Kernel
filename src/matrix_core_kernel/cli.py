from __future__ import annotations

import argparse
import json
from pathlib import Path

from .validation import load_json, validate_by_name, validate_policy_directory


def _print_result(result) -> int:
    print(json.dumps(result.as_dict(), indent=2))
    return 0 if result.ok else 1


def cmd_validate(args: argparse.Namespace) -> int:
    return _print_result(validate_by_name(load_json(args.path)))


def cmd_validate_all(args: argparse.Namespace) -> int:
    return _print_result(validate_policy_directory(args.policy_dir))


def cmd_report(args: argparse.Namespace) -> int:
    data = load_json(args.path)
    result = validate_by_name(data)
    text = ["# Matrix Core Kernel Validation Report", "", f"Schema: `{data.get('name', '<unknown>')}`", f"Status: `{'PASS' if result.ok else 'FAIL'}`", ""]
    if result.issues:
        text.append("## Issues")
        for issue in result.issues:
            text.append(f"- **{issue.severity.upper()} {issue.code}:** {issue.message}")
    else:
        text.append("No validation issues detected.")
    text.append("\nTruth boundary: this validates local schema structure only; it does not prove Level 6 readiness or mathematical universality.\n")
    rendered = "\n".join(text)
    if args.out:
        Path(args.out).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)
    return 0 if result.ok else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="matrix-core")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("validate")
    p.add_argument("path")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("validate-all")
    p.add_argument("policy_dir")
    p.set_defaults(func=cmd_validate_all)

    p = sub.add_parser("report")
    p.add_argument("path")
    p.add_argument("--out")
    p.set_defaults(func=cmd_report)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
