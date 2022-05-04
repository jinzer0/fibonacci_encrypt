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

"""
a=1
b=1
finalkey=0

for i in range(3-1):

    a+=b
    b=a-b
finalkey=b
print(b)
"""