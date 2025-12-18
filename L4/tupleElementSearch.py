def cautare_in_tupla():
    print("\n*** Program Căutare în Tuplă ***")

    while True:
        try:
            # 1. Citirea și crearea tuplei
            raw_input = input("\nInput (valori separate prin virgulă): ")

            # Validare input gol
            if not raw_input.strip():
                raise ValueError("Inputul nu poate fi gol.")

            # Transformăm inputul într-o tuplă de string-uri, curățând spațiile
            # Ex: "1, 2,  3 " -> ("1", "2", "3")
            # Folosim string-uri pentru a permite orice tip de caractere
            date_tupla = tuple(x.strip() for x in raw_input.split(','))

            print(f"-> Tupla creată: {date_tupla}")

            # 2. Citirea valorii de căutat
            valoare_cautata = input("Search for: ").strip()

            # 3. Căutarea valorii folosind tratarea excepțiilor
            # Metoda .index() aruncă ValueError dacă elementul nu există
            index_gasit = date_tupla.index(valoare_cautata)

            # Dacă linia de mai sus nu dă eroare, înseamnă că a găsit valoarea
            print("-" * 40)
            print(f" '{valoare_cautata}' se regăsește în tuplă la indexul {index_gasit}.")
            print("-" * 40)

            # Ieșim din buclă după o execuție cu succes
            break

        except ValueError as e:
            # Aici prindem DOUĂ tipuri de erori:
            # A. Eroarea generată de noi dacă inputul e gol
            # B. Eroarea generată de .index() dacă valoarea nu e în tuplă

            error_message = str(e)

            if "tuple.index(x): x not in tuple" in error_message:
                print("-" * 40)
                # Acesta este cazul în care valoarea nu a fost găsită
                print(f" Valoarea '{valoare_cautata}' NU se regăsește în tuplă.")
                print("-" * 40)
                break  # Considerăm că programul a rulat corect (chiar dacă nu a găsit), deci ieșim
            else:
                # Alte erori (ex: input gol) - cerem input din nou
                print(f" Eroare: {e}")
                print("Te rog încearcă din nou.")



cautare_in_tupla()