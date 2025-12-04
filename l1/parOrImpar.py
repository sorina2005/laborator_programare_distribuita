print("--- Verificare Paritate (Par/Impar) ---")

number = 0

# --- Pasul 1: Citire și Validare ---
while True:
    try:
        # Citim de la tastatură
        input_utilizator = input("Numar care urmeaza a fi verificat: ")

        # Încercăm conversia în număr întreg (int)
        number = int(input_utilizator)

        # Dacă a reușit conversia, ieșim din buclă
        break
    except ValueError:
        print("Eroare! Te rog introdu un număr întreg valid (fără litere sau virgulă).")

# --- Pasul 2: Verificarea propriu-zisă ---
# Un număr este par dacă restul împărțirii la 2 este 0
if number % 2 == 0:
    print(f"{number} este un număr par.")
else:
    print(f"{number} este un număr impar.")