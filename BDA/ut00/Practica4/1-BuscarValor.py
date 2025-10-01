dic1= {
    "manzana": 1.20,
    "pera": 1.50,
    "naranja": 0.90,
    "plátano": 1.10,
    "uva": 2.50
}

fruta= input("Introduzca una fruta:")

if fruta in dic1:
    print(dic1[fruta])
else:
    print ("No disponemos de esa fruta")
    
