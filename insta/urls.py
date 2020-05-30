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
    path('comment/<int:id>', views.add_comment,name = "add_comment" )
]
