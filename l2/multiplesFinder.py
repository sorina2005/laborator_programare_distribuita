def multiples_finder():
    print("--- Cautator de Multipli ---")

    try:
        # Pasul 1: Citirea datelor
        input_x = input("Introduceti numarul baza (x): ")
        input_y = input("Introduceti limita superioara (y): ")

        # Conversia in numere intregi (integer)
        x = int(input_x)
        y = int(input_y)

        # Pasul 2: Validari logice (Exceptii specifice logicii matematice)

        # Cazul x = 0: 0 nu poate fi folosit ca pas intr-un range si ar genera eroare
        if x == 0:
            print("Eroare: Numarul x nu poate fi 0.")
            return

        # Cazul numerelor negative (pentru simplificare, cerem numere pozitive)
        if x < 0:
            print("Atentie: Acest program este optimizat pentru numere pozitive.")
            return

        # Pasul 3: Generarea multiplilor
        # Folosim functia range(start, stop, step)
        # start = x (primul multiplu este chiar x)
        # stop = y (ne oprim inainte de y)
        # step = x (sarim din x in x)
        multipli = list(range(x, y, x))

        # Pasul 4: Afisarea rezultatului
        if len(multipli) > 0:
            # *multipli (cu steluta) despacheteaza lista pentru a o afisa frumos fara paranteze
            print(f"Multiplii lui {x} mai mici decat {y} sunt:", *multipli)
        else:
            print(f"Nu exista multipli ai lui {x} mai mici decat {y}.")

    except ValueError:
        # Pasul 5: Tratarea erorii de tip input gresit (litere in loc de cifre)
        print("Eroare de input: Va rugam sa introduceti doar numere intregi (fara litere).")


while True:
    multiples_finder()
    if input("Vrei sa continui? (n for no, anything for yes): ") == "n":
        break