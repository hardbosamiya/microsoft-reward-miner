import pyautogui
import time
import random
import keyboard
import g4f

START_DELAY = 5
ITERATIONS = 15

running = True

def stop():
    global running
    running = False
    print("Stopped")

keyboard.add_hotkey("esc", stop)

def generate_text():
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Give me one short random topic or search idea"}
        ]
    )
    return response.strip()


print(f"Start in {START_DELAY} sec...")
time.sleep(START_DELAY)

for i in range(ITERATIONS):

    if not running:
        break

    text = generate_text()
    print("Typing:", text)

    pyautogui.click(235,75)

    pyautogui.write(text, interval=random.uniform(0.04,0.08))
    pyautogui.press("enter")

    time.sleep(random.uniform(2,4))

    pyautogui.hotkey("ctrl","l")   # focus search / address bar
    time.sleep(1)

print("Finished")