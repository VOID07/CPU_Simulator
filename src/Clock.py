import time

class Clock:

    def __init__(self, p_freq):
        self.clock = False
        self.reset = False
        self.freq = p_freq/2
        
    def reset(self):
        self.reset = True

    def getClock(self):
        return self.clock

    def run(self):
        global var
        while(True):
            if (not self.reset):
                time.sleep(self.freq)
                self.clock = not self.clock
            else:
                time.sleep(self.freq)
                self.reset = False
    
    def printClock(self):
        while(True):
            time.sleep(self.freq/10)
            print(self.clock)