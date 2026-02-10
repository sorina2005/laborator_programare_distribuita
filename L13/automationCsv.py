import csv
import os


def proceseaza_comenzi(fisier_intrare, fisier_iesire):
    try:
        # verific daca fisierul de intrare exista inainte de a incepe
        if not os.path.exists(fisier_intrare):
            print(f"eroare: fisierul '{fisier_intrare}' nu a fost gasit.")
            return

        comenzi_procesate = []

        # deschid fisierul sursa pentru citire
        with open(fisier_intrare, mode='r', encoding='utf-8') as f_in:
            cititor = csv.DictReader(f_in)

            # parcurg fiecare rand pentru a calcula valoarea totala
            for rand in cititor:
                try:
                    produs = rand['Produs']
                    cantitate = float(rand['Cantitate'])
                    pret_unitar = float(rand['Pret unitar'])

                    # calculez valoarea totala a comenzii
                    valoare_totala = cantitate * pret_unitar

                    # adaug rezultatul intr-o lista pentru salvarea ulterioara
                    comenzi_procesate.append({
                        'Produs': produs,
                        'Cantitate': cantitate,
                        'Pret unitar': pret_unitar,
                        'Valoare Totala': valoare_totala
                    })
                except ValueError:
                    # gestionez cazurile in care datele nu sunt numerice
                    print(f"avertisment: date invalide pe randul pentru produsul {rand.get('Produs')}")
                except KeyError as e:
                    # gestionez lipsa unei coloane specifice in header-ul csv
                    print(f"eroare: coloana {e} lipseste din fisierul de intrare.")
                    return

        # deschid fisierul destinatie pentru a scrie rezultatele finale
        campuri = ['Produs', 'Cantitate', 'Pret unitar', 'Valoare Totala']
        with open(fisier_iesire, mode='w', encoding='utf-8', newline='') as f_out:
            scriitor = csv.DictWriter(f_out, fieldnames=campuri)

            # scriu capul de tabel si datele calculate
            scriitor.writeheader()
            scriitor.writerows(comenzi_procesate)

        print(f"succes: procesarea a fost finalizata. rezultatele sunt in '{fisier_iesire}'.")

    except IOError:
        # gestionez erorile de sistem la deschiderea sau scrierea fisierelor
        print("eroare: a aparut o problema la accesarea fisierelor pe disc.")
    except Exception as e:
        # captez orice alta exceptie neprevazuta
        print(f"a aparut o eroare neasteptata: {e}")


# functia de test pentru a genera un fisier csv de proba si a-l procesa
if __name__ == "__main__":
    # rulez procesarea automata
    proceseaza_comenzi("exemplu.csv", "rezultate_comenzi.csv")