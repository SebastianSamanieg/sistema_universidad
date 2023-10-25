class Persona:

    def __init__(self, nombre, identificacion, correo) -> None:
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre