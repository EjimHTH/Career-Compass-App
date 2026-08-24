from job_application import JobApplication


class FullTimeJob(JobApplication):
    def __init__(self, company, position, salary, status, benefits):
        super().__init__(company, position, salary, status)
        self.benefits = benefits

    def display_application(self):
        print(f"{self.company} - {self.position}")
        print(f"Salary: ${self.salary:,}")
        print(f"Status: {self.status}")
        print(f"Benefits: {self.benefits}")