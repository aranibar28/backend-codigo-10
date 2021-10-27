edad = input("Ingresar tu edad: ")

n = int(edad)

if n >= 18:
    print("Eres mayor de edad")
elif n < 0:
    print("Edad inválida")
else:
    print("Eres menor de edad")
