from django.shortcuts import render

# Create your views here.
def home(request):
    '''
    Displays home page
    '''
    title = "Finsta"
    
    return render(request, "home.html")
