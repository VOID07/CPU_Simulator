# Import dependencies
import time
import keyboard
import threading
import os
from dotenv import dotenv_values

# Import modules
import Clock 
import MainMemory

# Global configurations from .env file ans extract global values
global CONFIG
CONFIG = dotenv_values(".env")

# Initialize clock
clk = Clock.Clock()
threading.Thread(target=clk.run).start()
#threading.Thread(target=clk.printClock).start()
 
