import time  # Don't forget this!
from agent import get_action
from environment import WebEnvironment
from reward import get_reward

# Define the task for the agent
TASK = "Search for laptops on Amazon India."
EXPECTED_URL = "s?k=laptop"

def main():
    try:
        env = WebEnvironment()
        env.go_to("https://www.amazon.in/")

        typed_already = False  # Memory flag: whether we have typed already

        for step in range(5):
            print(f"Step {step+1}: Getting page visible text...")
            page_text = env.page.inner_text('body')

            # Dynamic prompt based on whether typing happened
            if not typed_already:
                prompt = f"""You are a web agent helping to complete a task.

Visible Text Content:
{page_text}

Instruction:
{TASK}

RULES:
- First, TYPE "laptops" into the search input box (input[name="field-keywords"]).
- Only give a TYPE action.
- Do not click anything yet.
- Only one action per reply.

Example:
type input[name="field-keywords"] laptops
"""
            else:
                prompt = f"""You are a web agent helping to complete a task.

Visible Text Content:
{page_text}

Instruction:
{TASK}

RULES:
- Now, CLICK the search button (input[type="submit"]).
- Only give a CLICK action.
- Only one action per reply.

Example:
click input[type="submit"]
"""

            print(f"Step {step+1}: Sending prompt to agent...")
            action = get_action(prompt)
            print(f"Raw action received:\n{action}")

            # Clean action: take only first line if multiple
            action = action.strip().split('\n')[0]
            print(f"Using first action: {action}")

            if action.strip().lower() == "no_action":
                print(f"Step {step+1}: Agent decided no action needed. Skipping step.")
                continue

            try:
                env.perform_action(action)
                print(f"Step {step+1}: Action performed successfully.")

                # Wait after every action (important for page load)
                time.sleep(3)

                # If typing happened, mark that we should click next
                if action.startswith("type"):
                    typed_already = True

            except Exception as e:
                print(f"⚠️ Error while performing action on Step {step+1}: {e}")
                break

        # Final page check after all steps
        final_page_text = env.page.inner_text('body')
        reward = get_reward(env.page.url, EXPECTED_URL)

        if reward > 0:
            print(f"🎯 Final Reward: {reward}")
        else:
            # Optional: smarter check based on page text if needed
            if "laptop" in final_page_text.lower() and "results" in final_page_text.lower():
                print(f"🎯 Final Reward (based on page text): 1")
            else:
                print(f"❌ Final Reward: -1")

        env.close()

    except Exception as e:
        print(f"🚨 MAIN Error: {e}")

if __name__ == "__main__":
    main()
