import re

with open("data.txt", "r") as file:
    file_open = file.read()

array = file_open.strip()

# Regex per catturare le istruzioni
regex = r"(don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\))"

# Trova tutte le istruzioni
istruzioni = re.findall(regex, array)

# Variabili per tracciare lo stato e il risultato
attivo = True  # Mul attivo di default
somma = 0

for istruzione in istruzioni:
    if istruzione[0] == "don't()":
        attivo = False  # Disabilita mul()
    elif istruzione[0] == "do()":
        attivo = True  # Riabilita mul()
    elif istruzione[1] and istruzione[2]:  # È un'istruzione mul()
        if attivo:  # Calcola solo se mul() è abilitato
            somma += int(istruzione[1]) * int(istruzione[2])

print("Somma totale:", somma)
