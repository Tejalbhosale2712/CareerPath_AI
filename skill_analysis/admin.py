from django.contrib import admin
from .models import JobRole, Job, LearningRoadmap


@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    list_display = ('role_name',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'company_name',
        'location',
        'job_type',
    )

    search_fields = (
        'job_title',
        'company_name',
        'location',
    )


@admin.register(LearningRoadmap)
class LearningRoadmapAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'skill',
        'level',
        'topic',
        'order',
    )

    search_fields = (
        'user__username',
        'skill',
        'topic',
    )

    list_filter = (
        'level',
    )

    ordering = (
        'user',
        'order',
    )