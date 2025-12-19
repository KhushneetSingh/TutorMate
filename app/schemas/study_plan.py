from pydantic import BaseModel
from typing import List

class StudyTask(BaseModel):
    day: int
    topic: str
    objective: str
    resources: List[str]

class StudyPlan(BaseModel):
    goal: str
    duration_days: int
    tasks: List[StudyTask]