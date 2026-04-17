from langchain.agents import initialize_agent
from langchain_groq import ChatGroq
from agent.tools import tools
from dotenv import load_dotenv

load_dotenv()

def run_planner(goal):

    llm = ChatGroq(
        # model="llama-3.3-70b-versatile",
        model="llama-3.1-8b-instant",
        # model="openai/gpt-oss-20b",
        temperature=0
    )   

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
        # max_iterations=1,
        # early_stopping_method="generate" 
        handle_parsing_errors=True
    )

    with open("prompts/planner_prompt.txt", "r") as f:
        prompt = f.read()

    final_prompt = prompt + "\nGoal: " + goal

    # result = agent.run(final_prompt)
    # return result

    response = llm.invoke(final_prompt)

    return response.content