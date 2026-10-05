from django.urls import path
from views import *

app_name = account

urlpatterns = [
    path('register/',regester_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout',logout_view,name='logout'),
]