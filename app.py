# import streamlit as st
# from agent.planner import run_planner

# # Page config
# st.set_page_config(
#     page_title="Construction Planner AI",
#     page_icon="🏗️",
#     layout="centered"
# )

# # Title
# st.title("🏗️ Construction Planning Agent")

# st.markdown("Enter your construction goal and let AI generate a plan.")

# # Input box
# goal = st.text_input("Enter Goal (e.g., Build a 2-floor house)")

# # Button
# if st.button("Generate Plan"):

#     if goal.strip() == "":
#         st.warning("Please enter a goal")
#     else:
#         with st.spinner("Generating plan..."):
#             result = run_planner(goal)

#         st.success("Plan Generated ✅")

#         st.subheader("📋 Execution Plan")
#         st.text(result)














import streamlit as st
from agent.planner import run_planner

st.set_page_config(page_title="Construction AI", page_icon="🏗️")

# Custom styling
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ Construction Planning Agent")

st.write("AI-powered planner for construction projects")

goal = st.text_input("Enter your goal")

col1, col2 = st.columns([1,1])

if col1.button("Generate Plan"):
    if goal:
        with st.spinner("Thinking like an engineer..."):
            result = run_planner(goal)

        st.success("Plan Ready ✅")

        st.markdown("### 📋 Final Plan")
        st.code(result, language="markdown")
    else:
        st.error("Enter a goal first!")

if col2.button("Clear"):
    st.rerun()
