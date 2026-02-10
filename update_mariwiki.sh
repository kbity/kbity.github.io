#!/bin/bash

# Usage: ./update_mariwiki.sh "Your commit message here"
# If no message is provided, defaults to "sample text"

source ../pyenv/bin/activate
python main.py

if [ $? -ne 0 ]; then
  echo "Error: main.py failed to run."
  exit 1
fi

COMMIT_MSG=${1:-"sample text"}

git add .
git commit -m "$COMMIT_MSG"
git push
