import sys

current_hour = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    try:
        hour, count_str = line.split('\t', 1)
        count = int(count_str)
    except ValueError:
        continue

    if current_hour == hour:
        current_count += count
    else:
        if current_hour and current_hour != "Error_Hora":
            print(f"{current_hour}\t{current_count}")
        current_hour = hour
        current_count = count

if current_hour and current_hour != "Error_Hora":
    print(f"{current_hour}\t{current_count}")
