from django import forms
from .models import CareerProfile
from skill_analysis.models import JobRole


class CareerProfileForm(forms.ModelForm):

    target_role = forms.ModelChoiceField(
        queryset=JobRole.objects.all().order_by('role_name'),
        empty_label="Select your target role",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = CareerProfile
        fields = ['target_role']