from Persona import Persona

class Estudiante(Persona):
    
    def __init__(self, nombre, identificacion, correo, codigo, promedio) -> None:
        super().__init__(nombre, identificacion, correo)
        self.__codigo = codigo
        self.__promedio = promedio

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def promedio(self):
        return self.__promedio
    
    @promedio.setter
    def promedio(self, valor):
        self.__promedio = valor
