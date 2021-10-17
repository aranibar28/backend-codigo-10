# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

num = int(input("Ingrese número: "))

if num % 2 == 0:
    print("Es número par")
else:
    print("Es número impar")