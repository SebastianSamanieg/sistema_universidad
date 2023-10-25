class Programa:

    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__estudiantes = []
        self.__asignaturas = []


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def estudiantes(self):
        return self.__estudiantes
    
    @property
    def asignaturas(self):
        return self.__asignaturas
    

    def agregar_estudiantes(self, estudiante):
        self.__estudiantes.append(estudiante)

    def agregar_asignaturas(self, asignatura):
        self.__asignaturas.append(asignatura)