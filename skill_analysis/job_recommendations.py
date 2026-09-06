def calculate_job_match(user_skills, required_skills, job_title="", target_role=""):

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

    # Compare user skills with job skills
    for skill in required_skills_list:

        if skill.lower() in user_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    # Skill match percentage
    if required_skills_list:
        skill_match = (
            len(matched_skills) /
            len(required_skills_list)
        ) * 100
    else:
        skill_match = 0

    # Target role relevance
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

    # Final recommendation score
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