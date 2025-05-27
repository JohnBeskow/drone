#!/bin/bash

echo "[+] Updating package list and installing dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip git libSDL2-dev

echo "[+] Installing Python libraries..."
pip3 install --user pygame bleak

REPO_DIR="$HOME/drone-controller"

if [ ! -d "$REPO_DIR" ]; then
    echo "[+] Cloning repository..."
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git "$REPO_DIR"
else
    echo "[+] Pulling latest changes..."
    cd "$REPO_DIR" && git pull
fi

echo "[+] Running control app..."
cd "$REPO_DIR"
python3 main.py
