from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from resume.models import Resume
from resume.utils import extract_text_from_pdf, extract_skills

from career.models import CareerProfile

from .models import JobRole, SkillGapAnalysis, Job
from .job_recommendations import (
    calculate_job_match,
    calculate_description_match,
    search_adzuna_jobs,
    get_linkedin_jobs_url,
    get_naukri_jobs_url
)
from .roadmap import generate_roadmap


@login_required
def skill_gap_analysis(request):

    resume = Resume.objects.filter(
        user=request.user
    ).order_by('-uploaded_at').first()

    if not resume:
        return render(
            request,
            'skill_analysis/skill_gap.html',
            {
                'error': 'Please upload your resume first.'
            }
        )

    profile = CareerProfile.objects.filter(
        user=request.user
    ).first()

    if not profile or not profile.target_role:
        return render(
            request,
            'skill_analysis/skill_gap.html',
            {
                'error': 'Please select your target career role first.'
            }
        )

    job_role = JobRole.objects.filter(
        role_name__iexact=profile.target_role.strip()
    ).first()

    if not job_role:
        return render(
            request,
            'skill_analysis/skill_gap.html',
            {
                'error': 'Selected career role was not found.'
            }
        )

    resume_text = extract_text_from_pdf(resume.file)

    user_skills = extract_skills(resume_text)

    required_skills = [
        skill.strip()
        for skill in job_role.required_skills.split(',')
        if skill.strip()
    ]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if any(
            skill.lower() == user_skill.lower()
            for user_skill in user_skills
        ):
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if required_skills:
        readiness_score = round(
            (len(matched_skills) / len(required_skills)) * 100,
            2
        )
    else:
        readiness_score = 0

    analysis = SkillGapAnalysis.objects.create(
        user=request.user,
        job_role=job_role,
        matched_skills=', '.join(matched_skills),
        missing_skills=', '.join(missing_skills),
        readiness_score=readiness_score
    )

    return render(
        request,
        'skill_analysis/skill_gap.html',
        {
            'resume': resume,
            'job_role': job_role,
            'matched_skills': matched_skills,
            'missing_skills': missing_skills,
            'readiness_score': readiness_score,
            'analysis': analysis,
        }
    )


@login_required
def job_recommendations(request):

    resume = Resume.objects.filter(
        user=request.user
    ).order_by('-uploaded_at').first()

    if not resume:
        return render(
            request,
            'skill_analysis/job_recommendations.html',
            {
                'recommendations': [],
                'error': 'Please upload your resume first.'
            }
        )

    profile = CareerProfile.objects.filter(
        user=request.user
    ).first()

    if not profile or not profile.target_role:
        return render(
            request,
            'skill_analysis/job_recommendations.html',
            {
                'recommendations': [],
                'error': 'Please select your target career role first.'
            }
        )

    resume_text = extract_text_from_pdf(resume.file)

    user_skills = extract_skills(resume_text)

    # -------------------------------------------------
    # REAL JOBS FROM ADZUNA
    # -------------------------------------------------

    adzuna_jobs = search_adzuna_jobs(
        target_role=profile.target_role,
        location="Pune",
        results_per_page=10
    )

    recommendations = []

    for job in adzuna_jobs:

        job_title = job.get(
            'title',
            'Job Opportunity'
        )

        company_data = job.get(
            'company',
            {}
        )

        company_name = company_data.get(
            'display_name',
            'Company not specified'
        )

        location_data = job.get(
            'location',
            {}
        )

        location_name = location_data.get(
            'display_name',
            'Location not specified'
        )

        description = job.get(
            'description',
            ''
        )

        # -------------------------------------------------
        # CALCULATE JOB MATCH
        # -------------------------------------------------

        result = calculate_description_match(
            user_skills,
            description,
            job_title,
            profile.target_role
        )

        recommendations.append({
            'title': job_title,
            'company': company_name,
            'location': location_name,
            'description': description,
            'salary_min': job.get('salary_min'),
            'salary_max': job.get('salary_max'),
            'job_url': job.get('redirect_url'),
            'match_percentage': result['match_percentage'],
            'matched_skills': result['matched_skills'],
            'missing_skills': result['missing_skills'],
            'source': 'Adzuna'
        })

    # -------------------------------------------------
    # SORT JOBS BY MATCH PERCENTAGE
    # -------------------------------------------------

    recommendations.sort(
        key=lambda x: x['match_percentage'],
        reverse=True
    )

    # -------------------------------------------------
    # LINKEDIN JOB SEARCH
    # -------------------------------------------------

    linkedin_url = get_linkedin_jobs_url(
        profile.target_role,
        "Pune"
    )

    # -------------------------------------------------
    # NAUKRI JOB SEARCH
    # -------------------------------------------------

    naukri_url = get_naukri_jobs_url(
        profile.target_role,
        "Pune"
    )

    return render(
        request,
        'skill_analysis/job_recommendations.html',
        {
            'recommendations': recommendations,
            'target_role': profile.target_role,
            'resume': resume,
            'user_skills': user_skills,

            # LinkedIn and Naukri
            'linkedin_url': linkedin_url,
            'naukri_url': naukri_url,
        }
    )


@login_required
def learning_roadmap(request):

    # Get the user's latest skill gap analysis
    analysis = SkillGapAnalysis.objects.filter(
        user=request.user
    ).order_by('-analyzed_at').first()

    if not analysis:
        return render(
            request,
            'skill_analysis/learning_roadmap.html',
            {
                'roadmap': [],
                'message': 'Please complete Skill Gap Analysis first.'
            }
        )

    # Convert missing skills text into a list
    missing_skills = [
        skill.strip()
        for skill in analysis.missing_skills.split(',')
        if skill.strip()
    ]

    # Generate personalized roadmap
    roadmap = generate_roadmap(missing_skills)

    return render(
        request,
        'skill_analysis/learning_roadmap.html',
        {
            'roadmap': roadmap,
            'analysis': analysis,
            'target_role': analysis.job_role.role_name,
        }
    )