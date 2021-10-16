class Empleado:
    def __init__(self, nombre, apellido, salario, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.dni = dni

    def reportar(self):
        print(f"{self.nombre} Reportó")


class Vendedor(Empleado):
    def vender(self):
        print(f"{self.nombre} Vendió")


class Contador(Empleado):
    def __init__(self, nombre, apellido, salario, dni, cod_colegiatura):
        super().__init__(nombre, apellido, salario, dni)
        self.cod_colegiatura = cod_colegiatura

    def declarar_impuestos(self):
        print(f"{self.nombre} declaró impuestos")


contador1 = Contador("Gerson", "Aranibar", 5000, 70800756, 52915)
contador1.declarar_impuestos()
contador1.reportar()
