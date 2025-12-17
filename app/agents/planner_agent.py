from typing import Dict, Any, List
from datetime import datetime, timedelta

from app.agents.base_agent import BaseAgent
from app.ai_client import generate_study_plan


class PlannerAgent(BaseAgent):
    """
    PlannerAgent:
    - creates a structured study plan
    - adapts plan based on progress
    """

    def _execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        input_data example:
        {
          "goal": "Prepare for Mobile Forensics exam",
          "topics": ["Android Security", "Traffic Analysis", "Evidence Extraction"],
          "days_available": 14,
          "daily_hours": 2
        }
        """

        goal = input_data["goal"]
        topics = input_data["topics"]
        days = input_data["days_available"]
        hours = input_data["daily_hours"]

        prompt = self._build_prompt(goal, topics, days, hours)

        plan_text = generate_study_plan(prompt)

        structured_plan = self._structure_plan(
            topics=topics,
            days=days,
            hours=hours
        )

        self.state["current_plan"] = {
            "goal": goal,
            "plan_text": plan_text,
            "schedule": structured_plan,
            "created_at": datetime.utcnow().isoformat()
        }

        return self.state["current_plan"]

    def _build_prompt(self, goal, topics, days, hours) -> str:
        return f"""
You are an expert study planner.

Goal: {goal}
Topics: {topics}
Total days: {days}
Hours per day: {hours}

Create a clear, day-wise study plan with:
- daily goals
- revision slots
- mock test days
"""

    def _structure_plan(self, topics: List[str], days: int, hours: int):
        """
        Deterministic fallback structure
        (important: product reliability)
        """
        plan = []
        start_date = datetime.utcnow().date()

        topic_index = 0
        for day in range(days):
            plan.append({
                "day": day + 1,
                "date": str(start_date + timedelta(days=day)),
                "topic": topics[topic_index],
                "hours": hours
            })
            topic_index = (topic_index + 1) % len(topics)

        return plan