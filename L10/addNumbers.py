def imparte_numere(a, b):
    try:
        # calculez raportul dintre cele doua numere
        rezultat = a / b
        return rezultat
    except ZeroDivisionError:
        # tratez cazul de nedeterminare la impartirea cu zero
        print("eroare: operatia nu este permisa deoarece numitorul este zero.")
        return None
    except TypeError:
        # verific daca argumentele sunt de tip numeric
        print("eroare: datele de intrare trebuie sa fie de tip int sau float.")
        return None
    except Exception as e:
        # gestionez alte potentiale erori neprevazute pentru siguranta
        print(f"eroare neasteptata: {e}")
        return None

# exemple pentru verificarea functionalitatii
print(imparte_numere(20, 4))
print(imparte_numere(20, 0))
print(imparte_numere(20, "x"))