from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm
from django.views import View
from django.views.generic import CreateView, FormView

# def regester_view(request):
#     if request.user.is_authenticate:
#         return redirect('/')

#     if request.method == 'POST':
#         form = UserRegistrationForm(request.post)

#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     form=UserRegistrationForm()
#     context = {'form':form}
#     return render(request,'account/register.html',context=context)

class RegisterView(View):

    def get(self,request):
        if request.user.is_authenticated:
            return render ('/')
        
        form=UserRegistrationForm()
        context = {'form':form}
        return render(request,'account/register.html',context=context)
    
    def post(self,request):
        if request.user.is_authenticated:
            return redirect('/')
        
        form = UserRegistrationForm(request.post)
        if form.is_valid:
            form.save()
            return redirect('/')
        
        form = UserRegistrationForm()
        context = {'form':form}
        return render(request,'account/register.html',context=context)


# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('/')

#     if request.method == 'POST':
#         form = LoginForm(request.post)

#         if form.is_valid():
#             user= form.cleaned_data.get('user')
#             if user is not None:
#                 login(request,user)
#                 return redirect('/')

#     form = LoginForm()
#     context = {'form': form}
#     return render(request,'login.html',context=context)
class LoginView(View):

    def get(self,request):
        if request.user.is_authenticated:
            return render ('/')
        
        form=LoginForm()
        context = {'form':form}
        return render(request,'account/login.html',context=context)
    
    def post(self,request):
        if request.user.is_authenticated:
            return redirect('/')
        
        form = LoginForm(request.post)
        if form.is_valid:
            form.save()
            return redirect('/')
        
        form = LoginForm()
        context = {'form':form}
        return render(request,'account/login.html',context=context)
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

