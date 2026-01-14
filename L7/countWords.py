import os


def count_words_in_file(file_path):
    """
    Citeste un fisier si returneaza numarul total de cuvinte.
    Returneaza -1 sau 0 daca fisierul nu este gasit, in functie de preferinta.
    """
    try:
        # Folosim 'with open' pentru a ne asigura ca fisierul se inchide corect
        # encoding='utf-8' este recomandat pentru a citi corect caracterele speciale
        with open(file_path, 'r') as f:
            text = f.read()

            # split() imparte textul la orice spatiu alb (spatiu, tab, linie noua)
            cuvinte = text.split()

            # Returnam lungimea listei de cuvinte
            return len(cuvinte)

    except FileNotFoundError:
        print(f"Eroare: Fisierul '{file_path}' nu a fost gasit.")
        return 0


# --- Exemplu de utilizare ---

# 1. Cream un fisier temporar pentru test (ca sa avem ce citi)
nume_fisier = "text_files/example.txt"
continut_test = "Salut tuturor. Aceasta este o demonstratie de lucru cu fisiere."

with open(nume_fisier, "w") as f:
    f.write(continut_test)

# 2. Apelam functia noastra
numar_cuvinte = count_words_in_file(nume_fisier)

print(f"Continut fisier: '{continut_test}'")
print(f"Numar cuvinte gasite: {numar_cuvinte}")

# Nota: Pentru textul dat in exemplu, rezultatul corect tehnic este 10 cuvinte,
# deoarece split() separa la spatii.