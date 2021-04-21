# Dependencies
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


# Global Variables
global CLOCK
CLOCK = False

