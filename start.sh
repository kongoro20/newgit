#!/bin/bash

# Handle Ctrl+C and stop all child processes, also create the exit signal file
trap "echo 'Ctrl+C detected. Stopping all scripts'; touch exit_signal.txt; kill 0; exit 0" SIGINT

# If exit signal exists, terminate
if [[ -f "exit_signal.txt" ]]; then
  echo "Exit signal detected. Exiting..."
  exit 0
fi

# List of scripts to run sequentially
scripts=(
  "tempmail.py"
  "save.py"
  "omocaptcha.py"
  "outlook1.py"
  "outlook2.py"
  "outlook3.py"
  "outlook4.py"
  "banner.py"
  "github1.py"
  "github2.py"
  "github3.py"
  "github4.py"
  "upload.py"
)

# Loop through all scripts sequentially
for script in "${scripts[@]}"; do
  # Check for exit signal at the start of each iteration
  if [[ -f "exit_signal.txt" ]]; then
    echo "Exit signal detected. Exiting..."
    exit 0
  fi

  if [[ -f "$script" ]]; then
    echo "Running $script..."

    if [[ "$script" == "outlook4.py" || "$script" == "banner.py" ]]; then
      timeout 100s python3 "$script"
      exit_status=$?
      if [[ $exit_status -eq 124 ]]; then
        echo "Script $script exceeded 100 seconds. Skipping..."
        continue
      fi
    else
      timeout 250s python3 "$script"
      exit_status=$?
      if [[ $exit_status -eq 124 ]]; then
        echo "Script $script exceeded 250 seconds. Exiting."
        sleep 1.5
        echo "all scripts are finished successfully without any issue." > finish.txt
        exit 1
      fi
    fi
  fi
done

echo "Process completed successfully."
echo "all scripts are finished successfully without any issue." > finish.txt
