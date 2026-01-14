def filter_lines(input_path, output_path, keyword):
    """
    Citeste un fisier si scrie intr-un fisier nou doar liniile care contin
    cuvantul cheie specificat.
    """
    try:

        with open(input_path, 'r') as f_in, \
                open(output_path, 'w') as f_out:

            lines_found = 0

            for line in f_in:
                # Verificam daca keyword-ul se afla in linia curenta
                if keyword in line:
                    f_out.write(line)
                    lines_found += 1

            print(f"Am gasit si salvat {lines_found} linii care contin '{keyword}'.")

    except FileNotFoundError:
        print(f"Eroare: Fisierul '{input_path}' nu a fost gasit.")
    except Exception as e:
        print(f"Eroare neasteptata: {e}")


# --- Exemplu de utilizare ---

# 1. Definirea numelor de fisiere
fisier_intrare = "input.txt"
fisier_iesire = "filtered.txt"
cuvant_cautat = "Python"

# 2. Crearea fisierului de intrare cu textul din exemplu
continut = """Python este un limbaj versatil.
Java este popular în dezvoltarea enterprise.
Python este folosit în știința datelor.
Python este ușor de învățat."""

with open(fisier_intrare, "w") as f:
    f.write(continut)

# 3. Apelarea functiei de filtrare
filter_lines(fisier_intrare, fisier_iesire, cuvant_cautat)

# 4. Verificarea rezultatului
print("\n--- Continut Filtered ---")
with open(fisier_iesire, "r") as f:
    print(f.read())