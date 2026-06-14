import yaml
from pathlib import Path

from .schemas import SeminarQuestion


def load_questions(path: Path):
    with open(path) as f:
        data = yaml.safe_load(f)

    return [
        SeminarQuestion(question=q)
        for q in data["questions_for_seminar"]
    ]
