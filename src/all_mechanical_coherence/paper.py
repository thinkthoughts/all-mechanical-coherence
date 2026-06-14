import yaml
from pathlib import Path

from .schemas import Paper


def load_paper(path: Path) -> Paper:
    with open(path) as f:
        data = yaml.safe_load(f)

    return Paper(**data["paper"])
