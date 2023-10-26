from Persona import Persona
from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura
from Programa import Programa

persona1 = Persona('Debora', '111', 'debora@konrad')

print(persona1.nombre)
persona1.nombre = 'Flor'
print(persona1.nombre)

estudiante1 = Estudiante('Maria', '222', 'maria@konrad', '61622023', 40)
estudiante2 = Estudiante('Pablo', '333', 'pablo@konrad', '61622024', 45)

print(f'Est1: {estudiante1.codigo} - Est2 {estudiante2.codigo}')
print(f'Est1: {estudiante1.nombre} - Est2 {estudiante2.nombre}')

asignatura1 = Asignatura('Bases de datos', 3)
asignatura2 = Asignatura('Programacion I', 3)

print(f'As1: {asignatura1.nombre} - Creditos: {asignatura1.creditos}')
print(f'As2: {asignatura2.nombre} - Creditos: {asignatura2.creditos}')

p1 = Programa('Ingeniería de Sistemas')
p2 = Programa('Negocios')


estudiante3 = Estudiante('Camila', '444', 'camila@konrad', '61622025', 41)
estudiante4 = Estudiante('Roberto', '555', 'roberto@konrad', '61622026', 42)

profesor1 = Profesor('Leandro', '333', 'leandro@konrad', '61622028')
profesor2 = Profesor('Oscar', '777', 'oscar@konrad', '61622029')

print(f'Prof1: {profesor1.nombre} - Prof2 {profesor2.nombre}')

p1.agregar_estudiantes(estudiante1)
p1.agregar_estudiantes(estudiante2)
p1.agregar_estudiantes(estudiante3)


p2.agregar_estudiantes(estudiante4)

asignatura3 = Asignatura('Electiva I', 2)
asignatura4 = Asignatura('Mercadeo', 3)
asignatura5 = Asignatura('Teoría Admin', 2)

p1.agregar_asignaturas(asignatura1)
p1.agregar_asignaturas(asignatura2)
p1.agregar_asignaturas(asignatura3)
p2.agregar_asignaturas(asignatura4)
p2.agregar_asignaturas(asignatura5)


lista_programas = []
lista_programas.append(p1)
lista_programas.append(p2)

print('*'*15)

for p in lista_programas:
    print(p.nombre)
    for a in p.asignaturas:
        print(f'Asignatura: {a.nombre} - Creditos: {a.creditos}')
    print('*'*15)
