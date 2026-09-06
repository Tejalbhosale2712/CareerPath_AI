from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_resume, name='upload_resume'),
    path(
        'analyze/<int:resume_id>/',
        views.analyze_resume,
        name='analyze_resume'
    ),
]