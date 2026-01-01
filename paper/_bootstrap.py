import sys
from pathlib import Path


def bootstrap_asymptoticFunction():
    here = Path(__file__).resolve()
    repo_root = here.parents[1]  # unbounded-experiments/

    cfg = repo_root / ".asymptotic_function_path"

    if not cfg.exists():
        raise RuntimeError(
            "Missing .asymptotic_function_path file.\n"
            "Create one containing the path to asymptoticFunction."
        )

    repo_path = Path(cfg.read_text().strip())

    if not repo_path.exists():
        raise FileNotFoundError(
            f"Invalid path in .asymptotic_function_path:\n{repo_path}"
        )

    sys.path.insert(0, str(repo_path))
