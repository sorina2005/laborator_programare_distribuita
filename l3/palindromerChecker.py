def is_palindrome(word):
    # Convertim la string pentru a acoperi cazul numerelor si la litere mici pentru a ignora capitalizarea
    # Astfel 'Ana' sau '121' vor fi procesate corect
    word_str = str(word).lower()

    # Returnam True daca cuvantul este egal cu inversul sau, altfel False
    return word_str == word_str[::-1]


while True:
    # Preluam cuvantul de la tastatura
    cuvant_citit = input("Introduceti un cuvant pentru verificare: ")

    # Verificam folosind functia definita
    rezultat = is_palindrome(cuvant_citit)

    # Afisam rezultatul
    if rezultat == True:
        print("Cuvantul este palindrom.")
    else:
        print("Cuvantul nu este palindrom.")
    if input("Vrei sa continui? (n for no, anything for yes): ") == "n":
        break