estudiantes = {
    "Ana": {"Matemáticas": 8.5, "Física": 9.0, "Programación": 7.8},
    "Carlos": {"Matemáticas": 9.2, "Física": 8.8, "Programación": 9.4},
    "Luis": {"Matemáticas": 7.6, "Física": 8.0, "Programación": 8.5},
    "María": {"Matemáticas": 9.5, "Física": 10.0, "Programación": 9.8},
    "Jorge": {"Matemáticas": 8.8, "Física": 8.4, "Programación": 7.9},
    "Sofía": {"Matemáticas": 9.1, "Física": 8.9, "Programación": 9.3}
}

mediaEstudiantes = {}

mediaAsig={}
conteoAsig={}

for nombre, notas in estudiantes.items():
    media = sum(notas.values())/ len(notas)
    mediaEstudiantes[nombre] = round(media,2)
    
for notas in estudiantes.values():
    for asig, calif in notas.items():
        if asig not in mediaAsig:
            mediaAsig[asig]= 0
            conteoAsig[asig] = 0
        mediaAsig[asig] += calif  
        conteoAsig[asig] += 1 

for asig in mediaAsig:
    mediaAsig[asig] = round(mediaAsig[asig] / conteoAsig[asig], 2)

print("Promedio por estudiante:")
print(mediaEstudiantes)

print("\nPromedio por asignatura:")
print(mediaAsig)   
        
            