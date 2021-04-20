# Dependencies
import time
import keyboard
import threading

class Clock:
    def __init__(self):
        self.clock = False
        self.reset = False

    def reset(self):
        self.reset = True
    
    def run(self):
        threading.Thread(target=self.printclock()).start()
        while(True):
            time.sleep(1)
            if not keyboard.is_pressed('r'):
                if (not self.reset):
                    self.clock = not self.clock
                    continue
                else:    
                    self.clock = 0
                    time.sleep(1)
                    self.reset = False
            else:
                self.reset()
                
    def printclock(self):
        while(True):
            time.sleep(0.2)