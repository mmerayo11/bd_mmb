cad = input("Introduzca una frase: ")

cadNueva=""

for l in cad:
    if l.islower():
        cadNueva += l.upper()
    elif l.isupper():
        cadNueva += l.lower()
    else:
        cadNueva += l

print (cadNueva)