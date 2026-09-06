from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CareerProfileForm
from .models import CareerProfile


@login_required
def select_role(request):

    profile, created = CareerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = CareerProfileForm(request.POST)

        if form.is_valid():

            selected_role = form.cleaned_data['target_role']

            profile.target_role = selected_role.role_name
            profile.save()

            return redirect('dashboard')

    else:

        form = CareerProfileForm()

    return render(
        request,
        'career/select_role.html',
        {'form': form}
    )