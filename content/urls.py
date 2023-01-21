from content import views
from django.urls import re_path, path

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.loginUser, name='login'),
  re_path('logout', views.logoutUser, name='logout'),
  re_path('register', views.register, name='register'),
  re_path(r'^profile/(?P<username>\w{0,50})/$', views.myprofile, name='myprofile'),
  # path('profile/<str:username>/game/<int:id>/buy', views.buyGame, name="EditPortfolio"),
  re_path(r'^game/<id>(\d+)/buy/$', views.BuyGame, name="BuyGame"),
  re_path(r'^orders/(?P<username>\w{0,50})/$', views.OrdersMade, name='Orders'),
  re_path(r'^profile/(?P<username>\w{0,50})/edit/$', views.editprofile, name='editprofile'),
 
  path('TopUpCard', views.TopUpCard, name='TopUpCard'),
  
  
]