from content import views
from django.urls import re_path, path

urlpatterns = [
  path('', views.index, name='index'),
]