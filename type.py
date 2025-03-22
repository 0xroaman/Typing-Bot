import pyautogui
import time

# Delay to switch to the target window
print("Switch to the target window. Typing starts in 5 seconds...")
time.sleep(5)

text = "I'm a full-stack developer"  # Change this to your text
for char in text:
    pyautogui.typewrite(char)
    time.sleep(0.1)  # Adjust speed if needed

print("Typing completed!")
