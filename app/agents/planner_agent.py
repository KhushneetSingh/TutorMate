from typing import Dict, Any, List
from datetime import datetime, timedelta

from app.agents.base_agent import BaseAgent
from app.ai_client import generate_study_plan


class PlannerAgent(BaseAgent):
    """
    PlannerAgent:
    Converts syllabus + constraints → adaptive study plan
    """

    def __init__(self, agent_id=None):
        super().__init__(role="study_planner", agent_id=agent_id)

    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        goal = task["goal"]
        topics = task["topics"]
        days = task["days_available"]
        hours = task["daily_hours"]

        prompt = self._prompt(goal, topics, days, hours)
        ai_plan = generate_study_plan(prompt)

        schedule = self._build_schedule(topics, days, hours)

        plan = {
            "goal": goal,
            "ai_plan": ai_plan,
            "schedule": schedule,
            "created_at": datetime.utcnow().isoformat(),
        }

        self.state["active_plan"] = plan
        return plan

    def _prompt(self, goal, topics, days, hours):
        return f"""
You are an expert academic planner.

Goal: {goal}
Topics: {topics}
Available days: {days}
Hours per day: {hours}

Generate a realistic day-wise study plan.
Include revision and mock-test days.
"""

    def _build_schedule(self, topics: List[str], days: int, hours: int):
        start = datetime.utcnow().date()
        plan = []

        for i in range(days):
            plan.append({
                "day": i + 1,
                "date": str(start + timedelta(days=i)),
                "topic": topics[i % len(topics)],
                "hours": hours,
            })

        return plan