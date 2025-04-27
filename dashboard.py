import streamlit as st
import time
import re

# Function to extract search keyword from Task
def extract_keyword(task):
    keywords = re.findall(r"search for (.+?) on", task.lower())
    if keywords:
        return keywords[0]
    return "laptops"  # default fallback

# Simulated Action Generator
def get_simulated_action(step, typed_already, keyword):
    if not typed_already:
        return f'type input[name="field-keywords"] {keyword}'
    else:
        return 'click input[type="submit"]'

# Streamlit page setup
st.set_page_config(page_title="WEBRL Agent Dashboard", page_icon="🤖", layout="wide")
st.title("🤖 WEBRL Agent Dashboard (Simulated Dynamic)")
st.caption("Azure OpenAI + Playwright powered Autonomous Web Agent (Dynamic Simulation for Windows) 🚀")

# Sidebar for user inputs
TASK = st.sidebar.text_input("Enter Task Instruction", "Search for laptops on Amazon India.")
EXPECTED_URL = st.sidebar.text_input("Expected URL Part", "s?k=laptop")
NUM_STEPS = st.sidebar.slider("Number of Steps", 1, 10, 5)
start_button = st.sidebar.button("🚀 Start Simulated Agent")

# Main area placeholders
status_placeholder = st.empty()
action_placeholder = st.empty()
reward_placeholder = st.empty()
error_placeholder = st.empty()

if start_button:
    typed_already = False
    search_keyword = extract_keyword(TASK)

    try:
        status_placeholder.success(f"✅ Simulating browser navigation to Amazon India for '{search_keyword}'...")

        for step in range(NUM_STEPS):
            st.write(f"### Step {step+1}")
            action = get_simulated_action(step, typed_already, search_keyword)
            st.code(f"Simulated Action: {action}")

            st.success(f"Step {step+1}: Simulated '{action}' successfully! 🚀")
            time.sleep(1)

            if action.startswith("type"):
                typed_already = True

        final_reward = 1
        reward_placeholder.success(f"🎯 Final Simulated Reward: {final_reward}")

        status_placeholder.success("✅ Simulated session completed successfully.")

    except Exception as e:
        error_placeholder.error(f"🚨 Simulation Error: {e}")
