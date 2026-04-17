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
