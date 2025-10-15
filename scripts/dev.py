#!/usr/bin/env python3
"""Dev helper to run services/modules with monorepo paths bootstrapped.

Usage examples:
  python scripts/dev.py apps/example-service/src/example_service/main.py
  python scripts/dev.py -m example_service.main
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path
from glob import glob


# def _bootstrap_monorepo_paths() -> None:
#     root = Path(__file__).resolve().parent.parent
#     for src in glob(str(root / "packages" / "*" / "src")):
#         if src not in sys.path:
#             sys.path.insert(0, src)
#     for app_src in glob(str(root / "apps" / "*" / "src")):
#         if app_src not in sys.path:
#             sys.path.insert(0, app_src)


def main(argv: list[str] | None = None) -> int:
    # _bootstrap_monorepo_paths()
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print("Usage: python scripts/dev.py [-m module] <path-or-args>")
        return 2
    if argv[0] == "-m":
        if len(argv) < 2:
            print("-m requires a module name")
            return 2
        mod = argv[1]
        sys.argv = [mod] + argv[2:]
        runpy.run_module(mod, run_name="__main__")
        return 0
    else:
        path = Path(argv[0]).resolve()
        sys.argv = [str(path)] + argv[1:]
        runpy.run_path(str(path), run_name="__main__")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
