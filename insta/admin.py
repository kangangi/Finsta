from django.contrib import admin
from .models import Comment, Profile, Image

# Register your models here.
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Image)
