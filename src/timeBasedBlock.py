# Informal interface to inherit the actions to perform when the clock goes up and down

class TimeBasedBlock:
    # Clock goes up
    def tic(self): 
        pass
    # Clock goes down
    def toc(self):
        pass