# import dependencies
import time
import random

# import modules

class ControlUnit:
    def __init__(self, p_clk, p_freq, p_procNumber):
        self.clk = p_clk
        self.freq = p_freq/20
        self.lastInstr = ""
        self.INSTR_POOL = ["READ", "CALC", "WRITE"]
        self.lastClock = True
        self.procNumber = "P"+str(p_procNumber)+": "
    
    def sleep(self):
        time.sleep(self.freq)

    def pushInstr(self):
        print(self.lastInstr)
        pass

    def generateInstr(self):
        randNum = random.randrange(3) # Current size of the INSTR POOL is 3, discrete uniform probability
        instrType = self.INSTR_POOL[randNum] 

        self.lastInstr = self.procNumber + instrType

        if (randNum != 1):
            memPos = random.randrange(16)
            memPos = ' '+bin(memPos).split('b')[1].zfill(4)
            self.lastInstr += memPos

            if (randNum == 2): # Instr is 
                value = random.randrange(2**16)
                value = "; " +  hex(value).split('x')[1].zfill(4).upper()
                self.lastInstr += value
        
        print(self.lastInstr)

    # Monitors the clock to create a new instruction
    def run(self):
        import main
        while(main.isRunning()):
            self.sleep()
            # if state of the clock is the same, do nothing
            if (self.clk.getClock() == self.lastClock):
                continue

            # if state of the clock changed, update clock and perform an action
            else: 
                self.lastClock = self.clk.getClock()
                # Positive edge push instr
                if(self.lastClock):
                    self.pushInstr()
                # Negative edge create instr
                else:
                    self.generateInstr()