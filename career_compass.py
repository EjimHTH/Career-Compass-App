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

        application_source = input(
            "Where did you apply? (LinkedIn, Indeed, Company Website, etc.): "
        )

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
                application_source,
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
                application_source,
                contract_length
            )

        else:
            print("Invalid job type.")
            return

        self.applications.append(application)

        print("Application added successfully!")
        print(f"You now have {len(self.applications)} applications.")

    def update_status(self):
        if len(self.applications) == 0:
            print("There are no applications to update.")
            return

        print("\n--- Update Application Status ---")

        for index, application in enumerate(self.applications, start=1):
            print(
                f"{index}. "
                f"{application.company} - "
                f"{application.position}"
            )

        try:
            choice = int(input("\nSelect an application: "))

            if choice < 1 or choice > len(self.applications):
                print("Invalid application number.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

        application = self.applications[choice - 1]

        print(f"\nCurrent Status: {application.status}")

        print("\nChoose a new status:")
        print("1. Applied")
        print("2. Interviewing")
        print("3. Offer")
        print("4. Denied")

        new_status = input("Enter your choice: ")

        if new_status == "1":
            application.status = "Applied"

        elif new_status == "2":
            application.status = "Interviewing"

        elif new_status == "3":
            application.status = "Offer"

        elif new_status == "4":
            application.status = "Denied"

        else:
            print("Invalid status choice.")
            return

        print("Status updated successfully!")

    def menu(self):
        while True:
            print("\n==============================")
            print("       CAREER COMPASS")
            print("==============================")
            print("1. View Applications")
            print("2. Add Application")
            print("3. Update Application Status")
            print("4. Calculate Total Salary")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_applications()

            elif choice == "2":
                self.create_application()

            elif choice == "3":
                self.update_status()

            elif choice == "4":
                self.calculate_total_salary()

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose 1-5.")