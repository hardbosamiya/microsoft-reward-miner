import pyautogui
import time
import random
import keyboard
import g4f

START_DELAY = 5
running = True

def stop():
    global running
    running = False
    print("Stopped by user")

keyboard.add_hotkey("esc", stop)


# ===== Generate LIST of queries from g4f =====
def generate_queries():

    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": "Give me 15 short random search topics in numbered list"
            }
        ]
    )

    text = response.strip()

    # convert to python list
    lines = text.split("\n")

    queries = []

    for line in lines:
        line = line.strip()

        if line:
            # remove numbering like "1. topic"
            if "." in line:
                line = line.split(".",1)[1].strip()

            queries.append(line)

    return queries


print(f"Starting in {START_DELAY} sec...")
time.sleep(START_DELAY)

queries = generate_queries()

print("Generated Queries:")
for q in queries:
    print(q)

print("Starting automation...")

for query in queries:

    if not running:
        break
    

    print("Typing:", query)

    pyautogui.write(query, interval=random.uniform(0.04,0.08))
    pyautogui.press("enter")

    time.sleep(random.uniform(3,5))

    pyautogui.hotkey("ctrl","l")   # focus search bar
    time.sleep(random.uniform(1,2))

print("Finished")