cad = input("Introduzca una palabra codificada RLE: ")

nuevaCad = []

for l in cad:
    if l.isdigit():
        r = int(l)
        nuevaCad.extend([i]* (r-1))
    else:
        i = l
        nuevaCad.append(l)

print("".join(nuevaCad))