#!/bin/bash

echo "[+] Activating virtual environment..."
source /home/deck/drone/venv/bin/activate || exit 1

echo "[+] Pulling latest from GitHub..."
cd /home/deck/drone || exit 1
git pull origin master || exit 1

echo "[+] Running controller..."
python main.py || exit 1

