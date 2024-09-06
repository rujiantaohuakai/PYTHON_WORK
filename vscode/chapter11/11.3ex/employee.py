class Employee:
    def __init__(self, first_name, last_name, salary = 5000):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, amount=5000):
        self.salary += amount
    
    def get_salary(self):
        return self.salary
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
