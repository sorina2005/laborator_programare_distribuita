def grading_system():
    print("--- Sistem de Notare ---")

    try:
        # Pasul 1: Solicitam input de la utilizator
        input_utilizator = input("Introduceti scorul procentual (0-100): ")

        # Incercam sa convertim inputul in numar (float pentru a permite zecimale)
        scor = float(input_utilizator)

        # Pasul 2: Verificam daca numarul este in intervalul valid
        if scor < 0 or scor > 100:
            print("Eroare: Scorul trebuie sa fie intre 0 si 100.")
            return  # Opreste functia aici daca numarul nu e valid

        # Pasul 3: Determinam nota pe baza criteriilor
        nota = ""
        if scor >= 90:
            nota = "A"
        elif scor >= 80:
            nota = "B"
        elif scor >= 70:
            nota = "C"
        elif scor >= 60:
            nota = "D"
        else:
            nota = "F"

        # Pasul 4: Afisam rezultatul
        print(f"Pentru scorul {scor}, nota este: {nota}")

    except ValueError:
        # Pasul 5: Tratarea erorii daca utilizatorul introduce text in loc de numar
        print("Eroare: Va rugam sa introduceti un numar valid (fara litere sau simboluri).")


while True:
    grading_system()
    if input("Vrei sa continui? (n for no, anything for yes): ") == "n":
        break
