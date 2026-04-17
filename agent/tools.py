from langchain.agents import Tool

def check_budget(input: str) -> str:
    return "Budget available: ₹50,00,000. Suitable for mid-scale residential construction."

def check_engineers(input: str) -> str:
    return "2 Civil Engineers and 1 Architect available."

def check_materials(input: str) -> str:
    return "Cement, steel, sand available. Bricks need to be ordered."

def check_permits(input: str) -> str:
    return "Permit approval takes 20 days. Requires local authority clearance."


# # Register tools
tools = [
    Tool(
        name="check_budget",
        func=check_budget,
        description="Check budget availability"
    ),
    Tool(
        name="check_engineers",
        func=check_engineers,
        description="Check engineers availability"
    ),
    Tool(
        name="check_materials",
        func=check_materials,
        description="Check materials availability"
    ),
    Tool(
        name="check_permits",
        func=check_permits,
        description="Check permit timeline"
    )
]   
