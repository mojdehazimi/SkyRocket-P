# blink_name.py

import time
import os
import platform

def clear_console():
    """
    Clears the terminal screen based on the OS.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def blink_name(name: str, duration: int = 10, blink_interval: float = 0.5):
    """
    Blinks the provided name in the terminal for a set duration.
    
    Args:
        name (str): Name to blink.
        duration (int): Total time in seconds to blink the name.
        blink_interval (float): Time between each blink in seconds.
    """
    end_time = time.time() + duration
    show = True

    while time.time() < end_time:
        clear_console()
        if show:
            print(f"\n\n\n\t\t👋 {name} 👋")
        else:
            print("\n\n\n\t\t")  # blank space
        show = not show
        time.sleep(blink_interval)

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    blink_name(user_name)
    clear_console()
    print(f"\n\n\n\t\tDone blinking, {user_name}!")
