import math


def distance(x1, y1, x2, y2):
    """
    Calculează distanța euclidiană dintre două puncte:
    Punctul 1: (x1, y1)
    Punctul 2: (x2, y2)
    """
    # Calculăm diferențele pe axe
    delta_x = x2 - x1
    delta_y = y2 - y1

    # Aplicăm formula: radical din (delta_x^2 + delta_y^2)
    dist = math.sqrt(delta_x ** 2 + delta_y ** 2)

    return dist


while True:
    print("--- Calculator Distanță între Două Puncte ---")
    try:
        # Citirea coordonatelor pentru primul punct
        print("Introduceți coordonatele primului punct:")
        x1 = float(input("x1 = "))
        y1 = float(input("y1 = "))

        # Citirea coordonatelor pentru al doilea punct
        print("\nIntroduceți coordonatele celui de-al doilea punct:")
        x2 = float(input("x2 = "))
        y2 = float(input("y2 = "))

        # Apelarea funcției
        rezultat = distance(x1, y1, x2, y2)

        # Afișarea rezultatului (formatat cu 2 zecimale pentru claritate)
        print(f"\nDistanța dintre ({x1}, {y1}) și ({x2}, {y2}) este: {rezultat:.2f}")

    except ValueError:
        print("Eroare: Vă rugăm să introduceți numere valide (folosiți '.' pentru zecimale).")
    if input("Vrei sa continui? (n for no, anything for yes): ") == "n":
        break