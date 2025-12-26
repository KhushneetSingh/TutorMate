from app.agents.planner_agent import PlannerAgent

if __name__ == "__main__":
    agent = PlannerAgent()

    plan = agent.run({
        "goal": "Prepare for My upcoming placement drive",
        "topics": [
            "linear Data Structures",
            "DBMS with SQL",
            "Computer Fundamentals"
        ],
        "days_available": 20,
        "daily_hours": 6
    })

    print("\n====== FINAL STUDY PLAN ======\n")

    # Converts a model object to JSON
    print(plan.model_dump_json(indent=2))