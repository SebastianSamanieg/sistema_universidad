class Asignatura:

    def __init__(self,nombre, creditos) -> None:
        self.__nombre = nombre
        self.__creditos = creditos

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre =  valor
    
    @property
    def creditos(self):
        return self.__creditos
    
    @creditos.setter
    def creditos(self, valor):
        self.__creditos =  valor