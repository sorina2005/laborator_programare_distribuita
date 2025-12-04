print("--- Convertor Temperatură (Celsius -> Fahrenheit) ---")

celsius = 0.0

# Pasul 1: Citire și Validare
# Repetăm întrebarea până primim un număr corect
while True:
    try:
        date_input = input("Introdu temperatura în grade Celsius: ")

        # Încercăm să convertim textul în număr cu zecimale (float)
        celsius = float(date_input)

        # Dacă linia de sus nu dă eroare, ieșim din buclă (break)
        break

    except ValueError:
        # Dacă utilizatorul a scris text, afișăm eroarea și bucla se reia
        print("Eroare! Te rog introdu un număr (ex: 25 sau 36.6).")

# Pasul 2: Calculul (formula matematică)
fahrenheit = (celsius * 9 / 5) + 32

# Pasul 3: Afișarea rezultatului
print("-" * 30)
# Folosim .2f pentru a afișa doar 2 zecimale
print(f"{celsius} grade Celsius înseamnă {fahrenheit:.2f} grade Fahrenheit.")