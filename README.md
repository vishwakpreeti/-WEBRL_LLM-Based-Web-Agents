#  WEBRL: A Reinforcement Learning Framework to Train LLM-Based Web Agents for Autonomous and Efficient Web Interaction

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red.svg)](https://streamlit.io/)

---

## Project Overview

WEBRL is a practical framework designed to train web agents to autonomously interact with real-world websites using Large Language Models (LLMs) like Azure OpenAI GPT-35-Turbo.  
It combines browser automation (Playwright) with a simulation dashboard (Streamlit) to dynamically perform web tasks such as product searches on Amazon India.

This project lays the foundation for integrating Reinforcement Learning concepts into autonomous web navigation.

---

## Features

- Real-time web interaction using LLM reasoning
- Playwright browser automation
- Dynamic simulation of agent behavior (for Windows users)
- Reward calculation based on task success
- Real-time action visualization on Streamlit dashboard

---

## Technologies Used

| Technology | Purpose |
|:-----------|:--------|
| Python 3.9 | Programming Language |
| Azure OpenAI Service | Language Model (GPT-35 Turbo) |
| Playwright (Python) | Browser Automation |
| Streamlit | Frontend Dashboard |
| Windows 10/11 | Development Environment |

## Dashboard Output - Simulated Search Action

![image](https://github.com/user-attachments/assets/0603d35c-af99-4458-9e30-acff1654cef4)

## Dashboard Output - Typing Action

![image](https://github.com/user-attachments/assets/5d174d6e-dc38-4ec4-a774-78118eb341a5)

## Terminal Logs - Agent Actions

![image](https://github.com/user-attachments/assets/9a58f0a4-a0f2-4524-bc2a-2ec787d213ed)

# Future Work
- Integrate full Reinforcement Learning loop for policy learning
- Expand to multi-step workflows (login, checkout)
- Improve error recovery strategies
- Test agent on multiple websites (e.g., Flipkart, Walmart)
- Deploy in Linux environment for full Playwright control inside Streamlit

This project is licensed under the IITJ License.
