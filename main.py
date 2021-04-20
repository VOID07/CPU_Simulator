# Import dependencies
import os
import threading
from dotenv import dotenv_values


# Import modules
import Clock
import mainMemory

# Global configurations from .env file ans extract global values
global CONFIG
CONFIG = dotenv_values(".env")

NUM_MEN_BLOCKS = int(CONFIG["NUM_MEN_BLOCKS"])
mem = mainMemory.mainMemory(NUM_MEN_BLOCKS)

clock = Clock.Clock()

threading.Thread(target=clock.run()).start()
 
print(mem.printMem())