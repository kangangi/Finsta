from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile, Comment
from .forms import AddImageForm,AddProfpicForm
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
@login_required()
def home(request):
    '''
    Displays home page
    '''
    title = "Finsta"
    images = Image.objects.all().order_by("-pub_date")
    
    return render(request, "home.html", {"images": images})


def profile(request):
    '''
    Displays User's profile page
    '''
    title = "Profile"
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    images = Image.get_profile_images(current_user)
    posts = images.count()
    return render(request, 'profile.html', {"profile" : profile, "images":images, "posts": posts} )

@login_required
def upload_image(request):
    '''
    Enables user to upload image
    '''
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
        message =f"{searched_user}"
       
        
        return render(request, 'search.html', {"profile": profile,"message": message})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html', {"message": message}) 

def search_profile(request, user):
    '''
    Displays searched profile page
    '''
    title = "Profile"
    profile = Profile.objects.get(user =user)
    images = Image.get_profile_images(user)
    posts = images.count()
    return render(request, 'search_profile.html', {"profile" : profile, "images":images, "posts": posts} )


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

    return HttpResponseRedirect(reverse('image_details',args =[int(image.id)]))

def like_image(request,id):
    '''
    Adds and removes likes
    '''
    image = Image.objects.get(pk=id)
    liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        liked = False
    else:
        image.likes.add(request.user)
        liked = True 
    return HttpResponseRedirect(reverse('image_details',args =[int(image.id)]))


def image_details(request,id):
    '''
    Shows image details 
    '''
    image = Image.objects.get(pk=id)
    total_likes = image.like_count()
    comments = Comment.get_image_comments(image)
    liked = False
    if image.likes.filter(id =request.user.id).exists():
        liked = True

    return render(request, 'image_details.html',{"image": image, "total_likes": total_likes, "comments": comments ,"liked" : liked})

def edit_profile(request):
    '''
    Edits profile picture and bio
    '''
    current_user = request.user

    if request.method == "POST":
        form = AddProfpicForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data['profile_pic']
            bio  = form.cleaned_data['bio']

            updated_profile = Profile.objects.get(user= current_user)
            updated_profile.profile_pic = profile_pic
            updated_profile.bio = bio
            updated_profile.save()
        return redirect('profile')
    else:
        form = AddProfpicForm()
    return render(request, 'edit_profile.html', {"form": form})



def add_comment_homepage(request,id):
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

