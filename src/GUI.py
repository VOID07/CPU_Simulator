from tkinter import *
import threading

class GUI:

    # Class builder
    def __init__(self):
        self.root = Tk()
        self.root.title("CPU Simulator")
        self.root.geometry("800x600")
        self.root.mainloop()

    # Returns the TK member or the object
    def getRoot(self):
        return self.root