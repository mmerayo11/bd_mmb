import sys

current_url = None
total_requests = 0
total_errors = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    try:
        url, counts_str = line.split('\t', 1)
        success, error = map(int, counts_str.split(','))
    except ValueError:
        continue

    if current_url == url:
        total_requests += success + error
        total_errors += error
    else:
        if current_url:
            if total_requests > 0:
                error_rate = (total_errors / total_requests) * 100
                print(f"{current_url}\t{error_rate:.2f}%\t{total_requests}\t{total_errors}")
            else:
                print(f"{current_url}\t0.00%\t0\t0")
                
        current_url = url
        total_requests = success + error
        total_errors = error

if current_url:
    if total_requests > 0:
        error_rate = (total_errors / total_requests) * 100
        print(f"{current_url}\t{error_rate:.2f}%\t{total_requests}\t{total_errors}")
    else:
        print(f"{current_url}\t0.00%\t0\t0")
