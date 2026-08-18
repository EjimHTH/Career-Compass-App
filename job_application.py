class JobApplication:
    def __init__(self, company, position, salary, status):
        self.company = company
        self.position = position
        self.salary = salary
        self.status = status

    def display_application(self):
        print(f"{self.company} - {self.position}")
        print(f"Salary: ${self.salary}")
        print(f"Status: {self.status}")