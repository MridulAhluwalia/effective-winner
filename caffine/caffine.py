"""
Author: Mridul Ahluwalia
"""
import ctypes
import os
import sys

import infi.systray

# Get the base path of the application
base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))


def toggle_prevent_sleep(icon):
    # Check if the prevent_sleep_flag is set or not
    prevent_sleep_flag = not toggle_prevent_sleep.prevent_sleep_flag
    toggle_prevent_sleep.prevent_sleep_flag = prevent_sleep_flag

    # Prevent or allow system sleep based on the flag
    if prevent_sleep_flag:
        # Prevent system sleep
        ctypes.windll.kernel32.SetThreadExecutionState(
            0x80000002
        )  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED
        icon.update(icon=icon_path_awake)
    else:
        # Allow system sleep
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)  # ES_CONTINUOUS
        icon.update(icon=icon_path_asleep)


# Initialize the prevent_sleep_flag
toggle_prevent_sleep.prevent_sleep_flag = False

# Set the icon paths for awake and asleep states
icon_path_awake = os.path.join(base_path, "images/owl.ico")
icon_path_asleep = os.path.join(base_path, "images/panda.ico")


def main():
    menu_options = (("Toggle Prevent Sleep", None, toggle_prevent_sleep),)
    systray = infi.systray.SysTrayIcon(icon_path_asleep, "Prevent Sleep", menu_options)
    systray.start()


if __name__ == "__main__":
    main()
