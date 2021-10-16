import random

f = open("prueba.txt", "r")
l = f.readline()
""" print(l) """

for i in range(0, 10):
    r1 = f.read(i)
    """ print(r1) """

f.close()

f = open("ouput.txt", "w")
for i in range(0, 10):
    aleatorio = str(random.random())
    f.write(f"{aleatorio}\n")
f.close()

f = open("ouput.txt", "a")
for i in range(0, 5):
    aleatorio = str(random.random())
    f.write(f"{aleatorio}\n")
f.close()

col = ["4.234234\n", "1.1222544\n", "8.41212454\n", "9.70800756\n"]
f = open("ouput.txt", "a")
f.writelines(col)
f.close()
