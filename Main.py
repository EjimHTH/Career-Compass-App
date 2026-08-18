from job_application import JobApplication

application1 = JobApplication(
    "Kalos Health",
    "Performance Analyst",
   120,000,
    "Applied"
)

application2 = JobApplication(
    "Instituto Familiar de la Raza, Inc.",
    "Program Manager - RTP Initiative",
    80000,
    "Interviewed"
)
application3 = JobApplication(
    "Schools, Mentoring, And Resource Team, Inc (SMART, INC)",
    "Volunteer Program Manager",
    83000,
    "Interviewed"
)
application3.display_application()

application1.display_application()

application2.display_application()

application3.display_application()

print()