def factorial(n):
    """
    Calculează factorialul unui număr întreg nenegativ n.
    Returnează -1 dacă numărul este negativ (eroare).
    """
    if n < 0:
        return None  # Factorialul nu este definit pentru numere negative

    if n == 0 or n == 1:
        return 1

    rezultat = 1
    for i in range(2, n + 1):
        rezultat *= i  # Echivalent cu rezultat = rezultat * i

    return rezultat

while True:
    try:
        # Citirea datelor de la tastatură
            input_utilizator = input("Introduceți un număr întreg pentru a calcula factorialul: ")
            numar = int(input_utilizator)

        # Apelarea funcției
            valoare_factorial = factorial(numar)

        # Afișarea rezultatului
            if valoare_factorial is None:
                print("Eroare: Factorialul nu este definit pentru numere negative.")
            else:
                print(f"Factorialul numărului {numar} este: {valoare_factorial}")


    except ValueError:
        print("Eroare: Vă rugăm să introduceți un număr întreg valid (nu litere sau zecimale).")
    if input("Vrei sa continui? (n for no, anything for yes): ") == "n":
        break