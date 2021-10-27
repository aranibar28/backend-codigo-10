# Escribir una funcion que recibe un texto y retorna el texto invertido.
# Ejemplo: "hello world" -> "dlorw olleh"

def invertir_1(cadena):
    invertir = list(cadena)
    return invertir[::-1]
cadena = invertir_1("Hello World")
texto = "".join(cadena)
print(texto)

def invertir_2(cadena):
    cadenaText = ""
    for i in cadena:
        cadenaText = i + cadenaText
    return cadenaText
texto = invertir_2("Hello World")
print(texto)