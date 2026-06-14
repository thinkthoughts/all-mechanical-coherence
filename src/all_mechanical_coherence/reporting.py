from pathlib import Path

from .paper import load_paper
from .engineering import load_statements


def build_summary(path: Path) -> str:
    paper = load_paper(path)
    statements = load_statements(path)

    lines = [
        f"# {paper.title}",
        "",
        f"arXiv: {paper.arxiv}",
        "",
        "## Engineering Statements",
        "",
    ]

    for statement in statements:
        lines.append(
            f"- [{statement.id}] {statement.statement}"
        )

    return "\n".join(lines)
