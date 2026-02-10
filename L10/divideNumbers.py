def calculeaza_suma_fisier(nume_fisier):
    suma_totala = 0
    try:
        # deschid fisierul pentru citire in modul text
        with open(nume_fisier, 'r') as fisier:
            # parcurg fiecare linie din fisier
            for linie in fisier:
                try:
                    # elimin spatiile inutile si convertesc la tipul float
                    valoare = float(linie.strip())
                    suma_totala += valoare
                except ValueError:
                    # ignor liniile care nu contin valori numerice valide
                    print(f"avertisment: s-a omis o linie nevalida: {linie.strip()}")

        return suma_totala

    except FileNotFoundError:
        # gestionez cazul in care fisierul nu este gasit la calea specificata
        print(f"eroare: fisierul '{nume_fisier}' nu a fost gasit.")
        return None
    except IOError:
        # tratez eventualele erori de intrare/iesire la citirea fisierului
        print("eroare: a aparut o problema la citirea fluxului de date.")
        return None
    except Exception as e:
        # prind orice alta exceptie pentru a asigura stabilitatea executiei
        print(f"eroare neasteptata: {e}")
        return None


# apelarea functiei pentru testare
rezultat = calculeaza_suma_fisier("date_input.txt")
if rezultat is not None:
    print(f"suma totala a numerelor din fisier este: {rezultat}")