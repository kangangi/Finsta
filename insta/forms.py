from .models import Image,Comment
from django.forms import ModelForm
# image = models.ForeignKey(Image, on_delete= models.CASCADE)
#     content = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

class AddImageForm(ModelForm):
    class Meta :
        model = Image
        exclude = ['profile', 'pub_date', 'likes']

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['image','pub_date','user']