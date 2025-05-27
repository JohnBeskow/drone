# 🛸 Drone Controller with BLE + Steam Deck

This project turns your Steam Deck (or any Linux device) into a BLE-based controller for a drone. It uses a game controller (Xbox, PS5, etc.) to read joystick input and sends it over Bluetooth Low Energy (BLE) to a drone using the Nordic UART Service (NUS).

---

## 📦 Requirements

- Python 3.7+
- Steam Deck or Linux system with BLE support
- Game controller connected (Xbox, PS5, etc.)
- A drone or BLE device supporting the Nordic UART Service (NUS)

---

## 🛠 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/JohnBeskow/drone.git
cd drone
```
---

### 2. Create config.py

Here can you store address and NUS_TX_UUID for Ble

---
### 3. Create and start venv

```
python3 -m venv venv
source venv/bin/activate
```
---
### 4. Install dependencies
```
pip install -r requirements.txt
```
---
### 5. Run the controller
```
python main.py

//or 

chmod +x setup.sh
./setup.sh
```
--- 
### 6. Run on Steam Deck Startup

terminal:
```
mkdir -p ~/.config/systemd/user
vim ~/.config/systemd/user/drone.service
```

then in the drone.service:
```
[Unit]
Description=Drone Controller Auto Start
After=default.target

[Service]
ExecStart=/home/deck/drone/venv/bin/python /home/deck/drone/main.py
Restart=always

[Install]
WantedBy=default.target
```

Then just run 
```
systemctl --user daemon-reload
systemctl --user enable drone.service
systemctl --user start drone.service
```
---

### This should be the final structure
```
drone/
├── main.py           # Main controller logic
├── setup.sh          # Script: venv + run
├── requirements.txt  # Dependencies
├── config.py         # BLE secrets (you create this)
├── .gitignore        # Ignores venv/, config.py, etc.
```
