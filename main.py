import tkinter as tk


class FiboEnc(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.finaloutput = []

        select = tk.Frame(self)
        select.pack(side="top")

        select_2 = tk.LabelFrame(self)
        select_2.pack(side="left", padx=20)

        select_3 = tk.Frame(self)
        select_3.pack(side="left")

        select_4 = tk.LabelFrame(self)
        select_4.pack(side="left")

        self.geometry("800x600+600+250")
        self.resizable(True, True)
        self.title("Fibonacci De/Encrypt")

        contents = tk.Frame(self)
        contents.pack(side="bottom")

        self.name = tk.Label(select, text="피보나치 수열을 이용한 간단한 암호화/복호화")
        self.name.pack(pady=20)
        self.enter_ex = tk.Label(select_2, text="텍스트 입력").grid(row=0, column=0, ipady=30)
        self.enter = tk.Text(select_2, width=25)
        self.enter.grid(column=0, row=1, padx=5)

        self.enter_2_ex = tk.Label(select_2, text="항 번호 입력").grid(row=0, column=2)
        self.enter_2 = tk.Entry(select_2, width=10)
        self.enter_2.grid(column=2, row=1)

        self.outPut_ex = tk.Label(select_4, text="텍스트 출력")
        self.outPut_ex.grid(row=0, column=0, ipady=30)
        self.outPut = tk.Text(select_4, width=35)
        self.outPut.grid(row=1, column=0, padx=5)

        def deCrypt():
            a = 1
            b = 1
            finalkey = 0
            key = self.enter_2.get()
            for i in range(int(key) - 1):
                if int(key) == 1 or int(key) == 2:
                    finalkey = 1
                else:
                    a += b
                    b = a - b
            finalkey = b

            textkey = self.enter.get("1.0", "end")
            textkey = textkey.strip()
            textkey = textkey.split(" ")
            self.outPut.delete("1.0", "end")
            for i in textkey:
                i = int(i)
                self.outPut.insert("2.0", chr(i - finalkey))

        def enCrypt():
            self.outPut.config(state="normal")
            a = 1
            b = 1
            finalkey = 0
            key = self.enter_2.get()
            for i in range(int(key) - 1):
                if int(key) == 1 or int(key) == 2:
                    finalkey = 1
                else:
                    a += b
                    b = a - b
            finalkey = b

            textkey = self.enter.get("1.0", "end")
            textkey = textkey.upper()
            textkey = textkey.strip()
            textkey = textkey.replace(" ", "")

            for i in textkey:
                self.finaloutput.append(ord(i) + finalkey)

            self.outPut.delete("1.0", "end")
            self.outPut.insert("1.0", self.finaloutput)
            self.finaloutput = []

        self.button3 = tk.Button(select_3, height=1, width=10, text="Decrypt", command=deCrypt, padx=10, )
        self.button3.grid(row=1, column=2, ipadx=10)

        self.button4 = tk.Button(select_3, height=1, width=10, text="Encrypt", command=enCrypt, padx=10)
        self.button4.grid(row=2, column=2, ipadx=10)


app = FiboEnc()
app.mainloop()
