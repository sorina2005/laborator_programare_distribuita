def is_palindrome(text):
    """
    Verifica daca un text este palindrom, ignorand literele mari si spatiile.
    Functioneaza pentru siruri standard ASCII.
    """
    # 1. Transforma textul in litere mici (lowercase)
    text_lower = text.lower()

    # 2. Elimina spatiile
    text_clean = text_lower.replace(" ", "")

    # 3. Verifica daca textul curat este egal cu inversul sau
    return text_clean == text_clean[::-1]


# --- Exemplu de utilizare ---
text_test = "A man a plan a canal Panama"
rezultat = is_palindrome(text_test)

print(f"Text: '{text_test}'")
print(f"Este palindrom? {rezultat}")

# Test negativ
text_negativ = "Hello World"
print(f"Text: '{text_negativ}' -> {is_palindrome(text_negativ)}")