def reverse_words(sentence):
    """
    Inverseaza ordinea cuvintelor dintr-o propozitie si elimina spatiile inutile.
    """
    # 1. split() fara argumente imparte sirul la spatii albe
    # si elimina automat spatiile multiple, cele de la inceput si de la final.
    cuvinte = sentence.split()

    # 2. [::-1] creeaza o copie inversata a listei de cuvinte.
    cuvinte_inversate = cuvinte[::-1]

    # 3. join() uneste cuvintele folosind un singur spatiu intre ele.
    rezultat = " ".join(cuvinte_inversate)

    return rezultat


# --- Exemplu de utilizare ---
text_intrare = "soricel un cu joaca se pisica"
text_iesire = reverse_words(text_intrare)

print(f"Input:  '{text_intrare}'")
print(f"Output: '{text_iesire}'")

# Test cu spatii suplimentare
text_spatii = "  hello     world  "
print(f"Test spatii: '{reverse_words(text_spatii)}'")  # Va afisa 'world hello'