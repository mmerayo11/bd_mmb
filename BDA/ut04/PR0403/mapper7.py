import sys
import re

LOG_PATTERN = re.compile(
    r'(\S+)\s+-\s+-\s+\[(.*?)\]\s+"(\S+)\s+(.*?)\s+(\S+)"\s+(\d+)\s+(\S+)\s+"(.*?)"\s+"(.*?)"'
)

for line in sys.stdin:
    line = line.strip()
    match = LOG_PATTERN.match(line)
    if match:
        url = match.group(4)
        status_code_str = match.group(6)
        
        try:
            status_code = int(status_code_str)
        except ValueError:
            continue
        
        if status_code >= 400:
            print(f"{url}\t0,1")
        else:
            print(f"{url}\t1,0")
