import sys

current_city= None
max_temp= 9999

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')

    if len(parts) != 2:
        continue
        
    city, temp_str = parts
    
    try:
        temp = float(temp_str)
    except ValueError:
        continue

    if current_city and current_city != city:
        print(f"{current_city}\t{max_temp}")
        max_temp = -9999.0 # Reiniciamos para la nueva ciudad
    
    current_city = city

    if temp > max_temp:
        max_temp = temp

if current_city:
    print(f"{current_city}\t{max_temp}")