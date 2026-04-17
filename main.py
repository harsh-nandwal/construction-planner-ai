from agent.planner import run_planner

if __name__ == "__main__":
    goal = input("Enter your construction goal: ")

    result = run_planner(goal)

    print("\n===== FINAL PLAN =====\n")
    print(result)



