
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
        if url: 
            print(f"{url}\t1")
