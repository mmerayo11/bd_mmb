cad = input("Introduzca un palindromo: ")

if cad == cad[::-1]:
    print("Es un palindromo")
else:
    print("Incorrecto, eso no es un palindromo")