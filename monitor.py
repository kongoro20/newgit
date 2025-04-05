import time
import subprocess
import re
import pyperclip

# Regex pattern to match the GitHub confirmation link
pattern = r"https://github\.com/account_verifications/confirm/[^ ]+"

def check_clipboard_for_pattern():
    clipboard_content = pyperclip.paste()
    return re.search(pattern, clipboard_content)

def run_script(script_name):
    try:
        subprocess.run(["python3", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

def main():
    while True:
        if check_clipboard_for_pattern():
            print(" Found GitHub verification link. Exiting.")
            break
        else:
            print("L Link not found. Running github33.py...")
            run_script("github33.py")
            print(" github33.py done. Sleeping 2s...")
            time.sleep(2)
            print("¶ Running github44.py...")
            run_script("github44.py")
            print(" github44.py done. Looping again...\n")

if __name__ == "__main__":
    main()
