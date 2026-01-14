def run_length_encoding(text):
    """
    Implementeaza codificarea RLE (Run-Length Encoding).
    Returneaza o versiune comprimata a sirului.
    """
    # Daca sirul este gol, returnam un sir gol
    if not text:
        return ""

    # Folosim o lista pentru a construi rezultatul (mai eficient decat string concatenation)
    result = []

    # Initializam contorul pentru primul caracter
    count = 1

    # Parcurgem sirul incepand de la al doilea caracter
    for i in range(1, len(text)):
        # Comparam caracterul curent cu cel anterior
        if text[i] == text[i - 1]:
            count += 1
        else:
            # Daca caracterul s-a schimbat, adaugam grupul anterior in lista
            result.append(text[i - 1] + str(count))
            # Resetam contorul pentru noul caracter
            count = 1

    # Important: Adaugam ultimul grup de caractere (care nu a fost prins in bucla)
    result.append(text[-1] + str(count))

    # unim elementele listei intr-un singur sir
    return "".join(result)


# --- Exemplu de utilizare ---
text_test = "aaabbbbcccdde"
output = run_length_encoding(text_test)

print(f"Input:  '{text_test}'")
print(f"Output: '{output}'")

# Test pentru cazuri particulare (sir gol sau caractere unice)
text_simplu = "abc"
print(f"Input:  '{text_simplu}' -> Output: '{run_length_encoding(text_simplu)}'")