cad = input("Introduzca una frase: ")

palabras= cad.split(" ")

palabrasInvert = palabras[::-1]

nuevaCadena = " ".join(palabrasInvert)

print (nuevaCadena)