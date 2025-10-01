frase = "Hola amigo soy Hola que tal hola estas ".lower()

palabras = frase.split()

frecuencia= {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra]+= 1
    else:
        frecuencia[palabra] = 1

print (f"Frecuencia de palabras: ")
for palabra, cantidad in frecuencia.items():
    print(f"{palabra}: {cantidad}")