import random

def number_guessing():
    print("--- Joc: Ghiceste Numarul ---")
    print("Am ales un numar intre 1 si 20.")
    print("Ai 5 incercari sa il ghicesti.")

    # Pasul 1: Generam numarul secret
    # randint(1, 20) include ambele capete (1 si 20)
    numar_secret = random.randint(1, 20)
    incercari_ramase = 5

    # Pasul 2: Bucla jocului
    # Jocul ruleaza atata timp cat mai avem incercari
    while incercari_ramase > 0:
        print(f"\nIncercari ramase: {incercari_ramase}")

        try:
            # Pasul 3: Citirea inputului
            input_utilizator = input("Introdu numarul tau: ")
            ghicitoare = int(input_utilizator)

            # Validare suplimentara: Numarul trebuie sa fie intre 1 si 20
            if ghicitoare < 1 or ghicitoare > 20:
                print("Te rog alege un numar strict intre 1 si 20.")
                # Folosim 'continue' pentru a sari peste restul codului si a cere din nou
                # fara sa scadem o viata
                continue

            # Pasul 4: Verificarea raspunsului
            if ghicitoare == numar_secret:
                print(f"FELICITARI! Ai ghicit! Numarul era {numar_secret}.")
                return  # 'return' opreste functia imediat (iese din joc)

            elif ghicitoare < numar_secret:
                print("Prea mic!")
            else:
                print("Prea mare!")

            # Scadem o viata doar daca a fost un numar valid, dar gresit
            incercari_ramase -= 1

        except ValueError:
            # Pasul 5: Tratarea erorii de input non-numeric
            print("Eroare: Te rog introdu un numar intreg, nu litere.")
            # Nota: Aici nu scadem 'incercari_ramase', oferind o a doua sansa pentru typo-uri

    # Pasul 6: Finalul jocului (daca bucla s-a terminat fara succes)
    print("--------------------------------")
    print(f"Ai ramas fara incercari. Numarul secret era: {numar_secret}")
    print("Mai incearca o data!")


number_guessing()