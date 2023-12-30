from django.urls import  path
from . import views
urlpatterns=[
    path('register', views.Registerview.as_view(), name='register')
]