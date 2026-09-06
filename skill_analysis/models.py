from django.db import models
from django.contrib.auth.models import User


class JobRole(models.Model):
    role_name = models.CharField(max_length=100)

    required_skills = models.TextField(
        help_text="Enter skills separated by commas"
    )

    def __str__(self):
        return self.role_name


class SkillGapAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    job_role = models.ForeignKey(
        JobRole,
        on_delete=models.CASCADE
    )

    matched_skills = models.TextField(blank=True)

    missing_skills = models.TextField(blank=True)

    readiness_score = models.FloatField(default=0)

    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job_role.role_name}"


class Job(models.Model):
    job_title = models.CharField(max_length=150)

    company_name = models.CharField(max_length=150)

    required_skills = models.TextField(
        help_text="Enter skills separated by commas"
    )

    location = models.CharField(max_length=100)

    job_type = models.CharField(max_length=50)

    job_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.job_title} - {self.company_name}"


class LearningRoadmap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    skill = models.CharField(max_length=100)

    level = models.CharField(
        max_length=50,
        default='Beginner'
    )

    topic = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    order = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.skill}"