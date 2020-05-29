from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Image(models.Model):
    '''
    Class that defines the image objects
    '''
    image = CloudinaryField('image')
    name = models.CharField(max_length = 30)
    caption = models.TextField(blank= True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(default= 0)


    def __str__(self):
        return self.name

class Profile(models.Model):
    '''
    Class that defines the profile objects
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio =  models.TextField(blank=True)

    def __str__(self):
        return self.user

class Comment(models.Model):
    '''
    Class that determines the comment objects
    '''
    image = models.ForeignKey(Image, on_delete= models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
