class Vehiculo():
    def __init__(self, placa):
        self.placa = placa


class Auto(Vehiculo):
    def __init__(self, placa, ocupantes=5, asientos=5):
        super().__init__(placa)
        self.ocupantes = ocupantes
        self.asientos = asientos


class Camioneta(Vehiculo):
    def __init__(self, placa, ocupantes=5, asientos=5, traccion=1):
        super().__init__(placa, ocupantes, asientos)
        self.traccion = traccion


class Motocicleta(Vehiculo):
    pass
