from app.agents.planner_agent import PlannerAgent

if __name__ == "__main__":
    agent = PlannerAgent()

    plan = agent.run({
        "goal": "Prepare for Mobile Forensics exam",
        "topics": [
            "Android Security",
            "Traffic Analysis",
            "Evidence Extraction"
        ],
        "days_available": 14,
        "daily_hours": 2
    })

    print("\n====== FINAL STUDY PLAN ======\n")
    print(plan.model_dump_json(indent=2))