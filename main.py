import pygame
import asyncio
from bleak import BleakClient

# Replace with your drone's MAC address and characteristic UUID
BLE_ADDRESS = "D0:39:72:BF:4B:7C"
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"  # Example

# Joystick setup
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

def get_controls():
    pygame.event.pump()
    lx = round(joystick.get_axis(0), 2)
    ly = round(joystick.get_axis(1), 2)
    rx = round(joystick.get_axis(3), 2)
    th = round(joystick.get_axis(2), 2)
    return lx, ly, rx, th

async def main():
    print(f"Connecting to drone at {BLE_ADDRESS}...")
    async with BleakClient(BLE_ADDRESS) as client:
        print("Connected. Sending control data...")
        while True:
            lx, ly, rx, th = get_controls()
            payload = f"{lx:.2f},{ly:.2f},{rx:.2f},{th:.2f}"
            await client.write_gatt_char(CHARACTERISTIC_UUID, payload.encode())
            await asyncio.sleep(0.05)  # 20Hz update rate

if __name__ == "__main__":
    asyncio.run(main())
