class Cal():
    def __init__(self):
        self.value1=0
        self.value2=0
        self.inPut=0

    def setkey(self, inp_1,inp_2):
        self.value1=int(inp_1)
        self.value2=int(inp_2)

    def add(self):
        self.inPut=self.value1+self.value2



    def substract(self):
        self.inPut=self.value1-self.value2



    def multiply(self):
        self.inPut=self.value1*self.value2



    def divide(self):
        self.inPut=self.value1/self.value2


