from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def home(request):
    '''
    Displays home page
    '''
    title = "Finsta"
    
    return render(request, "home.html")
