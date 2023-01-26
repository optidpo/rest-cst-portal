from content import views
from django.urls import re_path, path

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.loginUser, name='login'),
  re_path('logout', views.logoutUser, name='logout'),
  re_path('register', views.register, name='register'),
  re_path(r'^profile/(?P<username>\w{0,50})/$', views.myprofile, name='myprofile'),
  path('game/<int:id>/buy', views.BuyGame, name="BuyGame"),
  # path('game/<int:id>/buy/', views.BuyGame, name="BuyGame"),
  # re_path(r'^game/<id>(\d+)/buy/$', views.BuyGame, name="BuyGame"),
  re_path(r'^orders/(?P<username>\w{0,50})/$', views.OrdersMade, name='Orders'),
  re_path(r'^profile/(?P<username>\w{0,50})/edit/$', views.editprofile, name='editprofile'),
  re_path(r'^oauth/success', views.oauth_success, name='test_oauth_success'),
	re_path(r'^stk-push/success', views.stk_push_success, name='test_stk_push_success'),
	re_path(r'^business-payment/success', views.business_payment_success, name='test_business_payment_success'),
	re_path(r'^salary-payment/success', views.salary_payment_success, name='test_salary_payment_success'),
	re_path(r'^promotion-payment/success', views.promotion_payment_success, name='test_promotion_payment_success'),
  path('TopUpCard', views.TopUpCard, name='TopUpCard'),
  
  
]