from django.urls import path
from . import views

urlpatterns = [
    path('select-role/', views.select_role, name='select_role'),
]