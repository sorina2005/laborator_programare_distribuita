# # main.py
# import math_operations  # Importăm fișierul creat anterior (fără extensia .py)
#
# # Definim numerele pentru test
# x = 10
# y = 5
#
# # Apelăm funcțiile din modul folosind sintaxa: nume_modul.nume_functie()
# suma = math_operations.adunare(x, y)
# diferenta = math_operations.scadere(x, y)
# produs = math_operations.inmultire(x, y)
# cat = math_operations.impartire(x, y)
#
# # Afișăm rezultatele
# print(f"Numerele sunt: {x} și {y}")
# print("-" * 30)
# print(f"Adunare: {suma}")
# print(f"Scădere: {diferenta}")
# print(f"Înmulțire: {produs}")
# print(f"Împărțire: {cat}")
#
# # Testăm și cazul special (împărțirea la zero)
# print(f"Test împărțire la 0: {math_operations.impartire(10, 0)}


# main.py

# Importăm modulele specifice din pachetul geometry
from geometry import circle, rectangle

# --- Testare Cerc ---
raza = 5
aria_c = circle.circle_area(raza)
circ_c = circle.circle_circumference(raza)

print(f"CERC (raza = {raza}):")
print(f"  - Aria: {aria_c:.2f}")
print(f"  - Circumferința: {circ_c:.2f}")
print("-" * 30)

# --- Testare Dreptunghi ---
L = 10
l = 4
aria_d = rectangle.rect_area(L, l)
perim_d = rectangle.rect_perimeter(L, l)

print(f"DREPTUNGHI (L = {L}, l = {l}):")
print(f"  - Aria: {aria_d}")
print(f"  - Perimetrul: {perim_d}")