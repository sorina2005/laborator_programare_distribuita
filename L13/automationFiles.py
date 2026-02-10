import os


def redenumeste_fisiere(cale_director):
    try:
        # verific daca directorul specificat exista intr-adevar
        if not os.path.exists(cale_director):
            print(f"eroare: directorul '{cale_director}' nu exista.")
            return

        # obtin lista cu toate elementele din director
        elemente = os.listdir(cale_director)

        # contor pentru a tine evidenta fisierelor modificate
        fisiere_redenumite = 0

        for nume_original in elemente:
            # construiesc calea completa pentru elementul curent
            cale_veche = os.path.join(cale_director, nume_original)

            # verific sa fie fisier, nu folder, pentru a evita erori de sistem
            if os.path.isfile(cale_veche):
                # creez noul nume adaugand prefixul cerut
                nume_nou = "renamed_" + nume_original
                cale_noua = os.path.join(cale_director, nume_nou)

                try:
                    # execut operatia de redenumire
                    os.rename(cale_veche, cale_noua)
                    print(f"succes: {nume_original} -> {nume_nou}")
                    fisiere_redenumite += 1
                except OSError as e:
                    # gestionez erorile de permisiuni sau fisiere blocate
                    print(f"eroare la redenumirea fisierului {nume_original}: {e}")

        print(f"\noperatiune finalizata. au fost redenumite {fisiere_redenumite} fisiere.")

    except PermissionError:
        # gestionez cazul in care scriptul nu are drepturi de scriere in folder
        print("eroare: nu ai permisiuni suficiente pentru a modifica acest director.")
    except Exception as e:
        # captez orice alta exceptie neprevazuta pentru siguranta
        print(f"a aparut o eroare neasteptata: {e}")


# exemplul de utilizare
if __name__ == "__main__":
    # poti inlocui punct-ul cu o cale specifica, de exemplu 'C:/fisiere_test'
    cale_target = "."
    print(f"incep redenumirea in directorul: {os.path.abspath(cale_target)}")
    redenumeste_fisiere(cale_target)