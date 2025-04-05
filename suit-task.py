import pyautogui
import random
import time
import subprocess
import string

def human_click(x1, y1, x2, y2):
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.6))
    pyautogui.click()

def human_type(text):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.05, 0.15))

def random_name(length_range=(3, 4)):
    vowels = 'aoui'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    length = random.randint(*length_range)
    name = ''
    for _ in range(length):
        name += random.choice([random.choice(consonants), random.choice(vowels)])
    return name

def move_mouse_randomly(x1, y1, x2, y2):
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))

def press_arrow_with_mouse_movement(key, times_range, area):
    for _ in range(random.randint(*times_range)):
        move_mouse_randomly(*area)
        pyautogui.press(key)
        time.sleep(random.uniform(0.15, 0.3))

# Start actions
pyautogui.click(575, 79)
time.sleep(0.5)
human_type("www.github.com")
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(random.uniform(5, 7))

# First random clicks and interactions
human_click(1086, 175, 1097, 190)
time.sleep(random.uniform(1, 1.5))
human_click(887, 286, 1077, 296)
time.sleep(random.uniform(4, 5))
human_click(66, 244, 77, 254)
time.sleep(random.uniform(2, 3))
human_click(70, 178, 82, 192)
time.sleep(random.uniform(4.5, 6))
for _ in range(random.randint(2, 5)):
    human_click(302, 162, 634, 196)
    time.sleep(random.uniform(0.2, 0.4))

human_click(48, 484, 260, 583)
time.sleep(0.5)
# Scroll simulation
press_arrow_with_mouse_movement('down', (5, 9), (336, 295, 1241, 584))
press_arrow_with_mouse_movement('up', (4, 8), (336, 295, 1241, 584))

# Back to input
pyautogui.click(575, 79)
time.sleep(0.5)
human_type("www.github.com")
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(random.uniform(5, 7))

# Search interaction
human_click(818, 182, 1003, 187)
time.sleep(random.uniform(0.5, 1))
human_type(random_name((2, 3)))  # Fixed: now it will truly give 23 character names
time.sleep(random.uniform(1, 2))
pyautogui.press('enter')
time.sleep(4)
human_click(985, 323, 994, 509)
time.sleep(random.uniform(0.5, 1))

# Scroll simulation again
for _ in range(random.randint(2, 3)):
    press_arrow_with_mouse_movement('down', (5, 9), (336, 295, 1241, 584))
    press_arrow_with_mouse_movement('up', (4, 8), (336, 295, 1241, 584))

# Run start.py
subprocess.run(['python3', 'start.py'])
time.sleep(5)
# Scroll simulation
press_arrow_with_mouse_movement('down', (5, 9), (336, 295, 1241, 584))
press_arrow_with_mouse_movement('up', (4, 8), (336, 295, 1241, 584))

# Run fork.py
subprocess.run(['python3', 'fork.py'])
time.sleep(6)

# Final interactions
for _ in range(9):
    pyautogui.press('down')
    time.sleep(random.uniform(0.15, 0.3))
human_click(952, 422, 1021, 436)
time.sleep(random.uniform(14, 16))
human_click(1324, 180, 1338, 191)
time.sleep(random.uniform(1, 1.7))
human_click(1078, 278, 1308, 287)
time.sleep(random.uniform(3.5, 5))

pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.8)
subprocess.run(['python3', 'edit.py'])
time.sleep(random.uniform(3, 4))
human_type(random_name((6, 8)))
time.sleep(random.uniform(1, 2))
pyautogui.press('enter')
time.sleep(4)

# Final return to GitHub
pyautogui.click(575, 79)
time.sleep(0.5)
human_type("www.github.com")
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(random.uniform(5, 7))
