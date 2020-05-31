from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home , name = "home"),
    path('profile/',views.profile, name = "profile"),
    path('upload/image/', views.upload_image, name = "upload_image"),
    path('search/', views.user_search, name = "user_search"),
    path('search/<user>', views.search_profile, name = "search_profile"),
    path('comment/<int:id>', views.add_comment,name = "add_comment" ),
    path('like/<int:id>', views.like_image, name = 'like_image'),
    path('image/details/<int:id>', views.image_details, name = 'image_details'),
    path('profile/edit', views.edit_profile,name = 'edit_profile')
]
