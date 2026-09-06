from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from resume.models import Resume
from resume.utils import extract_text_from_pdf, extract_skills

from career.models import CareerProfile
from .models import JobRole, SkillGapAnalysis

from .models import JobRole, SkillGapAnalysis, Job
from .job_recommendations import calculate_job_match
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

    jobs = Job.objects.all()

    recommendations = []

    for job in jobs:

        result = calculate_job_match(
            user_skills,
            job.required_skills,
            job.job_title,
            profile.target_role
        )

        if result['match_percentage'] >= 40:

            recommendations.append({
                'job': job,
                'matched_skills': result['matched_skills'],
                'missing_skills': result['missing_skills'],
                'match_percentage': result['match_percentage']
            })

    recommendations.sort(
        key=lambda x: x['match_percentage'],
        reverse=True
    )

    return render(
        request,
        'skill_analysis/job_recommendations.html',
        {
            'recommendations': recommendations,
            'target_role': profile.target_role,
            'resume': resume,
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