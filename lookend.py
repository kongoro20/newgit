import pyautogui
import time
import random

time.sleep(2)
# Helper functions
def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a specified rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)
    return x, y  # Return the coordinates for reuse

def human_typing(text):
    """Simulate human-like typing."""
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))

# Function to perform the third part of the script
def perform_third_part():
    """Perform the third part of the script."""
    # Proceed to the next actions
    random_click_in_area((762, 473), (841, 487))  # Random click
    time.sleep(random.uniform(14, 16))

    pyautogui.click(293, 42)  # Click at (290, 178)
    time.sleep(1)
    pyautogui.click(250, 42)  # Click at (248, 178)
    time.sleep(1)

    pyautogui.write('https://go.microsoft.com/fwlink/p/?LinkID=2125442&deeplink=owa%2F')  # Type URL
    time.sleep(0.5)
    pyautogui.press('enter')  # Press Enter
    time.sleep(14)

# Run the script
if __name__ == "__main__":
    perform_third_part()
