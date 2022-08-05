from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.getBlogs, name='blog'),
    path('<slug>', views.getBlog, name='post'),
]