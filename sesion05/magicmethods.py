class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def getDni(self):
        print(super().__getattribute__("dni"))

    def __getattribute__(self, attr):
        print(f"Atributo {attr} solicitado: ")
        if attr == "dni":
            return ("*********")
        else:
            return super().__getattribute__(attr)
    
    def __setattr__(self, attr, value):
        print(f"Se asigna el valor de {value} a {attr}")


persona1 = Persona("Dora", 70800756)

print(persona1.nombre)
print(persona1.dni)

persona1.getDni()