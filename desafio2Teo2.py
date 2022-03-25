palabra = input("ingrese palabaras hasta ingresar la palabra 'FIN' ")
while palabra != "FIN":
    if palabra[0] == palabra[len(palabra) -1]:
        print(palabra)
    palabra = input("ingrese palabaras hasta ingresar la palabra 'FIN' ")    
