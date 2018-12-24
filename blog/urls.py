from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),  #empyt path, views.home is the hoem function that we created in views,name should be different
    path('about/',views.about,name='blog-about'),
]
