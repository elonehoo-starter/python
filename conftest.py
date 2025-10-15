# Ensure pytest can import local packages in monorepo without installation.
import sys
from pathlib import Path
from glob import glob


def pytest_sessionstart(session):  # noqa: ARG001 (pytest hook signature)
    root = Path(__file__).resolve().parent
    for src in glob(str(root / "packages" / "*" / "src")):
        if src not in sys.path:
            sys.path.insert(0, src)
    for app_src in glob(str(root / "apps" / "*" / "src")):
        if app_src not in sys.path:
            sys.path.insert(0, app_src)
