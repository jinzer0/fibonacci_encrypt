import tkinter as tk


class Calc(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("계산기")
        self.geometry("640x400+100+100")
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

        # def add(self):
        #     key = value1 + value2
        #     self.outPut.insert(0, key)
        #
        # def substract(self):
        #     key = value1 - value2
        #     self.outPut.insert(0, key)
        #
        # def multiply(self):
        #     key = value1 * value2
        #     self.outPut.insert(0, key)
        #
        # def divide(self):
        #     key = value1 / value2
        #     self.outPut.insert(0, key)
        def pr():
            value1 = self.enter_1.get()
            value2 = self.enter_2.get()
            print(value1)
            print(value2)

        self.aDD = tk.Button(select_2, width=10, height=3, text="+").pack(side="left", command=pr(), padx=20)
        self.subStract = tk.Button(select_2, width=10, height=3, text="-").pack(side="left", padx=20, )
        self.multiPly = tk.Button(select_2, width=10, height=3, text="*").pack(side="left", padx=20, )
        self.diVide = tk.Button(select_2, width=10, height=3, text="%").pack(side="left", padx=20, )


app = Calc()
app.mainloop()
