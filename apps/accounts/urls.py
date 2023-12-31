from django.urls import  path
from . import views
from .views import UserPasswordResetView

urlpatterns=[
    path('register', views.Registerview.as_view(), name='register'),
    path('login',views.LoginView.as_view(),name='login'),
    path('profile',views.UserProfile.as_view(),name='profile'),
    path('changepassword', views.ChangePasswordUser.as_view(),name='change'),
    path('sendemailchangepassword', views.SendEmailResetPasswordView.as_view(),name='sendemailchanegpassword'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]