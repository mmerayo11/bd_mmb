import sys
import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(\S+)\s+-\s+-\s+\[(.*?)\]\s+"(\S+)\s+(.*?)\s+(\S+)"\s+(\d+)\s+(\S+)\s+"(.*?)"\s+"(.*?)"'
)
LOG_TIME_FORMAT = '%d/%b/%Y:%H:%M:%S %z'

for line in sys.stdin:
    line = line.strip()
    match = LOG_PATTERN.match(line)
    if match:
        timestamp_raw = match.group(2)
        
        try:
            dt_obj = datetime.strptime(timestamp_raw, LOG_TIME_FORMAT)
            hour = dt_obj.strftime('%H')
            print(f"{hour}\t1")
        except ValueError:
            print("Error_Hora\t1")
