import time

class Clock:

    # Operation modes
    #STEP = False
    #CONTINUOUS = True

    def __init__(self, p_freq):
        self.clock = False
        self.reset = False
        self.freq = p_freq/2
        self.mode = False
        self.step = False 
    
    # Stops the thread
    def reset(self):
        self.reset = True

    def getClock(self):
        return self.clock

    def changeMode(self):
        self.mode = not self.mode
        self.step = True

    def step(self):
        self.step = True

    # Sleeps the thread the given amount of time
    def sleep(self):
        time.sleep(self.freq)

    def run(self):
        while(not self.reset):
            self.sleep()
            if (self.mode): # False STEP mode, True CONTINUOUS mode
                self.clock = not self.clock
                continue

            else:
                if (self.step):
                    self.clock = not self.clock
                    self.sleep()
                    self.clock = not self.clock
                    self.step = False
    
    def printClock(self):
        import main

        while(main.isRunning()):
            time.sleep(self.freq/10)
            print(self.clock)