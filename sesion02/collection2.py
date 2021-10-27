# 1. summar todos los elementos numericos

col2 = [3, 5, 8, 9, 13, "4"]

suma = 0

for x in col2:
    if type(x) == int:
        suma = suma + x
print (suma)
