import tkinter as tk
import calculate

class Calc(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.work=calculate.Cal()

        self.title("계산기")
        self.geometry("800x600+100+100")
        self.resizable(1, 1)



        select = tk.Frame(self)
        select.pack(side="top", pady=60)

        select_2 = tk.Frame(self)
        select_2.pack(side="top")

        self.context = tk.Label(select, text="계산기").pack(pady=20)

        self.enter_1 = tk.Entry(select, width=15)
        self.enter_1.pack(side="left", padx=50)

        self.enter_2 = tk.Entry(select, width=15)
        self.enter_2.pack(side="left", padx=50)

        self.outPut = tk.Entry(select, width=15)
        self.outPut.pack(side="left", padx=50)
        rvalue=tk.IntVar

        def adddd():
            self.work.setkey(self.enter_1.get(),self.enter_2.get())
            self.work.add()
            self.outPut.delete(0,"end")
            self.outPut.insert(0,self.work.inPut)

        def subs():
            self.work.setkey(self.enter_1.get(),self.enter_2.get())
            self.work.substract()
            self.outPut.delete(0,"end")
            self.outPut.insert(0,self.work.inPut)

        def multi():
            self.work.setkey(self.enter_1.get(),self.enter_2.get())
            self.work.multiply()
            self.outPut.delete(0,"end")
            self.outPut.insert(0,self.work.inPut)

        def divi():
            self.work.setkey(self.enter_1.get(),self.enter_2.get())
            self.work.divide()
            self.outPut.delete(0,"end")
            self.outPut.insert(0,self.work.inPut)


        self.aDD = tk.Button(select_2, width=10, height=3, text="+", command=adddd)
        self.aDD.pack(side="left", padx=20)

        self.subStract = tk.Button(select_2, width=10, height=3, text="-", command=subs)
        self.subStract.pack(side="left", padx=20)

        self.multiPly = tk.Button(select_2, width=10, height=3, text="*", command=multi)
        self.multiPly.pack(side="left", padx=20)

        self.diVide = tk.Button(select_2, width=10, height=3, text="%", command=divi)
        self.diVide.pack(side="left", padx=20)




app = Calc()
app.mainloop()