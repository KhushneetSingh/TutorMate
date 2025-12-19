import json
from typing import Dict, Any, List

from app.agents.base_agent import BaseAgent
from app.ai_client import generate_study_plan
from app.schemas.study_plan import StudyPlan


class PlannerAgent(BaseAgent):
    """
    PlannerAgent:
    Converts syllabus + constraints → structured study plan
    """

    def __init__(self, agent_id=None):
        super().__init__(role="study_planner", agent_id=agent_id)

    def execute(self, task: Dict[str, Any]) -> StudyPlan:
        prompt = self._prompt(task)
        raw = generate_study_plan(prompt)

        # HARD REQUIREMENT: JSON only
        plan_dict = json.loads(raw)
        plan = StudyPlan.model_validate(plan_dict)

        self.state["active_plan"] = plan.model_dump()
        return plan

    def _prompt(self, task: Dict[str, Any]) -> str:
        return f"""
You are a backend service.

Return ONLY valid JSON.
NO markdown. NO explanations. NO extra keys.

Schema:
{{
  "goal": string,
  "duration_days": number,
  "tasks": [
    {{
      "day": number,
      "topic": string,
      "objective": string,
      "resources": [string]
    }}
  ]
}}

User input:
Goal: {task["goal"]}
Topics: {task["topics"]}
Duration: {task["days_available"]} days
Daily hours: {task["daily_hours"]}

Rules:
- One task per day
- Cover all topics evenly
- Include revision and mock-test days
"""