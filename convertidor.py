import random
lines = open('frases.txt').read()
lineas_filtradas =  lines.replace("\"", "").replace("\'", "").split(',')
with open('frases_convertido.txt', 'w') as f:
    for line in lineas_filtradas:
        f.write(f"{line}\n")