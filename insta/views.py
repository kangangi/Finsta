from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile, Comment
from .forms import AddImageForm, AddCommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse



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
    images = Image.get_profile_images(current_user)
    return render(request, 'profile.html', {"profile" : profile, "images":images} )

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


@login_required
def user_search(request):
    '''
    Display the search results
    '''
    if "user" in request.GET and request.GET["user"]:
        searched_user = request.GET.get("user")
        profile = Profile.search_user(searched_user)
       
        print(profile)
        
        return render(request, 'search.html', {"profile": profile})

def search_profile(request, user):
    '''
    Displays searched profile page
    '''
    title = "Profile"
    profile = Profile.objects.get(user =user)
    images = Image.get_profile_images(user)
    return render(request, 'search_profile.html', {"profile" : profile, "images":images} )


def add_comment(request,id):
    '''
    Add new comments 
    '''
    image = Image.objects.get(pk=id)
    content= request.GET.get("comment")
    print(content)
    user = request.user
    comment = Comment( image = image, content = content, user = user)
    comment.save_comment()

    return redirect('home')

def like_image(request,id):
    image = Image.objects.get(pk=id)
    image.likes.add(request.user)

    return HttpResponseRedirect(reverse('home'))


