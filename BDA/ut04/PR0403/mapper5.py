import sys
import re

LOG_PATTERN = re.compile(
    r'(\S+)\s+-\s+-\s+\[(.*?)\]\s+"(\S+)\s+(.*?)\s+(\S+)"\s+(\d+)\s+(\S+)\s+"(.*?)"\s+"(.*?)"'
)

for line in sys.stdin:
    line = line.strip()
    match = LOG_PATTERN.match(line)
    if match:
        user_agent = match.group(9).lower()
        
        if 'bot' in user_agent or 'spider' in user_agent or 'crawler' in user_agent:
            browser = "Bot/Crawler"
        elif 'chrome' in user_agent and 'safari' in user_agent and 'edge' not in user_agent:
            browser = "Chrome"
        elif 'firefox' in user_agent:
            browser = "Firefox"
        elif 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent:
            browser = "Móvil/Tablet"
        else:
            browser = "Otro/Desconocido"
            
        print(f"{browser}\t1")
