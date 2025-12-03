import sys

current_country= None
contador = 0
total_temp = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')

    if len(parts) != 2:
        continue
        
    country, temp_str = parts
    
    try:
        temp = float(temp_str)
    except ValueError:
        continue

    if current_country and current_country != country:
        avg_temp = total_temp/contador
        print(f"{current_country}\t{round(avg_temp, 2)}")
        contador = 0
        total_temp = 0

    current_country = country
    total_temp += temp
    contador += 1   
    

if current_country and current_count > 0:
    avg_temp = total_temp / contador
    print(f"{current_country}\t{avg_temp}")