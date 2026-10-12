from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('post/',PostListView.as_view(),name='post-list'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('post/create/',PostCraeteView.as_view(),name='post-create'),
]