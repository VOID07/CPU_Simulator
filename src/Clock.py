import time

class Clock:

    def __init__(self):
        self.clock = False
        self.reset = False

    def reset(self):
        self.reset = True

    def run(self):
        global var
        while(True):
            if (not self.reset):
                time.sleep(1)
                self.clock = not self.clock
            else:
                time.sleep(2)
                self.reset = False
    
    def printClock(self):
        while(True):
            time.sleep(0.2)
            print(self.clock)