from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    likes = models.ManyToManyField(User, related_name="posts")


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    def like_count(self):
        return self.likes.count()

    @classmethod
    def get_profile_images(cls,profile):
        return cls.objects.filter(profile = profile)

    


class Profile(models.Model):
    '''
    Class that defines the profile objects
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio =  models.TextField(blank=True)
    followers = models.ManyToManyField(User, related_name='followers')
    following = models.ManyToManyField(User, related_name='following')

    def __str__(self):
        return self.user.username

    @classmethod
    def search_user(cls,username):
        #searched_user = User.objects.filter(username__icontains = username ) 
        return User.objects.filter(username__icontains = username)


@receiver(post_save, sender = User)
def create_profile(sender, instance,created, **kwargs):
     if created:
        Profile.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_profile( sender, instance, **kwargs):
    instance.profile.save()

    

class Comment(models.Model):
    '''
    Class that determines the comment objects
    '''
    image = models.ForeignKey(Image, on_delete= models.CASCADE, related_name = "comments")
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls,image):
        return cls.objects.filter(image =image)

