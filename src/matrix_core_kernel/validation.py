from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Set

REQUIRED_LAYER_IDS = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
REQUIRED_VALIDATION_GATES = [
    "finite_horizon_required",
    "ledger_required",
    "truth_label_required",
    "admission_gate_required",
]

@dataclass
class ValidationIssue:
    code: str
    message: str
    severity: str = "error"

@dataclass
class ValidationResult:
    ok: bool = True
    issues: List[ValidationIssue] = field(default_factory=list)

    def add(self, code: str, message: str, severity: str = "error") -> None:
        self.issues.append(ValidationIssue(code, message, severity))
        if severity == "error":
            self.ok = False

    def as_dict(self) -> Dict[str, Any]:
        return {
            "ok": self.ok,
            "issue_count": len(self.issues),
            "issues": [issue.__dict__ for issue in self.issues],
        }

def load_json(path: str | Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def validate_cls_schema(data: Dict[str, Any]) -> ValidationResult:
    result = ValidationResult()
    if data.get("truth_label") != "symbolic_master_layer_schema":
        result.add("truth_label", "CLS schema requires truth_label=symbolic_master_layer_schema")
    layers = data.get("layers")
    if not isinstance(layers, list):
        result.add("layers", "layers must be a list")
        return result
    ids: Set[int] = set()
    for layer in layers:
        if not isinstance(layer, dict):
            result.add("layer_record", "each layer must be an object")
            continue
        if "id" not in layer:
            result.add("layer_id", "layer missing id")
            continue
        ids.add(layer["id"])
        if not layer.get("name"):
            result.add("layer_name", f"layer {layer.get('id')} missing name")
        if not layer.get("core_function"):
            result.add("layer_core_function", f"layer {layer.get('id')} missing core_function")
    missing = [layer_id for layer_id in REQUIRED_LAYER_IDS if layer_id not in ids]
    if missing:
        result.add("missing_layers", f"missing required layer ids: {missing}")
    return result

def validate_layer_policy(data: Dict[str, Any]) -> ValidationResult:
    result = ValidationResult()
    if data.get("truth_label") != "symbolic_layer_policy":
        result.add("truth_label", "policy requires truth_label=symbolic_layer_policy")
    if "layer_id" not in data:
        result.add("layer_id", "policy missing layer_id")
    gates = data.get("validation_gates")
    if not isinstance(gates, list):
        result.add("validation_gates", "validation_gates must be a list")
        return result
    for gate in REQUIRED_VALIDATION_GATES:
        if gate not in gates:
            result.add("missing_gate", f"policy missing required gate: {gate}")
    return result

def validate_policy_directory(path: str | Path) -> ValidationResult:
    path = Path(path)
    result = ValidationResult()
    files = sorted(path.glob("layer_*_policy.json")) + sorted(path.glob("layer_minus*_policy.json"))
    if not files:
        result.add("policy_files", "no policy files found")
        return result
    seen = set()
    for file_path in files:
        data = load_json(file_path)
        child = validate_layer_policy(data)
        layer_id = data.get("layer_id")
        if layer_id in seen:
            result.add("duplicate_layer", f"duplicate policy for layer {layer_id}")
        seen.add(layer_id)
        for issue in child.issues:
            result.add(f"{file_path.name}:{issue.code}", issue.message, issue.severity)
    missing = [layer_id for layer_id in REQUIRED_LAYER_IDS if layer_id not in seen]
    if missing:
        result.add("missing_policy_layers", f"missing policy layers: {missing}")
    return result

def validate_by_name(data: Dict[str, Any]) -> ValidationResult:
    if data.get("name") in {"complete_layered_structure_v0_2", "matrix_complete_layered_structure_v0_2"}:
        return validate_cls_schema(data)
    if data.get("truth_label") == "symbolic_layer_policy":
        return validate_layer_policy(data)
    result = ValidationResult()
    result.add("unknown_schema", "unknown schema type")
    return result
