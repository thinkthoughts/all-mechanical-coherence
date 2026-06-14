import yaml
from pathlib import Path

from .schemas import EngineeringStatement


def load_statements(path: Path):
    with open(path) as f:
        data = yaml.safe_load(f)

    return [
        EngineeringStatement(**item)
        for item in data["engineering_statements"]
    ]
