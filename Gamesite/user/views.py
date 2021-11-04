from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcome {username}, your account successfully created')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/sign-up.html', context={'form': form})

@login_required()
def user_profile(request):
    return render(request, 'user/profile.html')
