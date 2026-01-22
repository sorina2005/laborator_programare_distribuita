import math

# 1. Definirea datelor de intrare
num = 25
angle = 30

# 2. Calcule matematice
# Rădăcina pătrată
radacina = math.sqrt(num)

# Factorialul (calculat pentru numărul întreg)
factorial = math.factorial(num)

# Sinusul
# ATENȚIE: Calculatoarele lucrează în radiani.
# Trebuie să convertim 30 de grade în radiani înainte de a aplica sinus.
sinus = math.sin(math.radians(angle))

# 3. Afișarea rezultatelor (Output)
print(f"Rădăcina pătrată a {num} este {radacina}")
print(f"Factorialul lui {num} este {factorial}")

# Notă: Folosim :.1f pentru a formata sinusul la o zecimală (0.5),
# deoarece calculele în virgulă mobilă pot returna uneori 0.4999999...
print(f"Sinusul unghiului de {angle} grade este {sinus:.1f}")