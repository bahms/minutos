from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = UserProfile.objects.create(user=user)
            userprofile.save()

            login(request, user)
            return redirect(to='frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {'form': form})
