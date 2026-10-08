from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout',logout_view,name='logout'),
]