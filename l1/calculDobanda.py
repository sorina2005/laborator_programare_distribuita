print("--- Calculator de Dobanda simpla (cu Validare) ---")

principal = 0.0
rata = 0.0
timp = 0.0

# --- Pasul 1: Citire și Validare ---
while True:
    try:
        # Cerem toate cele 3 valori în interiorul blocului 'try'
        # Dacă oricare dintre ele e greșită, sare direct la 'except'
        principal = float(input("Introdu suma principala (Principal): "))
        rata = float(input("Introdu rata anuală a dobanzii (fara %, ex: 5): "))
        timp = float(input("Introdu perioada in ani (Time): "))

        # Validare logică: Nu acceptăm numere negative
        if principal < 0 or rata < 0 or timp < 0:
            print("Te rog introdu doar valori pozitive. Încearcă din nou.")
            print("-" * 15)
            continue # Reia bucla

        # Dacă am ajuns aici, toate 3 sunt numere corecte
        break 

    except ValueError:
        print("Eroare! Ai introdus text în loc de număr. Te rog reia datele.")
        print("-" * 15)

# --- Pasul 2: Calculăm dobânda (Processing) ---
# Formula: (P * R * T) / 100
dobanda = (principal * rata * timp) / 100

# Calculăm și suma totală
total = principal + dobanda

# --- Pasul 3: Afișăm rezultatul (Output) ---
print("-" * 30)
print(f"Suma Principala: {principal}")
print(f"Dobanda calculată: {dobanda:.2f}") # .2f afișează doar 2 zecimale
print(f"Total (Principal + Dobanda): {total:.2f}")