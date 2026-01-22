class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Constructorul clasei. Se apelează automat la instanțiere.
        Inițializează atributul protejat _balance.
        """
        # Folosim underscore (_) pentru a semnala că acest atribut
        # este privat/protejat și nu ar trebui accesat direct din afara clasei.
        self._balance = initial_balance

    def deposit(self, amount):
        """Metoda pentru depunere."""
        if amount > 0:
            self._balance += amount
            print(f"✅ Ai depus {amount} RON. Sold nou: {self._balance} RON.")
        else:
            print("❌ Suma depusă trebuie să fie pozitivă.")

    def withdraw(self, amount):
        """Metoda pentru retragere."""
        if amount > self._balance:
            print(f"❌ Fonduri insuficiente! Ai doar {self._balance} RON.")
        elif amount <= 0:
            print("❌ Suma retrasă trebuie să fie pozitivă.")
        else:
            self._balance -= amount
            print(f"✅ Ai retras {amount} RON. Sold rămas: {self._balance} RON.")

    def get_balance(self):
        """Metoda getter pentru a vedea soldul."""
        return self._balance

# --- ZONA DE TESTARE (Instanțiere și Utilizare) ---

# 1. Instanțiere (Creăm un obiect nou 'cont_meu' cu 100 RON la start)
cont_meu = BankAccount(100)

# 2. Verificăm soldul inițial
print(f"Sold inițial: {cont_meu.get_balance()} RON")
print("-" * 30)

# 3. Facem o depunere (Adding functionality)
cont_meu.deposit(50)

# 4. Încercăm o retragere validă
cont_meu.withdraw(30)

# 5. Încercăm o retragere invalidă (fonduri insuficiente)
cont_meu.withdraw(500)

# 6. Încercăm o retragere cu sumă negativă
cont_meu.withdraw(-20)

print("-" * 30)
# 7. Verificăm soldul final
print(f"Sold final în cont: {cont_meu.get_balance()} RON")