from datetime import *

from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from src.virtual_class.models import *
from src.virtual_class.forms import *
from datetime import date


def all_students(request):
    return render(request, 'all_students.html')

def staff(request):
    return render(request, 'staff_main.html', {'today': date.today()})#today is used to show the today date in main page4

def filter_student_show(request):
    pass


def my_login(request):
    if request.method == 'POST':
        log_in_form = UserForm()
        username = request.POST['username']
        password = request.POST['password']
        this_user = User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(staff)
    else:
        log_in_form = UserForm()
    return render(request, 'login.html', {'log_in_form': log_in_form})
