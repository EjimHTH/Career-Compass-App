class JobApplication:
    def __init__(self, company, position, salary, status, application_source):
        self.company = company
        self.position = position
        self.salary = salary
        self.status = status
        self.application_source = application_source

    def set_salary(self, salary):
        if salary >= 0:
            self.salary = salary
        else:
            print("Salary cannot be negative.")

    def display_application(self):
        print(f"{self.company} - {self.position}")
        print(f"Salary: ${self.salary:,.0f}")
        print(f"Status: {self.status}")
        print(f"Applied Through: {self.application_source}")