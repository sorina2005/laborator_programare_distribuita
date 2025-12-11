import math

print("--- Verificare Număr Prim (Script Simplu) ---")

numar = 0

# --- Pasul 1: Citire și Validare ---
# Nu trecem mai departe până nu primim un număr corect
while True:
    try:
        date_utilizator = input("Introdu un număr întreg pozitiv: ")

        # Încercăm conversia
        numar = int(date_utilizator)

        if numar < 0:
            print("Te rog introdu un număr pozitiv.")
            continue

        # Dacă a funcționat și e pozitiv, ieșim din bucla de validare
        break

    except ValueError:
        print("Ai introdus text. Te rog introdu un număr intreg(cifre).")

# --- Pasul 2: Logica de verificare ---
este_prim = True

if numar < 2:
    este_prim = False
else:
    # Verificăm divizorii până la radical din număr
    limita = int(math.sqrt(numar)) + 1

    for i in range(2, limita):
        if numar % i == 0:
            este_prim = False
            break

# --- Pasul 3: Afișare ---
print("-" * 30)
if este_prim:
    print(f"Rezultat: {numar} ESTE numar prim.")
else:
    print(f"Rezultat: {numar} NU este numar prim.")