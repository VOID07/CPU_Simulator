# Import dependencies
import time
import keyboard
import threading
import os
from dotenv import dotenv_values

# Import modules
import Clock 
import MainMemory
import GUI

CPU_GUI = threading.Thread(target=GUI.GUI).start()
print("checkpoint")

# Global configurations from .env file and extract global values
global CONFIG
CONFIG = dotenv_values(".env")

# Extract valuies from config file

FREQ = int(CONFIG["CLOCK_FREQ"])

# Initialize clock
clk = Clock.Clock(FREQ)
CPU_GUI.
threading.Thread(target=clk.run).start()
#threading.Thread(target=clk.printClock).start()
 
