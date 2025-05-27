#!/bin/bash

echo "[+] Updating repo..."
cd ~/drone || exit
git pull origin main

echo "[+] Running app..."
python3 main.py
