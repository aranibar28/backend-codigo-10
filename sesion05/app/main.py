from lib.converter import Converter
from lib.parser import pedir_centigrados

n = input("Ingrese grados centigrados: ")

degrees = float(n)
result = Converter.ctof(degrees)

print(f"Farenheit: {result}")
