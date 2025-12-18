import string


def inverted_index(documents):
    """
    Creează un index inversat dintr-o listă de documente.
    Mapează fiecare cuvânt la un set de indecși de documente.
    """
    # 1. Validare Tip Input
    if not isinstance(documents, list):
        raise TypeError("Inputul trebuie să fie o listă de șiruri de caractere.")

    index_map = {}

    # Folosim enumerate pentru a avea acces și la index (0, 1, 2...) și la text
    for doc_id, text in enumerate(documents):

        # 2. Validare Element Listă
        if not isinstance(text, str):
            print(f"⚠ Avertisment: Elementul de la indexul {doc_id} nu este text. A fost ignorat.")
            continue

        # 3. Procesare Text (Normalizare)
        # a. Lowercase (pentru a trata "Pisica" la fel cu "pisica")
        text_lower = text.lower()

        # b. Eliminare punctuație (folosind metoda eficientă translate)
        # Eliminăm semne precum . , ! ? " etc.
        tabela_curatare = str.maketrans('', '', string.punctuation)
        text_curat = text_lower.translate(tabela_curatare)

        # c. Tokenizare (spargere în cuvinte)
        cuvinte = text_curat.split()

        # 4. Construire Index
        for cuvant in cuvinte:
            # Dacă cuvântul nu e în dicționar, îl adăugăm cu un set gol
            if cuvant not in index_map:
                index_map[cuvant] = set()

            # Adăugăm ID-ul documentului în setul cuvântului
            # Set-urile se ocupă automat de unicitate (dacă cuvântul apare de 2 ori în același doc)
            index_map[cuvant].add(doc_id)

    return index_map


def run_app():
    print("\n*** Generator de Index Inversat ***")
    print("Instrucțiuni: Introdu documente (propoziții) una câte una.")
    print("Scrie 'STOP' sau 'GATA' când ai terminat de introdus lista.")

    lista_documente = []

    # Etapa 1: Colectarea Datelor
    while True:
        try:
            user_input = input(f"Document #{len(lista_documente)}: ")

            # Condiție de oprire
            if user_input.strip().upper() in ["STOP", "GATA"]:
                # Verificăm să avem măcar un document
                if not lista_documente:
                    print(" Lista e goală. Introdu măcar un document.")
                    continue
                break

            # Validare input gol
            if not user_input.strip():
                raise ValueError("Documentul nu poate fi gol.")

            lista_documente.append(user_input)

        except ValueError as e:
            print(f"⚠ {e}")

    # Etapa 2: Procesarea
    try:
        print("\n⚙️  Se generează indexul...")
        rezultat = inverted_index(lista_documente)

        # Etapa 3: Afișarea
        print("-" * 40)
        print(" Rezultat (Index Inversat):")
        # Afișăm frumos dicționarul
        for cuvant, indecsi in rezultat.items():
            print(f"   '{cuvant}': {indecsi}")
        print("-" * 40)

        # Bonus: Simulare Căutare
        while True:
            cautare = input("\nCaută un cuvânt (sau ENTER pentru a ieși): ").lower().strip()
            if not cautare:
                break

            if cautare in rezultat:
                print(f" Cuvântul '{cautare}' apare în documentele: {rezultat[cautare]}")
                # Afișăm și textul original pentru claritate
                for i in rezultat[cautare]:
                    print(f"    Doc {i}: \"{lista_documente[i]}\"")
            else:
                print(f" Cuvântul '{cautare}' nu apare în niciun document.")

    except Exception as e:
        print(f" A apărut o eroare neașteptată: {e}")



run_app()