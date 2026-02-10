def gestioneaza_inventar():
    # initializez inventarul ca un dictionar gol
    inventar = {}

    while True:
        print("\n--- meniu inventar ---")
        print("1. adauga/actualizeaza produs")
        print("2. cauta produs")
        print("3. iesire")

        optiune = input("alege o optiune: ").strip()

        if optiune == "1":
            try:
                # citesc numele si cantitatea de la utilizator
                nume = input("introdu numele produsului: ").strip().lower()
                if not nume:
                    raise ValueError("numele produsului nu poate fi vid.")

                cantitate = int(input("introdu cantitatea: "))
                if cantitate < 0:
                    raise ValueError("cantitatea nu poate fi negativa.")

                # adaug sau actualizez valoarea in dictionar
                inventar[nume] = cantitate
                print(f"produsul '{nume}' a fost actualizat cu succes.")

            except ValueError as e:
                # gestionez erorile de conversie sau validarile custom
                print(f"eroare de intrare: {e}")
            except Exception as e:
                # captez orice alta eroare neprevazuta
                print(f"a aparut o eroare neasteptata: {e}")

        elif optiune == "2":
            try:
                nume = input("introdu numele produsului cautat: ").strip().lower()
                # verific daca produsul exista in structura de date
                if nume in inventar:
                    print(f"produs: {nume} | cantitate: {inventar[nume]}")
                else:
                    # generez o eroare daca produsul lipseste
                    raise KeyError(f"produsul '{nume}' nu exista in inventar.")

            except KeyError as e:
                # gestionez cazul in care cheia nu este gasita
                print(f"eroare de cautare: {e}")
            except Exception as e:
                print(f"eroare neasteptata: {e}")

        elif optiune == "3":
            print("iesire din program...")
            break
        else:
            print("optiune invalida, incearca din nou.")


# pornesc executia programului
if __name__ == "__main__":
    gestioneaza_inventar()