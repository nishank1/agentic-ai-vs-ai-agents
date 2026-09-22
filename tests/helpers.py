from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_example_module(module_name: str, relative_path: str):
    saved_modules = {
        transient_module: sys.modules.get(transient_module)
        for transient_module in ("state", "agents", "tools", "prompts")
    }
    original_named_module = sys.modules.get(module_name)
    original_sys_path = list(sys.path)

    for transient_module in ("state", "agents", "tools", "prompts"):
        sys.modules.pop(transient_module, None)

    module_path = REPO_ROOT / relative_path
    parent = str(module_path.parent)
    if parent not in sys.path:
        sys.path.insert(0, parent)

    try:
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path[:] = original_sys_path
        if original_named_module is None:
            sys.modules.pop(module_name, None)
        else:
            sys.modules[module_name] = original_named_module
        for transient_module, original_module in saved_modules.items():
            if original_module is None:
                sys.modules.pop(transient_module, None)
            else:
                sys.modules[transient_module] = original_module
