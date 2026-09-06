from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ResumeUploadForm
from .models import Resume
from .utils import (
    extract_text_from_pdf,
    extract_skills,
    extract_education,
    extract_experience,
    extract_projects,
    extract_certifications,
)

@login_required
def upload_resume(request):

    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)

        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            messages.success(
                request,
                "Resume uploaded successfully!"
            )

            return redirect('upload_resume')

    else:
        form = ResumeUploadForm()

    resumes = Resume.objects.filter(
        user=request.user
    ).order_by('-uploaded_at')

    return render(
        request,
        'resume/upload_resume.html',
        {
            'form': form,
            'resumes': resumes
        }
    )

@login_required
def analyze_resume(request, resume_id):

    resume = Resume.objects.get(
        id=resume_id,
        user=request.user
    )

    # Extract complete resume text
    resume_text = extract_text_from_pdf(resume.file)

    # Extract skills
    skills = extract_skills(resume_text)

    # Extract resume sections
    education = extract_education(resume_text)

    experience = extract_experience(resume_text)

    projects = extract_projects(resume_text)

    certifications = extract_certifications(resume_text)

    return render(
        request,
        'resume/analyze_resume.html',
        {
            'resume': resume,
            'resume_text': resume_text,
            'skills': skills,
            'education': education,
            'experience': experience,
            'projects': projects,
            'certifications': certifications,
        }
    )