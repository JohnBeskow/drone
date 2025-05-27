# ~/drone/main.py

import pygame
import time

# Initialize pygame and joystick
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller found. Make sure it's connected via Bluetooth or USB.")
    exit(1)

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Connected to controller: {joystick.get_name()}")

try:
    while True:
        pygame.event.pump()

        # Read joystick axes
        lx = joystick.get_axis(0)  # Left stick X
        ly = joystick.get_axis(1)  # Left stick Y
        rx = joystick.get_axis(2)  # Right stick X
        ry = joystick.get_axis(3)  # Right stick Y

        # Read triggers or buttons if needed
        throttle = joystick.get_axis(5)  # Example for trigger

        print(f"LX: {lx:.2f}, LY: {ly:.2f}, RX: {rx:.2f}, RY: {ry:.2f}, TH: {throttle:.2f}")

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    pygame.quit()

