edad = input("Ingresar tu edad: ")

n = int(edad)

if n >= 18:
    print("Es mayor de edad")
elif n < 0:
    print("Edad inválida")
else:
    print("Es menor de edad")
