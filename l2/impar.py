def odd_numbers_generator():
    print("--- Generator Numere Impare ---")

    try:
        # Pasul 1: Citirea lui n
        input_n = input("Introdu n: ")
        n = int(input_n)

        # Validare: Programul are sens doar pentru numere pozitive
        if n <= 0:
            print("Te rog introdu un numar pozitiv (mai mare ca 0).")
            return

        # Pasul 2: Generarea numerelor
        impare = list(range(1, n + 1, 2))

        # Pasul 3: Afișarea
        # Folosim * (asterisc) pentru a scoate elementele din listă
        # sep=", " pune virgula doar între numere, nu și la final
        print(f"Numerele impare pana la {n} sunt:")
        print(*impare, sep=", ")

    except ValueError:
        print("Eroare: Te rog introdu un număr întreg valid.")

while True:
    odd_numbers_generator()
    if input("Vrei sa continui? (n for no, anything for yes): ") == "n":
        break
