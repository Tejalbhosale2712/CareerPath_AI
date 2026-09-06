from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    text = ""

    reader = PdfReader(pdf_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


SKILLS = [
    # Programming / IT
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "Django",
    "Flask",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Git",
    "GitHub",

    # Data / AI
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Scikit-learn",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Statistics",
    "Data Analysis",
    "Data Visualization",
    "Power BI",
    "Power Query",
    "DAX",
    "Tableau",

    # Office / Business
    "Excel",
    "Advanced Excel",
    "Communication",
    "Reporting",
    "Presentation",
    "Problem Solving",
    "Time Management",
    "Team Management",
    "Business Strategy",

    # Finance / Accounting
    "Accounting",
    "Tally",
    "GST",
    "Financial Analysis",
    "Financial Modeling",
    "Financial Reporting",
    "Bookkeeping",
    "Taxation",
    "Banking",
    "Financial Services",

    # Marketing
    "Digital Marketing",
    "SEO",
    "Social Media Marketing",
    "Content Marketing",
    "Analytics",

    # HR / Recruitment
    "Recruitment",
    "Employee Relations",
    "HR Management",
    "Payroll",
    "Interviewing",
    "Sourcing",
    "LinkedIn",
    "Negotiation",

    # Sales / Customer Service
    "Sales",
    "Customer Service",
    "Customer Relationship Management",
    "CRM",
    "Lead Generation",

    # Design / Creative
    "Graphic Design",
    "Photoshop",
    "Illustrator",
    "Canva",
    "Creativity",
    "Typography",
    "Branding",

    # Content / Media
    "Content Writing",
    "English",
    "Research",
    "Copywriting",
    "Editing",
    "Video Editing",
    "Adobe Premiere Pro",
    "After Effects",
    "Storytelling",
    "Audio Editing",

    # Education
    "Teaching",
    "Subject Knowledge",
    "Classroom Management",
    "Lesson Planning",

    # Operations / Project / Supply Chain
    "Operations Management",
    "Process Management",
    "Project Management",
    "Inventory Management",
    "Logistics",
    "Procurement",
    "Supply Chain Management",
    "Event Management",
    "Planning",
    "Budgeting",
]

SKILL_ALIASES = {
    "powerbi": "Power BI",
    "power bi": "Power BI",

    "ms excel": "Excel",
    "microsoft excel": "Excel",
    "advanced excel": "Advanced Excel",

    "mysql database": "MySQL",
    "postgres database": "PostgreSQL",
    "postgresql database": "PostgreSQL",

    "machinelearning": "Machine Learning",
    "machine learning": "Machine Learning",

    "artificial intelligence": "Artificial Intelligence",
    "ai": "Artificial Intelligence",

    "data visualization": "Data Visualization",
    "data analysis": "Data Analysis",

    "scikit learn": "Scikit-learn",
    "sklearn": "Scikit-learn",

    "ms power bi": "Power BI",
    "power-query": "Power Query",
}


def extract_skills(resume_text):
    found_skills = []
    resume_text_lower = resume_text.lower()

    for skill in SKILLS:
        if skill.lower() in resume_text_lower:
            found_skills.append(skill)

    # Check skill aliases
    for alias, standard_skill in SKILL_ALIASES.items():
        if alias in resume_text_lower:
            if standard_skill not in found_skills:
                found_skills.append(standard_skill)

    return found_skills


def extract_section(resume_text, section_names):

    lines = resume_text.splitlines()

    section_content = []

    capturing = False

    common_headings = [
        "skills",
        "technical skills",
        "education",
        "academic qualification",
        "educational qualification",
        "experience",
        "work experience",
        "professional experience",
        "internship",
        "projects",
        "academic projects",
        "personal projects",
        "certifications",
        "certificates",
        "courses",
        "courses & certifications",
        "achievements",
        "summary",
        "objective",
        "profile",
    ]

    for line in lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        clean_lower = clean_line.lower()

        # Start requested section
        if any(
            section.lower() in clean_lower
            for section in section_names
        ):
            capturing = True
            continue

        # Stop when another section heading is found
        if capturing:

            is_new_heading = any(
                heading == clean_lower
                or heading in clean_lower
                for heading in common_headings
            )

            is_requested_heading = any(
                section.lower() in clean_lower
                for section in section_names
            )

            if is_new_heading and not is_requested_heading:
                break

            section_content.append(clean_line)

    return section_content


def extract_education(resume_text):

    return extract_section(
        resume_text,
        [
            "education",
            "academic qualification",
            "educational qualification",
            "academic background",
        ]
    )


def extract_experience(resume_text):

    return extract_section(
        resume_text,
        [
            "experience",
            "work experience",
            "professional experience",
            "internship",
            "employment history",
        ]
    )


def extract_projects(resume_text):

    return extract_section(
        resume_text,
        [
            "projects",
            "academic projects",
            "personal projects",
            "project experience",
        ]
    )


def extract_certifications(resume_text):

    return extract_section(
        resume_text,
        [
            "certifications",
            "certificates",
            "courses",
            "courses & certifications",
            "professional certifications",
        ]
    )