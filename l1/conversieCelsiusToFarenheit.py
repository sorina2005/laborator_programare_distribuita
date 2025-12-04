# 1. Cerem input de la utilizator
# Folosim float() pentru a permite numere cu zecimale (ex: 36.6)
celsius = float(input("Introdu temperatura în grade Celsius: "))

# 2. Calculam conversia
# Putem scrie 9/5 sau direct 1.8
fahrenheit = (celsius * 9/5) + 32

# 3. Afisam rezultatul
print(f"{celsius} grade Celsius înseamnă {fahrenheit} grade Fahrenheit.")