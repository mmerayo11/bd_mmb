productos1 = {"Manzana": 2, "Pera": 3, "Plátano": 1}
productos2 = {"Pera": 4, "Plátano": 2, "Naranja": 5}

combinado = productos1.copy()

for producto, precio in productos2.items():
    if producto in combinado:
        combinado[producto] += precio
    else:
        combinado[producto] = precio


print("Diccionario combinado:", combinado)