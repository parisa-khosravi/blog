from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm
from django.views import View
from django.views.generic import CreateView, FormView
# Creating register view based on Function-Based View (FBV)

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
######
# Creating register view based on Class-Based View (CBV) By inheriting from View
# class RegisterView(View):

#     def get(self,request):
#         if request.user.is_authenticated:
#             return render ('/')
        
#         form=UserRegistrationForm()
#         context = {'form':form}
#         return render(request,'account/register.html',context=context)
    
#     def post(self,request):
#         if request.user.is_authenticated:
#             return redirect('/')
        
#         form = UserRegistrationForm(request.post)
#         if form.is_valid:
#             form.save()
#             return redirect('/')
        
#         form = UserRegistrationForm()
#         context = {'form':form}
#         return render(request,'account/register.html',context=context)

# Creating login view based on Function-Based View (FBV)
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
# Creating login view based on Class-Based View (CBV) By inheriting from View
# class LoginView(View):

#     def get(self,request):
#         if request.user.is_authenticated:
#             return render ('/')
        
#         form=LoginForm()
#         context = {'form':form}
#         return render(request,'account/login.html',context=context)
    
#     def post(self,request):
#         if request.user.is_authenticated:
#             return redirect('/')
        
#         form = LoginForm(request.post)
#         if form.is_valid:
#             form.save()
#             return redirect('/')
        
#         form = LoginForm()
#         context = {'form':form}
#         return render(request,'account/login.html',context=context)
#####
class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "account/register.html"
    success_url='/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect ('/')
        
        return super().dispatch(request, *args, **kwargs)

class LoginView(FormView):
    form_class = LoginForm
    template_name = "account/login.html"
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user=form.cleaned_data.get('user')
        if user is not None:
            login(self.request,user)
            return super().form_valid(form)
        
        return super().form_invalid(form)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

