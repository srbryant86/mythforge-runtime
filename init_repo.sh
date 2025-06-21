#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: ./init_repo.sh <your-github-repo-url>"
  exit 1
fi

git init
git add .
git commit -m "Initial commit: MythForge runtime payload"
git branch -M main
git remote add origin $1
git push -u origin main
