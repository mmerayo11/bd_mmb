
import sys

current_url = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    try:
        url, count_str = line.split('\t', 1)
        count = int(count_str)
    except ValueError:
        continue

    if current_url == url:
        current_count += count
    else:
        if current_url:
            print(f"{current_url}\t{current_count}")
        current_url = url
        current_count = count

if current_url:
    print(f"{current_url}\t{current_count}")
