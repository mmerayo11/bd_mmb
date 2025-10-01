cad = input("Introduzca una frase: ")

cadNueva= ""
vistos=[]

for l in cad:
    if l not in vistos:
        cadNueva += l
        vistos.append(l)

print (cadNueva)