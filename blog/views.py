from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class PostListView(ListView):

    queryset = Post.objects.all()
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    paginate_by = 2

class PostDetailView(DetailView):

    queryset = Post.objects.all()
    template_name = "blog/post_details.html"
    ontext_object_name = 'post'

class PostCraeteView(LoginRequiredMixin,CreateView):

    form_class = PostCreateForm
    template_name = "post_create.html"
    success_url = "/"

# To check whether the author is the same as the logged-in user.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


