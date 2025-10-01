asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

while True:
        print("Menú.")
        print("1. Listar estudiantes por asignatura.")
        print("2. Matricular estudiante.")
        print("3. Dar baja.")
        print("4. Salir")
        opcion = input("Escoja una opción: ")

        if opcion == "1":
            tipo = input("Ingrese la asignatura: ").capitalize()
            if tipo in asignaturas:
                print(f"Estudiantes en {tipo}:")
                for alumno in asignaturas[tipo]:
                    print("-", alumno)
            else:
                print("La asignatura no existe.")

        elif opcion == "2":
            tipo = input("Ingrese la asignatura: ").capitalize()
            if tipo in asignaturas:
                alumno = input("Nombre del estudiante a matricular: ").capitalize()
                if alumno not in asignaturas[tipo]:
                    asignaturas[tipo].append(alumno)
                    print(f"{alumno} matriculado en {tipo}.")
                else:
                    print(f"{alumno} ya está matriculado en {tipo}.")
            else:
                print("La asignatura no existe.")

        elif opcion == "3":
            tipo = input("Ingrese la asignatura: ").capitalize()
            if tipo in asignaturas:
                print(f"Estudiantes en {tipo}:")
                for alumno in asignaturas[tipo]:
                    print("-", alumno)
                alumno = input("Nombre del estudiante a dar de baja: ").capitalize()
                if alumno in asignaturas[tipo]:
                    asignaturas[tipo].remove(alumno)
                    print(f"{alumno} dado de baja en {tipo}.")
                else:
                    print(f"{alumno} no está matriculado en {tipo}.")
            else:
                print("La asignatura no existe.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, inténtelo de nuevo.")