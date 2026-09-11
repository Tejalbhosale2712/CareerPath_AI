import os
import requests
from dotenv import load_dotenv

load_dotenv()


def calculate_job_match(
    user_skills,
    required_skills,
    job_title="",
    target_role=""
):
    user_skills_lower = [
        skill.lower().strip()
        for skill in user_skills
    ]

    required_skills_list = [
        skill.strip()
        for skill in required_skills.split(',')
        if skill.strip()
    ]

    matched_skills = []
    missing_skills = []

    for skill in required_skills_list:

        if skill.lower() in user_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if required_skills_list:
        skill_match = (
            len(matched_skills) /
            len(required_skills_list)
        ) * 100
    else:
        skill_match = 0

    role_match = 0

    if target_role and job_title:

        target_words = target_role.lower().split()
        job_title_lower = job_title.lower()

        matched_role_words = sum(
            1
            for word in target_words
            if word in job_title_lower
        )

        if matched_role_words > 0:
            role_match = 100

    final_score = (
        (skill_match * 0.7) +
        (role_match * 0.3)
    )

    return {
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'skill_match': round(skill_match, 2),
        'role_match': role_match,
        'match_percentage': round(final_score, 2)
    }

def calculate_description_match(
    user_skills,
    job_description,
    job_title="",
    target_role=""
):
    """
    Calculate job match based on:
    1. Skills required by the job description
    2. Skills available in the user's resume
    3. Target role match
    """

    description = job_description.lower()

    # Common skills that may appear in job descriptions
    skill_keywords = [
        "python",
        "java",
        "c",
        "c++",
        "sql",
        "mysql",
        "postgresql",
        "django",
        "flask",
        "html",
        "css",
        "javascript",
        "react",
        "git",
        "github",
        "pandas",
        "numpy",
        "matplotlib",
        "scikit-learn",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "statistics",
        "data analysis",
        "data visualization",
        "power bi",
        "power query",
        "dax",
        "tableau",
        "excel",
        "advanced excel",
        "communication",
        "reporting",
        "problem solving",
        "financial analysis",
        "accounting",
        "digital marketing",
        "seo",
        "recruitment",
        "sales",
        "customer service",
        "crm",
        "graphic design",
        "photoshop",
        "illustrator",
        "canva",
        "content writing",
        "video editing",
        "project management",
        "operations management"
    ]

    # Find skills required by the job
    required_skills = []

    for skill in skill_keywords:
        if skill.lower() in description:
            required_skills.append(skill)

    # Remove duplicates
    required_skills = list(dict.fromkeys(required_skills))

    # Normalize user's skills
    user_skills_lower = [
        skill.lower().strip()
        for skill in user_skills
    ]

    # Find matching skills
    matched_skills = []

    for required_skill in required_skills:
        if required_skill.lower() in user_skills_lower:
            matched_skills.append(required_skill)

    # Calculate skill match
    if required_skills:
        skill_match = (
            len(matched_skills) /
            len(required_skills)
        ) * 100
    else:
        skill_match = 0

    # Calculate role match
    role_match = 0

    if target_role and job_title:

        target_words = target_role.lower().split()
        job_title_lower = job_title.lower()

        matched_role_words = sum(
            1
            for word in target_words
            if word in job_title_lower
        )

        if matched_role_words > 0:
            role_match = 100

    # Final score
    final_score = (
        (skill_match * 0.7) +
        (role_match * 0.3)
    )

    # Skills required by job but missing from resume
    missing_skills = [
        skill
        for skill in required_skills
        if skill not in matched_skills
    ]

    return {
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'skill_match': round(skill_match, 2),
        'role_match': role_match,
        'match_percentage': round(final_score, 2)
    }


def search_adzuna_jobs(
    target_role,
    location="Pune",
    results_per_page=10
):
    """
    Fetch real job listings from Adzuna API.
    """

    app_id = os.getenv("ADZUNA_APP_ID")
    app_key = os.getenv("ADZUNA_APP_KEY")

    if not app_id or not app_key:
        return []

    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "results_per_page": results_per_page,
        "what": target_role,
        "where": location,
        "content-type": "application/json",
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("results", [])

    except requests.RequestException:

        return []

from urllib.parse import quote_plus


def get_linkedin_jobs_url(target_role, location="Pune"):
    """
    Generate LinkedIn job search URL.
    """
    keywords = quote_plus(target_role)
    location = quote_plus(location)

    return (
        f"https://www.linkedin.com/jobs/search/"
        f"?keywords={keywords}&location={location}"
    )


def get_naukri_jobs_url(target_role, location="Pune"):
    """
    Generate Naukri job search URL.
    """
    keywords = quote_plus(target_role)
    location = quote_plus(location)

    return (
        f"https://www.naukri.com/"
        f"{keywords.replace('+', '-')}-jobs-in-{location.replace('+', '-')}"
    )