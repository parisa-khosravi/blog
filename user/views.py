from django.shortcuts import render
from .forms import ProfileEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView
from .models import Profile


class ProfileEditView(LoginRequiredMixin,UpdateView):
    form_class = ProfileEditForm
    template_name = 'user/profile_edit.html'
    succes_url = reverse_lazy('user:profile-edit')
    login_url = 'account/login.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

class ProfileListView(ListView):
    # Using model or query set
    # model = Profile
    queryset = Profile.objects.all()
    template_name = 'user/profile_list.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):

    template_name = 'user/profile_detail.html'
    model =  Profile
    context_object_name = 'profile'
    
