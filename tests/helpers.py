from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_example_module(module_name: str, relative_path: str):
    for transient_module in ("state", "agents", "tools", "prompts"):
        sys.modules.pop(transient_module, None)

    module_path = REPO_ROOT / relative_path
    parent = str(module_path.parent)
    if parent not in sys.path:
        sys.path.insert(0, parent)

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module
