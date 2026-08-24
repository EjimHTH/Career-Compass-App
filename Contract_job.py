from job_application import JobApplication


class ContractJob(JobApplication):
    def __init__(
        self,
        company,
        position,
        salary,
        status,
        application_source,
        contract_length
    ):
        super().__init__(
            company,
            position,
            salary,
            status,
            application_source
        )

        self.contract_length = contract_length

    def display_application(self):
        print(f"{self.company} - {self.position}")
        print(f"Salary: ${self.salary:,.0f}")
        print(f"Status: {self.status}")
        print(f"Applied Through: {self.application_source}")
        print(f"Contract Length: {self.contract_length} months")