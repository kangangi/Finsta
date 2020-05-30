from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile, Comment



# Create your views here.
@login_required()
def home(request):
    '''
    Displays home page
    '''
    title = "Finsta"
    
    return render(request, "home.html")


def profile(request):
    '''
    Displays User's profile page
    '''
    title = "Profile"
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    return render(request, 'profile.html', {"profile" : profile})
