from django.urls import  path
from . import views
urlpatterns=[
    path('register', views.Registerview.as_view(), name='register'),
    path('login',views.LoginView.as_view(),name='login'),
    path('profile',views.UserProfile.as_view(),name='profile'),
    path('changepassword', views.ChangePasswordUser.as_view(),name='change')
]