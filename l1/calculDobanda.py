def main():
    print("--- Calculator de Dobândă Simplă ---")

    # 1. Preluăm datele de la utilizator (Input)
    principal = float(input("Introdu suma principală (Principal): "))
    rata = float(input("Introdu rata anuală a dobânzii (fără %, ex: 5): "))
    timp = float(input("Introdu perioada în ani (Time): "))

    # 2. Calculăm dobânda (Processing)
    # Folosim formula: (P * R * T) / 100
    dobanda = (principal * rata * timp) / 100

    # Calculăm și suma totală (Principal + Dobânda) pentru claritate
    total = principal + dobanda

    # 3. Afișăm rezultatul (Output)
    print("-" * 30)
    print(f"Suma Principală: {principal}")
    print(f"Dobânda calculată: {dobanda}")
    print(f"Total (Principal + Dobândă): {total}")

if __name__ == "__main__":
    main()