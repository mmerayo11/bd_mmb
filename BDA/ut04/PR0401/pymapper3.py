import sys

for line in sys.stdin:
    line = line.strip()
    
    parts = line.split()
    
    if len(parts) == 2:
        word = parts[0]
        count = parts[1]
        
        try:
            count_padded = f"{int(count):010d}"
            print(f"{count_padded}\t{word}")
        except ValueError:
            continue