#import dependencies
import time

class CPU:

    def __init__(self, p_freq, p_L1):
        self.instr = ""
        self.lag = 2*p_freq
        self.L1 = p_L1 
        self.instTypes = {"READ":0, "CALC":1, "WRITE":2}

    def sleep(self):
        time.sleep(self.lag)

    def execute(self, p_instr, p_type, p_addr, p_data):
        self.Instr = p_instr
        self.sleep()

        # if statement approach used since the number of instructions is not expected to grow, hence, using easiest method
        if (p_instr == self.instTypes["READ"]):
            #self.L1.read(p_instr, p_addr)
            pass

        else if (p_instr == self.instTypes["WRITE"]):
            #self.L1.write(p_instr, p_addr, p_data)
            pass

        # Omited calc instruction, since it does only waits for the lagging time, and it is already taken at the begining of the function


