# 1. Clasa de Bază (Părinte)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        """Returnează detaliile standard ale angajatului."""
        return f"Employee: {self.name}, Salary: {self.salary}"


# 2. Subclasa (Copil)
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Aici folosim super() pentru a apela constructorul părintelui (Employee)
        # Astfel, nu trebuie să rescriem logica pentru name și salary
        super().__init__(name, salary)

        # Adăugăm atributul specific managerului
        self.department = department

    def get_details(self):
        """
        Suprascrie (Override) metoda din părinte.
        Oferă o implementare diferită, specifică managerului.
        """
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


# --- ZONA DE TESTARE ---

# Instanțiem un angajat simplu
emp = Employee("John", 3000)

# Instanțiem un manager (care are și departament)
mgr = Manager("Alice", 5000, "IT")

# Apelăm metoda get_details() pentru ambele obiecte
print(emp.get_details())
print(mgr.get_details())