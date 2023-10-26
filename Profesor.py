from Persona import Persona

class Profesor(Persona):
    
    def __init__(self, nombre, identificacion, correo, codigo_empleado) -> None:
        super().__init__(nombre, identificacion, correo)
        self.__codigo_empleado = codigo_empleado

    @property
    def codigo_empleado(self):
        return self.__codigo_empleado
    
    @codigo_empleado.setter
    def codigo_empleado(self, valor):
        self.__codigo_empleado = valor