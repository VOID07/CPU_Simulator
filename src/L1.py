#import dependencies
import time

class L1:

    MODIFIED = 'M'
    SHARED = 'S'
    INVALID = 'I'
    def  __init__(self, p_freq):
        # Mem block with following structure: block number, coherence status, mem address, hex data
        self.memBlock = [   [0, INVALID, '0000', '0000'],
                            [1, INVALID, '0000', '0000']]
        self.lastStatus = ''
        self.lag = 3*p_freq

    def sleep(self):
        time.sleep(self.lag)
    
    def read(self, p_instr, p_addr):
        self.sleep()
        if (self.memBlock[0][2] == p_addr and self.memBlock[0][1] == SHARED ):

