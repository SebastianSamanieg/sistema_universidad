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

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, identificacion):
        self.__identificacion = identificacion

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, correo):
        self.__correo = correo