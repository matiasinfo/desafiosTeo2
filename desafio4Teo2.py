
def ingreso_notas():
    """ Esta función retorna un diccionario con los nombres y notas de estudiantes """
    nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    dicci = {}
    while nombre != "FIN":
        nota = int(input(f"Ingresa la nota de {nombre}: "))
        dicci[nombre] = nota
        nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    return dicci


def calcular_promedio(dicci):
    """ esta funcion recibe un diccionario y retorna el promedio de las notas"""
    notas= dicci.values()
    total = 0
    for elem in notas:
        total += elem
    return total / len(dicci)


def reporte(dicci, promedio):
    """en este metodo se genera una lista de alumnosvde alumnos,
        que estan por debajo de la nota promedio"""
    alumnos_complicados = []
    for elem in dicci:
        if dicci[elem] < promedio:
            alumnos_complicados.append(elem)
    return alumnos_complicados


notas_de_estudiantes = ingreso_notas()
promedio = calcular_promedio(notas_de_estudiantes)
alumnos = reporte(notas_de_estudiantes, promedio)
# como tengo que tratar este tipo de lineas que son demaciado largas?
print(f"el promedio de las notas es: {promedio:5} ,  y los alumnos que tienen notas por debajo del primedio son: {alumnos}")