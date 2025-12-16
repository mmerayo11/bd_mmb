
import sys
import re

LOG_PATTERN = re.compile(
    r'(\S+)\s+-\s+-\s+\[(.*?)\]\s+"(\S+)\s+(.*?)\s+(\S+)"\s+(\d+)\s+(\S+)\s+"(.*?)"\s+"(.*?)"'
)

for line in sys.stdin:
    line = line.strip()
    match = LOG_PATTERN.match(line)
    if match:
        ip = match.group(1)
        bytes_str = match.group(7)
        
        bytes_sent = bytes_str if bytes_str.isdigit() else '0'
        
        print(f"{ip}\t{bytes_sent}")
