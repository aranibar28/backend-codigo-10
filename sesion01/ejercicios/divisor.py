# Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

a = int(input("Ingrese número 1: "))
b = int(input("Ingrese número 2: "))

if b != 0:
    resultado = a / b
    print(f"El resultado es: {resultado}")
else:
    print("Error papu ingresa otro número")
