import os
import shutil
import uuid
from pathlib import Path

def ensure_dir(path):
    path = Path(path)
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def clear_dir(path):
    path = Path(path)
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)

def unique_run_dir(base_dir="runs"):
    run_id = str(uuid.uuid4())[:8]
    run_dir = Path(base_dir) / run_id
    ensure_dir(run_dir)
    return run_dir
