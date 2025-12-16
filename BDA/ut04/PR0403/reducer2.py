
import sys

current_ip = None
total_bytes = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    try:
        ip, bytes_str = line.split('\t', 1)
        bytes_sent = int(bytes_str)
    except ValueError:
        continue

    if current_ip == ip:
        total_bytes += bytes_sent
    else:
        if current_ip:
            print(f"{current_ip}\t{total_bytes}")
        current_ip = ip
        total_bytes = bytes_sent

if current_ip:
    print(f"{current_ip}\t{total_bytes}")
