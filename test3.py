import pyautogui
import time
import subprocess
import sys  # Add sys module for exiting with status

time.sleep(3)
pyautogui.click(1339, 170)
print("Clicked on (666, 242)")
time.sleep(1)
pyautogui.write('shell')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(476, 461)
time.sleep(1)
pyautogui.write('nix-env -f https://github.com/NixOS/nixpkgs/archive/05bbf675397d5366259409139039af8077d695ce.tar.gz -iA firefox')
time.sleep(1)
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(15)
subprocess.run(["python3", "firefox.py"])
time.sleep(6)
pyautogui.write('firefox')
time.sleep(0.7)
pyautogui.press('enter')
time.sleep(40)

try:
    if pyautogui.locateCenterOnScreen('vnc_button.png', confidence=0.8, grayscale=True):
        print("VNC button found. Exiting...")
        pyautogui.click(25, 131)
        time.sleep(2.5)
        pyautogui.press('enter')
        time.sleep(3)
        subprocess.run(['python3', 'deleteworkspace.py'])
        sys.exit(100)  # Exit with status 100 to indicate VNC was found
except pyautogui.ImageNotFoundException:
    print("Image not found, continuing with the script...")

pyautogui.click(1347, 193)
print("Clicked on (1347, 194)")
time.sleep(4)
pyautogui.click(884, 170)
time.sleep(0.4)
pyautogui.click(884, 170)
time.sleep(0.4)
pyautogui.click(884, 170)
time.sleep(2)
pyautogui.click(598, 573)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(598, 573)
print("Clicked on (912, 167)")
time.sleep(2)
pyautogui.write('pip install requests')
print("Typed 'python3'")
time.sleep(1)
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(2)
pyautogui.write('y')
print("Pressed 'y'")
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(15)
pyautogui.write('clear')
print("Typed 'clear'")
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(2)
pyautogui.click(1343, 200)
print("Clicked on (572, 170)")
time.sleep(2)
pyautogui.click(348, 171)
time.sleep(1)
print("Script execution completed.")
