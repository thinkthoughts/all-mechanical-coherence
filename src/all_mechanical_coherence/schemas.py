from pydantic import BaseModel
from typing import List, Optional


class Paper(BaseModel):
    title: str
    arxiv: str
    url: str
    html: Optional[str] = None
    year: Optional[int] = None


class EngineeringStatement(BaseModel):
    id: str
    category: str
    statement: str


class SeminarQuestion(BaseModel):
    question: str
