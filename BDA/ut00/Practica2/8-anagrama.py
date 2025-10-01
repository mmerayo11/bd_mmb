cad1 = input("Introduzca una palabra: ")
cad2 = input("Introduzca una palabra: ")

lista1 = cad1.split()
lista2 = cad2.split()

lista1Ord = lista1.sort()
lista2Ord = lista2.sort()

if lista1Ord==lista2Ord:
    print ("Son anagramas")
else:
    print ("No son anagramas")