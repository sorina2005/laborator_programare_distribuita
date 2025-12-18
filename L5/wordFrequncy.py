import string


def word_frequency(text):
    """
    Calculează frecvența cuvintelor dintr-un text, ignorând punctuația și majusculele.
    """
    # 1. Validare Tip de Date (Defensive Programming)
    if not isinstance(text, str):
        raise TypeError("Funcția așteaptă un șir de caractere (string).")

    # 2. Validare Conținut
    if not text.strip():
        raise ValueError("Textul introdus este gol sau conține doar spații.")

    # 3. Procesare Text
    # a. Transformare în litere mici
    text_curat = text.lower()

    # b. Eliminare punctuație
    # string.punctuation conține: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    # Metoda .translate() este cea mai rapidă metodă de a șterge caractere
    tabela_traducere = str.maketrans('', '', string.punctuation)
    text_curat = text_curat.translate(tabela_traducere)

    # c. Spargere în cuvinte (Tokenizare)
    # .split() fără argumente separă după orice spațiu alb (space, tab, newline)
    cuvinte = text_curat.split()

    # 4. Construire Dicționar de Frecvență
    frecventa = {}

    for cuvant in cuvinte:
        # Folosim .get() pentru a evita erorile dacă cheia nu există încă
        # Dacă cuvântul există, ia valoarea curentă + 1
        # Dacă nu există, ia 0 + 1
        frecventa[cuvant] = frecventa.get(cuvant, 0) + 1

    return frecventa


def citire_si_procesare():
    print("\n*** Analizator de Frecvență a Cuvintelor ***")
    print("Scrie o frază pentru a număra cuvinte (sau 'exit' pentru a ieși).")

    while True:
        try:
            # Citirea inputului
            user_input = input("\nIntrodu textul: ")

            # Condiție de ieșire manuală
            if user_input.lower() == 'exit':
                print("La revedere!")
                break

            # Apelarea funcției
            rezultat = word_frequency(user_input)

            # Afișare frumoasă a rezultatului
            print("-" * 40)
            print(f" Rezultat (Dicționar):")
            print(rezultat)

            # Opțional: Afișare detaliată
            print("\nDetaliat:")
            for cuvant, count in rezultat.items():
                print(f"   • '{cuvant}': {count}")
            print("-" * 40)

            # Putem pune break aici dacă vrem să rulăm o singură dată,
            # sau îl lăsăm să ruleze la infinit. Voi pune break pentru a respecta
            # stilul problemelor anterioare de "run once or retry on error".
            break

        except (ValueError, TypeError) as e:
            print("-" * 40)
            print(f" Eroare: {e}")
            print("Te rog introdu un text valid care conține cuvinte.")
            print("-" * 40)
            # Bucla continuă, cerând din nou input


# Rularea programului
citire_si_procesare()