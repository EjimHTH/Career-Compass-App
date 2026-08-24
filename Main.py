from full_time_job import FullTimeJob
from contract_job import ContractJob
from career_compass import CareerCompass


career_compass = CareerCompass()


application1 = FullTimeJob(
    "Kalos Health",
    "Performance Analyst",
    120_000,
    "Applied",
    "LinkedIn",
    "Yes"
)


application2 = FullTimeJob(
    "Instituto Familiar de la Raza, Inc.",
    "Program Manager - RTP Initiative",
    80_000,
    "Interviewing",
    "Indeed",
    "Yes"
)


application3 = FullTimeJob(
    "Schools, Mentoring, And Resource Team, Inc (SMART, INC)",
    "Volunteer Program Manager",
    83_000,
    "Interviewing",
    "Organization Website",
    "Yes"
)


application4 = ContractJob(
    "State Job",
    "Analyst 2",
    70_000,
    "Applied",
    "Government Website",
    12
)


application5 = FullTimeJob(
    "ELF",
    "Sales Analyst",
    70_000,
    "Applied",
    "LinkedIn",
    "Yes"
)


career_compass.add_application(application1)
career_compass.add_application(application2)
career_compass.add_application(application3)
career_compass.add_application(application4)
career_compass.add_application(application5)


career_compass.menu()
