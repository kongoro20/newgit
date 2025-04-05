import time
import pyautogui
import pyperclip
import re
import subprocess

time.sleep(1)

# Step 2: Retrieve clipboard content
clipboard_content = subprocess.run(["xclip", "-selection", "clipboard", "-o"], capture_output=True, text=True).stdout

# Step 3: Extract email address (only Hotmail or Outlook)
match = re.search(r'[\w\.-]+@(hotmail|outlook)\.com', clipboard_content)

if match:
    extracted_email = match.group(0)
    
    # Step 4: Save extracted email back to clipboard
    subprocess.run(["xclip", "-selection", "clipboard"], input=extracted_email, text=True)
