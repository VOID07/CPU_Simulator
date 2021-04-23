# Import dependencies
import time
import keyboard
import threading
import os
import dotenv

# Import modules
import Clock
import MainMemory
import GUI
import ControlUnit

# Global variables

global running
running = True
def isRunning():
    global running
    return running
#CPU_GUI = threading.Thread(target=GUI.GUI).start()

# Global configurations from .env file and extract global values
global CONFIG
CONFIG = dotenv.dotenv_values(".env")

# Extract values from config file

FREQ = int(CONFIG["CLOCK_FREQ"])

# Initialize clock
clk = Clock.Clock(FREQ)
cu1 = ControlUnit.ControlUnit(clk, FREQ, 0)
cu2 = ControlUnit.ControlUnit(clk, FREQ, 1)
cu3 = ControlUnit.ControlUnit(clk, FREQ, 2)
cu4 = ControlUnit.ControlUnit(clk, FREQ, 3)

threading.Thread(target=cu1.run).start()
threading.Thread(target=cu2.run).start()
threading.Thread(target=cu3.run).start()
threading.Thread(target=cu4.run).start()
clk.changeMode()
threading.Thread(target=clk.run).start()
threading.Thread(target=clk.printClock).start()
 
