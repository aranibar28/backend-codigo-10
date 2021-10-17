# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key = "password"
password = input("Introduce el password: ")
if key == password.lower():
    print("El password es correcto")
else:
    print("El password es incorrecto")
