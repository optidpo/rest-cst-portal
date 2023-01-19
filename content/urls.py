from content import views
from django.urls import re_path, path

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.loginUser, name='login'),
  re_path('logout', views.logoutUser, name='logout'),
  re_path('register', views.register, name='register'),
]