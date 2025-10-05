from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views



# Create your views here.

class registerView (View):

    # Handle The Post Request in the registration page
    def post(self, request) :
        form = CustomUserCreationForm(request.POST)
        if (form.is_valid()) :
            form.save( )
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
        else :
            form = CustomUserCreationForm()
        return render (request, "blog/register.html", {"form": form})
    
    # Handle The Get Request
    def get(self, request) :
        form = CustomUserCreationForm()
        return render (request, "blog/register.html", {"form": form})

@method_decorator(login_required, name='dispatch')
class profilView ( View ) :

    def post (self, request) :
        form = UserUpdateForm(request.POST,  instance=request.user)
        if (form.is_valid()) :
            form.save()
            messages.success(request, 'Your account has been Modified!')
            return redirect ('profile')
        else :
            messages.error(request, 'Your account has not been Modified!')
            return redirect ('profile')


    def get (self, request) :
        form = UserUpdateForm(instance=request.user)
        return render(request, 'blog/profile.html', {'form': form})
    
@login_required
def logoutView(request) :
    logout(request)
    return redirect('register')



