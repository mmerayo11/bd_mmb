import sys

current_method = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    try:
        method, count_str = line.split('\t', 1)
        count = int(count_str)
    except ValueError:
        continue

    if current_method == method:
        current_count += count
    else:
        if current_method:
            print(f"{current_method}\t{current_count}")
        current_method = method
        current_count = count

if current_method:
    print(f"{current_method}\t{current_count}")
