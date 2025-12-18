def unique_pair_sum(numbers, target):
    """
    Găsește perechi unice de numere care însumate dau ținta.
    Returnează un set de tupluri (a, b) unde a <= b.
    Complexitate: O(n) - Parcurgem lista o singură dată.
    """

    # 1. Validări Defensive
    if not isinstance(numbers, list):
        raise TypeError("Inputul 'numbers' trebuie să fie o listă.")
    if not isinstance(target, (int, float)):
        raise TypeError("Ținta trebuie să fie un număr.")

    seen = set()  # Set pentru numerele vizitate deja
    pairs = set()  # Set pentru rezultate (asigură unicitatea perechilor)

    for num in numbers:
        # Validăm că elementele din listă sunt numere
        if not isinstance(num, int):
            raise ValueError(f"Elementul '{num}' din listă nu este un număr întreg.")

        complement = target - num

        # Logica: Dacă complementul (ceea ce ne lipsește) a fost văzut deja,
        # înseamnă că am găsit o pereche validă.
        if complement in seen:
            # Sortăm perechea pentru a respecta regula a <= b
            # min(a,b), max(a,b) asigură ordinea corectă
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)

        # Adăugăm numărul curent în set-ul de 'văzute' pentru iterțiile viitoare
        seen.add(num)

    return pairs


def run_program():
    print("\n*** Găsire Perechi cu Sumă Țintă ***")

    while True:
        try:
            # 1. Citire și procesare listă
            input_str = input("\nIntrodu lista de numere (separate prin virgulă): ")

            if not input_str.strip():
                raise ValueError("Lista nu poate fi goală.")

            # Convertim string-ul în listă de int-uri
            lista_numere = []
            for x in input_str.split(','):
                x_clean = x.strip()
                if x_clean:  # ignorăm elemente goale
                    lista_numere.append(int(x_clean))

            if not lista_numere:
                raise ValueError("Nu au fost introduse numere valide.")

            # 2. Citire țintă
            target_str = input("Introdu valoarea țintă (target): ")
            target = int(target_str)

            # 3. Apelare funcție
            rezultat = unique_pair_sum(lista_numere, target)

            # 4. Afișare
            print("-" * 40)
            if rezultat:
                print(f" Perechi găsite (Sum = {target}):")
                print(rezultat)
                # Afișare mai prietenoasă
                sorted_res = sorted(list(rezultat))  # Sortăm doar pentru afișare
                print(f"   Detaliat: {', '.join(str(p) for p in sorted_res)}")
            else:
                print(f"⚠️ Nicio pereche nu sumează la {target}.")
            print("-" * 40)

            break  # Ieșim după succes

        except ValueError as e:
            print("-" * 40)
            if "invalid literal for int()" in str(e):
                print(" Eroare: Te rog introdu doar numere întregi.")
            else:
                print(f" Eroare: {e}")
            print("Încearcă din nou.")
            print("-" * 40)
        except Exception as e:
            print(f" Eroare neașteptată: {e}")


# Rularea programului

run_program()