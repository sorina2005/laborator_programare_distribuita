def gaseste_min_max():
    print("\n*** Program Determinare Minim și Maxim ***")
    print("Instrucțiune: Introdu numere întregi separate prin virgulă (ex: 10, -5, 20, 3)")

    while True:
        user_input = input("\nIntrodu lista de numere: ")

        try:
            # 1. Verificăm dacă inputul este gol
            if not user_input.strip():
                raise ValueError("Inputul nu poate fi gol.")

            # 2. Procesare: Split + Convertire
            # - user_input.split(',') -> împarte șirul unde găsește virgule
            # - x.strip() -> elimină spațiile inutile (ex: " 5 " devine "5")
            # - int(...) -> convertește textul în număr întreg
            lista_str = user_input.split(',')
            lista_numere = []

            for element in lista_str:
                # Verificăm elementele goale (ex: "1,,2")
                if element.strip() == "":
                    continue
                lista_numere.append(int(element.strip()))

            # 3. Verificăm dacă lista rezultată conține numere
            if not lista_numere:
                raise ValueError("Nu au fost introduse numere valide.")

            # 4. Calculare Min și Max folosind funcțiile built-in
            val_max = max(lista_numere)
            val_min = min(lista_numere)

            # 5. Afișare Rezultat
            print("-" * 40)
            print(f" Lista finală: {lista_numere}")
            print(f" Valoarea Maximă: {val_max}")
            print(f" Valoarea Minimă: {val_min}")
            print("-" * 40)

            # Ieșim din bucla while după succes
            break

        except ValueError as e:
            # Prindem erorile de conversie (dacă scrie litere) sau cele ridicate manual
            print("-" * 40)
            # Verificăm dacă eroarea vine de la funcția int()
            if "invalid literal for int()" in str(e):
                print(f" Eroare de conversie: Ai introdus caractere care nu sunt cifre.")
                print(f"   Detaliu tehnic: {e}")
            else:
                print(f" Eroare: {e}")
            print("Te rog încearcă din nou, folosind doar cifre și virgule.")
            print("-" * 40)


# Rularea programului
gaseste_min_max()