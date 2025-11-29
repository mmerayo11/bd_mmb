import sys
import string

traductor = str.maketrans('', '', string.punctuation)

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    
    for word in words:
        word = word.translate(traductor)
        word = word.lower()
        print(f"{word}\t1")