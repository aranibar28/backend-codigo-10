# Escribir una funcion que retorna verdadero 
# Si la palabra ingresada como parametro es palindroma

def invertir(cadena):
    invertida = ""
    for i in cadena:
        invertida = i + invertida
    return invertida

def palindroma(cadena):
    palabra = invertir(cadena)
    if cadena != palabra:
        return False
    else:
        return True

texto = palindroma("alla")
print(texto)