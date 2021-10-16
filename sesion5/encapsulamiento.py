class Empleado:
    def __init__(self, nombre, dni, salario=930):
        self.nombre = nombre
        self.__salario = salario
        self.__dni = dni

    def setSalario(self, monto):
        if monto >= 930:
            self.__salario = monto
        else:
            raise Exception("Mínimo sueldo permitido: 930")

    def __getSalario(self):
        salario_base = self.__salario
        return salario_base * 0.89

    def pagar(self):
        salario_final = self.__getSalario()
        print ("Salario pagado")

    def getDni(self):
        return self.__dni


empleado1 = Empleado("Gerson", 70800756, 2000)
empleado2 = Empleado("Diego", 70800756)
empleado2.setSalario(1500)

print(empleado1.nombre)
print(empleado1._Empleado__salario)
print(empleado1.getDni())
