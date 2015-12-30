from datetime import *

from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from src.virtual_class.models import *
from src.virtual_class.forms import *


def open_login_page(request):
    current_user = request.user.username
    user = User.objects.get(username=current_user)
    # context = RequestContext(request, {
    #      'paper_list': all_list,
    # })
    return render(request, 'index.html')  #, context

def my_login(request):
    if request.method == 'POST':
        log_in_form = UserForm()
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return redirect(open_login_page)
                return render(request, 'index.html')
    else:
        log_in_form = UserForm()
    return render(request, 'login.html', {'log_in_form': log_in_form})

def user_logout(request):
    logout(request)
    return redirect(my_login)
