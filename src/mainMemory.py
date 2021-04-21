class MainMemory():
    def __init__(self, blockSize):
        self.memBlock = [0]*blockSize # Creates a  memory block of size 8

    def getMemoryDump(self):
        return self.memBlock
    
    def writeTo(self, pos, data):
        self.memBlock[pos] = data

    def printMem(self):
        return self.memBlock
             



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)