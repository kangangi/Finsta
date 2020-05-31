from .models import Image,Comment, Profile
from django.forms import ModelForm

class AddImageForm(ModelForm):
    class Meta :
        model = Image
        exclude = ['profile', 'pub_date', 'likes']

class AddProfpicForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
