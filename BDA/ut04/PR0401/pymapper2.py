import sys
import string
palabrasNoSignificaticas = [
    "a", "ante", "bajo", "con", "contra", "de", "desde", "en", "entre", "hacia", "hasta", "para", "por", "según", "sin", "sobre", "tras", "y", "e", "ni", "o", "u", "pero", "porque", "aunque",  "si",         "que", "el", "la", "los", "las", "un", "una", "unos", "unas", "este", "esta", "estos", "estas", "ese", "esa", "esos",
    "esas", "aquel", "aquella", "aquellos", "aquellas", "mi", "tu", "su", "mis",
    "tus", "sus", "nuestro", "nuestra", "nuestros", "nuestras", "vuestro", "vuestra", "vuestros", "vuestras", "del", "se"
]

traductor = str.maketrans('', '', string.punctuation)

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    
    for word in words:
        word = word.translate(traductor)
        word = word.lower()

        if word and word not in palabrasNoSignificaticas:
            print(f"{word}\t1")