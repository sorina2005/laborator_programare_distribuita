def main():
    print("--- Calculator de Dobanda simpla ---")

    # 1. Preluăm datele de la utilizator (Input)
    principal = float(input("Introdu suma principala (Principal): "))
    rata = float(input("Introdu rata anuală a dobanzii (fara %, ex: 5): "))
    timp = float(input("Introdu perioada in ani (Time): "))

    # 2. Calculăm dobânda (Processing)
    # Folosim formula: (P * R * T) / 100
    dobanda = (principal * rata * timp) / 100

    # Calculăm și suma totală (Principal + Dobânda) pentru claritate
    total = principal + dobanda

    # 3. Afișăm rezultatul (Output)
    print("-" * 30)
    print(f"Suma Principala: {principal}")
    print(f"Dobanda calculată: {dobanda}")
    print(f"Total (Principal + Dobanda): {total}")

if __name__ == "__main__":
    main()


    