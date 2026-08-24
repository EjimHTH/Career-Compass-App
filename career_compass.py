from full_time_job import FullTimeJob
from contract_job import ContractJob


class CareerCompass:
    def __init__(self):
        self.applications = []

    def add_application(self, application):
        self.applications.append(application)

    def display_applications(self):
        if len(self.applications) == 0:
            print("There are no job applications yet.")
        else:
            for application in self.applications:
                application.display_application()
                print()

    def calculate_total_salary(self):
        total = 0

        for application in self.applications:
            total += application.salary

        print(f"Total target salary: ${total:,.0f}")

    def create_application(self):
        print("\n--- Add New Job Application ---")

        company = input("Company: ")
        position = input("Position: ")

        try:
            salary = float(input("Salary: "))
        except ValueError:
            print("Please enter a valid number for the salary.")
            return

        status = input("Status: ")

        print("\nWhat type of job is this?")
        print("1. Full-Time")
        print("2. Contract")

        job_type = input("Enter your choice: ")

        if job_type == "1":
            benefits = input("Does this job have benefits? (Yes/No): ")

            application = FullTimeJob(
                company,
                position,
                salary,
                status,
                benefits
            )

        elif job_type == "2":
            try:
                contract_length = int(
                    input("Contract length in months: ")
                )
            except ValueError:
                print("Please enter a valid number of months.")
                return

            application = ContractJob(
                company,
                position,
                salary,
                status,
                contract_length
            )

        else:
            print("Invalid job type.")
            return

        self.applications.append(application)

        print("\nApplication added successfully!")

    def menu(self):
        while True:
            print("\n==============================")
            print("       CAREER COMPASS")
            print("==============================")
            print("1. View Applications")
            print("2. Add Application")
            print("3. Calculate Total Salary")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_applications()

            elif choice == "2":
                self.create_application()

            elif choice == "3":
                self.calculate_total_salary()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")