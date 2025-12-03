import sys

current_key= None
contador=0

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')

    if len(parts) < 3:
        continue
        
    city, year, temp_str = parts
    
    try:
        temp = float(temp_str)
    except ValueError:
        continue
        
    key = f"{city}\t{year}"
    
    if current_key and current_key != key:
        print(f"{current_key}\t{contador}")
        contador =0
    
    current_key = key

    if temp > 30:
        contador+=1

if current_key:
    print(f"{current_key}\t{contador}")