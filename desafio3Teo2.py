lista = []
notas = int(input("ingrese notas hasta que ingrese la nota = -1: "))
cant = 0
total = 0
while notas != -1:
    cant += 1
    total += notas
    lista.append(notas)
    notas = int(input("ingrese notas hasta que ingrese la nota = -1: "))
promedio = total / cant
print(f"el promedio de notas es {promedio:5} y ahora mostramos las notas que estan por debajo del mismo ")
for elem in lista:
    if elem < promedio:
        print(elem)