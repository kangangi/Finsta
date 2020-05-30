from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile, Comment
from .forms import AddImageForm



# Create your views here.
@login_required()
def home(request):
    '''
    Displays home page
    '''
    title = "Finsta"
    images = Image.objects.all()
    
    return render(request, "home.html", {"images": images})


def profile(request):
    '''
    Displays User's profile page
    '''
    title = "Profile"
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    return render(request, 'profile.html', {"profile" : profile})

@login_required
def upload_image(request):
    if request.method == "POST":
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = request.user
            image.save()
        return redirect('home')
    else:
        form = AddImageForm()
    return render(request, 'upload_image.html', {"form": form})

