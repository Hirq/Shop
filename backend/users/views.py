from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from .forms import UsersLoginForm, UsersRegisterForm, UserShipmentForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import UserAccount

def login_view(request):
    if request.method == "POST":
        form = UsersLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect('/')
    else:
        form = UsersLoginForm()
    return render(request, 'users/form.html', {
            'form' : form,
            'title' : "Login",
        })


def register_view(request):
    form = UsersRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password = password)
        login(request, new_user)
        return redirect("/")
    return render(request, "users/form.html", {
        "title" : "Register",
        "form" : form,
    })

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def account_view(request):
    if request.method == "POST":
        form = UserShipmentForm(request.POST, instance=request.user)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('/')
    else:
        form = UserShipmentForm(instance=request.user)

    return render(request, 'users/account_update_form.html', {'form': form})
