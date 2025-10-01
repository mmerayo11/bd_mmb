dic1= {
    "manzana": 1.20,
    "pera": 1.50,
    "naranja": 0.90,
    "plátano": 1.10,
    "uva": 2.50
}

dic2 = {}

for clave, valor in dic1.items():
    if valor in dic2:
        dic2[valor].append(clave)
    else:
        dic2[valor] = [clave]

print (dic2)