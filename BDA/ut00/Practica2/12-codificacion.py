cad = input("Introduzca una palabra: ")

nuevaCad=[]
contador= 1
caracter_anterior= cad[0]

for i in cad[1:]:
    if i == caracter_anterior:
        contador +=1
    else:
        nuevaCad.append(f"{caracter_anterior}{contador}")
        caracter_anterior = i
        contador = 1

nuevaCad.append(f"{caracter_anterior}{contador}")

print ("".join(nuevaCad))