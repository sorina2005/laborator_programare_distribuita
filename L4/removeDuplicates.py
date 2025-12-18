def elimina_duplicate():
    print("\n*** Program Eliminare Duplicate (Păstrând Ordinea) ***")
    print("Exemplu input: 1, 1, 2, 3, 4, 4, 5, 4")

    while True:
        try:
            # 1. Citirea inputului
            user_input = input("\nIntrodu lista de numere: ")

            # Validare input gol
            if not user_input.strip():
                raise ValueError("Inputul nu poate fi gol.")

            # 2. Procesare: String -> Listă de numere întregi
            # Folosim list comprehension pentru a curăța spațiile și a converti la int
            lista_initiala = []
            parti = user_input.split(',')

            for p in parti:
                p_clean = p.strip()
                if p_clean:  # Ignorăm eventuale elemente goale (ex: "1, 2,")
                    lista_initiala.append(int(p_clean))

            if not lista_initiala:
                raise ValueError("Nu am detectat numere valide.")

            # 3. Logica de eliminare duplicate (Păstrând ordinea)
            lista_unica = []
            vazute = set()  # Set-ul este folosit pentru căutare rapidă (O(1))

            for numar in lista_initiala:
                if numar not in vazute:
                    lista_unica.append(numar)  # Adăugăm în lista finală
                    vazute.add(numar)  # Marcăm ca "văzut"

            # 4. Formatare și Afișare output
            # Convertim înapoi în string pentru a afișa frumos cu virgulă
            rezultat_string = ", ".join(str(x) for x in lista_unica)

            print("-" * 40)
            print(f" Lista inițială: {lista_initiala}")
            print(f" Lista unică:    {rezultat_string}")
            print("-" * 40)

            # Ieșim din buclă la succes
            break

        except ValueError as e:
            # Prindem erorile de conversie int() sau cele ridicate manual
            print("-" * 40)
            if "invalid literal for int()" in str(e):
                print(" Eroare: Ai introdus caractere care nu sunt numere.")
            else:
                print(f" Eroare: {e}")
            print("Te rog introdu numere separate prin virgulă (ex: 1, 2, 2, 3).")
            print("-" * 40)



elimina_duplicate()