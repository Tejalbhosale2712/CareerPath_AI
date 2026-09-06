from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_home(request):

    from resume.models import Resume
    from skill_analysis.models import SkillGapAnalysis, Job

    resumes_count = Resume.objects.filter(
        user=request.user
    ).count()

    latest_analysis = SkillGapAnalysis.objects.filter(
        user=request.user
    ).order_by('-analyzed_at').first()

    if latest_analysis:
        readiness_score = latest_analysis.readiness_score

        matched_skills_count = len([
            skill.strip()
            for skill in latest_analysis.matched_skills.split(',')
            if skill.strip()
        ])
    else:
        readiness_score = 0
        matched_skills_count = 0

    jobs_count = Job.objects.count()

    return render(
        request,
        'dashboard/dashboard.html',
        {
            'resumes_count': resumes_count,
            'readiness_score': readiness_score,
            'matched_skills_count': matched_skills_count,
            'jobs_count': jobs_count,
        }
    )