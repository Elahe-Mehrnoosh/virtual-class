from datetime import *

from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from src.virtual_class.models import *
from src.virtual_class.forms import *
from forms import *
from models import *

from datetime import date


def all_courses(request):
    pass

def add_course(request):
    if request.method == 'POST':
        add_new_course = SuggestedCourse(request.POST)
        if add_new_course.is_valid():
            sug_co_term_no = add_new_course.cleaned_data['term_no']
            tea_no = request.POST['teacher_national_id']
            teacher = Teacher.objects.get(national_id=tea_no)
            sug_co_exam_date = add_new_course.cleaned_data['exam_date']
            co_no = request.POST['course_no']
            course_id = Course.objects.get(name=co_no)
            # sug_co_co_no = add_new_course.cleaned_data[course_id]
            Suggested_course.objects.create(term_nu = sug_co_term_no, teacher = teacher, exam_date = sug_co_exam_date,course_no = course_id )
            # course_no = sug_co_co_no
            return render(request, 'add_course.html', {'add_new_course': add_new_course})
    else:
        add_new_course = SuggestedCourse()
    return render(request, 'add_course.html', {'add_new_course': add_new_course})

def all_students(request):
    if request.method == 'POST':
        search_stu = SearchStudentForm()
        student_number = request.POST['student_number']
        last_name = request.POST['last_name']
        if student_number != '':
            all_list = Student.objects.filter(national_id=student_number).order_by('national_id')
            if not all_list:
                all_list = Student.objects.all().order_by('national_id')
        else:
            # if last_name != '':
            #     user_list = User.objects.get(lastname__contains=last_name)
            #     all_list = Student.objects.filter(account_no_id=user_list.id)
            # else:
            #     all_list = Student.objects.all().order_by('national_id')
            all_list = Student.objects.all().order_by('national_id')
    else:
        search_stu = SearchStudentForm()
        all_list = Student.objects.all().order_by('national_id')
    number = len(all_list)
    for x in range(0, number):
        user_list = User.objects.filter(id=all_list[x].account_no_id)
        parent_list = User.objects.filter(id=all_list[x].parent_na_id_id)
    context = RequestContext(request, {
            'student_list': all_list,
            'user_list': user_list,
            'parent_list': parent_list
    })
    return render(request, 'all_students.html', {'search_stu': search_stu}, context)

def staff(request):
    return render(request, 'staff_main.html', {'today': date.today()})#today is used to show the today date in main page4

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
