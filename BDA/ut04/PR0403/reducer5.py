import sys

current_browser = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    try:
        browser, count_str = line.split('\t', 1)
        count = int(count_str)
    except ValueError:
        continue

    if current_browser == browser:
        current_count += count
    else:
        if current_browser:
            print(f"{current_browser}\t{current_count}")
        current_browser = browser
        current_count = count

if current_browser:
    print(f"{current_browser}\t{current_count}")
