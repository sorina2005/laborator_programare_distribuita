def reverse_lines(input_path, output_path):
    """
    Citeste un fisier linie cu linie si scrie inversul fiecarei linii
    intr-un fisier nou.
    """
    try:
        # Deschidem fisierul de intrare (r - read) si cel de iesire (w - write)
        # Folosim encoding='utf-8' pentru a suporta caractere romanesti
        with open(input_path, 'r') as f_in, \
                open(output_path, 'w') as f_out:

            for line in f_in:
                # 1. Eliminam caracterul de linie noua (\n) de la finalul randului
                # Daca nu facem asta, '\n' ajunge la inceputul randului dupa inversare
                clean_line = line.rstrip('\n')

                # 2. Inversam linia curata
                reversed_line = clean_line[::-1]

                # 3. Scriem linia inversata in noul fisier si adaugam '\n' la loc
                f_out.write(reversed_line + '\n')

        print("Operatiunea s-a incheiat cu succes.")

    except FileNotFoundError:
        print(f"Eroare: Fisierul '{input_path}' nu a fost gasit.")
    except Exception as e:
        print(f"A aparut o eroare neasteptata: {e}")


# --- Exemplu de utilizare ---

# 1. Cream fisierul de intrare pentru test
input_file = "text_files/input.txt"
output_file = "text_files/output.txt"

continut_initial = """Python este grozav.
Îmi place să lucrez cu fișiere."""

with open(input_file, "w") as f:
    f.write(continut_initial)

# 2. Apelam functia
reverse_lines(input_file, output_file)

# 3. Verificam rezultatul citind fisierul creat
print("\n--- Continut Output ---")
with open(output_file, "r") as f:
    print(f.read())