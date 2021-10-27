class Asiento():
    def __init__(self, color="negro"):
        self.color = color


class Car():
    def __init__(self, marca, modelo):
        #
        self.asientos = [Asiento(), Asiento(), Asiento(), Asiento()]

class Convertible(Car):
    def __init__(self, marca, modelo):
        #
        self.asientos = [Asiento(), Asiento()]

honda_civic = Car(marca="Honda", modelo="Civic")

honda_civic.asientos[0].color = "rojo"

for asientos in honda_civic.asientos:
    print(asientos.color)

ferrari = Convertible(marca="Lamborgini", modelo="Aventador")