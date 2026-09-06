from django.urls import path
from . import views

urlpatterns = [

    path(
        'analyze/',
        views.skill_gap_analysis,
        name='skill_gap_analysis'
    ),

    path(
        'jobs/',
        views.job_recommendations,
        name='job_recommendations'
    ),

    path(
        'roadmap/',
        views.learning_roadmap,
        name='learning_roadmap'
    ),
]