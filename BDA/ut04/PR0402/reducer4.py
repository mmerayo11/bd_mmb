import sys

current_region = None
min_temp = float('inf')  
max_temp = float('-inf')

for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')

    if len(parts) != 2:
        continue

    region, temp_str = parts

    try:
        temp = float(temp_str)
    except ValueError:
        continue

    if current_region and current_region != region:
        print(f"{current_region}\tMin: {min_temp}\tMax: {max_temp}")
        
        min_temp = float('inf')
        max_temp = float('-inf')

    current_region = region

    if temp < min_temp:
        min_temp = temp
    
    if temp > max_temp:
        max_temp = temp

if current_region:
    print(f"{current_region}\tMin: {min_temp}\tMax: {max_temp}")