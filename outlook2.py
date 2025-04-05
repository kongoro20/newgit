import pyautogui
import time
import random
import string

time.sleep(2)
# Helper functions
def human_typing(text):
    """Simulate human-like typing."""
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))

def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)

def generate_random_year(start=1990, end=2002):
    """Generate a random year."""
    return str(random.randint(start, end))

# Continue actions
def continue_actions():
    # Random click in specific area
    random_click_in_area((514, 488), (611, 499))
    time.sleep(random.uniform(0.5, 1))

    # Random click in specific area
    random_click_in_area((525, 195), (594, 456))
    time.sleep(random.uniform(0.5, 1))

    # Random click in specific area
    random_click_in_area((631, 486), (729, 498))
    time.sleep(random.uniform(0.5, 1))

    # Random click in specific area
    random_click_in_area((642, 194), (716, 455))
    time.sleep(random.uniform(0.5, 1))

    # Random click in specific area
    random_click_in_area((750, 489), (820, 492))
    time.sleep(random.uniform(0.5, 1))

    # Write random year
    random_year = generate_random_year()
    human_typing(random_year)
    time.sleep(1)

    # Perform random 1-4 clicks in one of two rectangular areas
    area1 = ((86, 230), (322, 421))
    area2 = ((1005, 258), (1282, 492))
    chosen_area = random.choice([area1, area2])
    for _ in range(random.randint(1, 4)):
        random_click_in_area(*chosen_area)
        time.sleep(random.uniform(0.5, 1))

    # Randomly wait
    time.sleep(random.uniform(1, 2))

    # Randomly press down arrow 4-6 times with short delay
    for _ in range(random.randint(4, 6)):
        pyautogui.press('down')
        time.sleep(random.uniform(0.5, 0.8))

    # Random click in specific area
    random_click_in_area((763, 503), (841, 516))
    time.sleep(random.uniform(3, 5))

# Run both parts
if __name__ == "__main__":
    continue_actions()  # Call the second part
