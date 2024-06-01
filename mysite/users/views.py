from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from users.forms import AuthForm
# Create your views here.

def login_view(request):
    if request.method=='GET':
       form = AuthForm()
       return(render(request, 'login.html',dict(form = form)))
    elif request.method=='POST':
        print(request.POST)
        form = AuthForm(request.POST)
        if form.is_valid():
            usr = form.cleaned_data['name']
            pwd = form.cleaned_data['password']
            user = authenticate(request,username = usr,password = pwd)
            if user is not None:
                login(request,user)
                return redirect('/admin')


def register_view(request):
    if request.method=='GET':
       form = AuthForm()
       return(render(request, 'login.html',dict(form = form)))
    elif request.method=='POST':
        print(request.POST)
        form = AuthForm(request.POST)
        if form.is_valid():
            usr = form.cleaned_data['name']
            pwd = form.cleaned_data['password']
            User = get_user_model()
            user = User.objects.filter(username = usr)

            if not user.exists():
                user = User(username = usr)
                user.set_password(pwd)
                user.save()
                login(request,user)
                return redirect('/admin')



























































































