import math


def main():
    print("--- Verificare Număr Prim ---")

    # 1. Input: Citim numărul de la tastatură
    # Folosim int() pentru că avem nevoie de un număr întreg
    numar = int(input("Introdu un număr întreg: "))

    # 2. Procesare: Verificăm dacă este prim
    # Presupunem inițial că numărul ESTE prim (este_prim = True)
    # și încercăm să demonstrăm contrariul.
    este_prim = True

    if numar < 2:
        # Numerele mai mici ca 2 (0, 1, negative) nu sunt prime
        este_prim = False
    else:
        # Verificăm dacă numărul se împarte la altceva între 2 și radical din număr
        # (Optimizare: nu e nevoie să verificăm până la numărul însuși)
        limita = int(math.sqrt(numar)) + 1

        for i in range(2, limita):
            if numar % i == 0:
                # Dacă am găsit un divizor, înseamnă că NU e prim
                este_prim = False
                break  # Oprim bucla, nu are rost să mai căutăm

    # 3. Output: Afișăm rezultatul pe baza "steagului" este_prim
    if este_prim:
        print(f"Numărul {numar} ESTE prim.")
    else:
        print(f"Numărul {numar} NU este prim.")


if __name__ == "__main__":
    main()