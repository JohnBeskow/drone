#/bin/bash

echo "[+] Updating repo..."
cd ~/drone-controller || exit
git pull origin main

echo "[+] Running app..."
python3 main.py
