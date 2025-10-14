empleados = {"Mario" : 1500, "Miguel" : 1400, "Jesús" : 970, "Marta" : 2000}

umbral = 1000

empleadosNuevo = {}

for nombre, salario in empleados.items():
    if salario > umbral:
        empleadosNuevo[nombre]= salario

print (empleadosNuevo)