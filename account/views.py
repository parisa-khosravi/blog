from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm

def regester_view(request):
    if request.user.is.authenticate:
        return redirect('/')

    if request.method == 'POST':
        form = UserRegistrationForm(request.post)

        if form.is_valid():
            form.save()
            return redirect('/')

    form=UserRegistrationForm()
    context = {'form'=form}
    return render(request,'account/register.html',context=context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.post)

        if form.is_valid():
            user= form.cleaned_data.get('user')
            if user is not None:
                login(request,user)
                return redirect('/')

    form = LoginForm()
    context = {'form': form}
    return render(request,'login.html',context=context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

