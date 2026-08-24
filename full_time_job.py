from job_application import JobApplication


class FullTimeJob(JobApplication):
    def __init__(
        self,
        company,
        position,
        salary,
        status,
        application_source,
        benefits
    ):
        super().__init__(
            company,
            position,
            salary,
            status,
            application_source
        )

        self.benefits = benefits

    def display_application(self):
        print(f"{self.company} - {self.position}")
        print(f"Salary: ${self.salary:,.0f}")
        print(f"Status: {self.status}")
        print(f"Applied Through: {self.application_source}")
        print(f"Benefits: {self.benefits}")