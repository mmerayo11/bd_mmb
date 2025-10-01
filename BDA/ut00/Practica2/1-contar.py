cad = input("Introduzca una cadena: ")

vocales = "aeiouáéíóúü"
consonantes = "bcdfghjklmnñpqrstvwxyz"

contador_vocales = 0
contador_consonantes = 0
    
for caracter in cad.lower():
        if caracter in vocales:
            contador_vocales += 1
        elif caracter in consonantes:
            contador_consonantes += 1
    
print (f"Número de vocales:  {contador_vocales}, número de consonantes:  {contador_consonantes}")