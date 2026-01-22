# math_operations.py

def adunare(a, b):
    """Returnează suma a două numere."""
    return a + b

def scadere(a, b):
    """Returnează diferența dintre a și b."""
    return a - b

def inmultire(a, b):
    """Returnează produsul a două numere."""
    return a * b

def impartire(a, b):
    """
    Returnează rezultatul împărțirii lui a la b.
    Returnează un mesaj de eroare dacă b este 0.
    """
    if b == 0:
        return "Eroare: Împărțirea la zero nu este permisă."
    return a / b