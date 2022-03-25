import string


def ingreso_notas():
""" Esta función retorna un diccionario con los nombres y notas de estudiantes """
nombre = input("Ingresa un nombre (<FIN> para finalizar)")
dicci = {}
while nombre != "FIN":
    nota = int(input(f"Ingresa la nota de {nombre}"))
    dicci[nombre] = nota
    nombre = input("Ingresa un nombre (<FIN> para finalizar)")
return dicci

def 
notas_de_estudiantes = ingreso_notas()
notas_de_estudiantes