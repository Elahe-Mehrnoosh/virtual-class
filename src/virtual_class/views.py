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

def add_course_student(request):
    all_stu = Student.objects.all().order_by('national_id').reverse()
    if request.method == 'POST':
        add_new_reg_co = RegCourseStudent(request.POST)
        # if add_new_reg_co.is_valid():
        lesson = request.POST['lesson_name']
        found_course = Course.objects.values_list('id', flat=True).filter(name=lesson)
        sugg_cou_id = Suggested_course.objects.filter(course_no=found_course)
        temp = sugg_cou_id[0].id
        student_na_id = request.POST['student_id']
        Registered_course.objects.create(suggested_cou_id=temp, student_id=student_na_id)
    #     , grade='0'
    else:
        add_new_reg_co = RegCourseStudent()
    context = RequestContext(request, {
        'add_new_reg_co': add_new_reg_co
    })
    return render(request, 'add_course_student.html', context)

def add_student(request):
    if request.method == 'POST':
        add_stu = AddStudentForm(request.POST)
        student = Student()
        user = User()
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        student.national_id = request.POST['national_id']
        student.parent_name = request.POST['parent_name']
        student.tell_number = request.POST['tell_number']
        student.total_average = 0
        user.save()
        student.account_no = user
        student.save()
    return render(request, 'add_student.html')

def all_course(request):
    if request.method == 'POST':
        search_cou = SearchCourseForm()
        course_name = request.POST['course_name']
        if course_name != '':
            found_course = Course.objects.values_list('id', flat=True).filter(name=course_name)
            all_list = Suggested_course.objects.filter(course_no=found_course)
            if not all_list:
                all_list = Suggested_course.objects.all()
                # found_course = Course.objects.values_list('name', flat=True).filter(name=course_name)
        else:
            all_list = Suggested_course.objects.all()
    else:
        search_cou = SearchCourseForm()
        all_list = Suggested_course.objects.all()
    name_list = Course.objects.filter(id=all_list[0].course_no.id)
    number = len(all_list)
    for x in range(0, number):
        # name_list = Course.objects.filter(id=all_list[x].course_no.id)
        name_list = Course.objects.filter(id__in=all_list)
        # teacher_list = User.objects.filter(id=all_list[x].teacher.id)
    context = RequestContext(request, {
        'course_list': all_list,
        'name_list': name_list,
        # 'result_list': list(chain(all_list, name_list)),
        'result_list' : list(all_list) + list(name_list)



def all_courses(request):
    pass

def view_course(request):
    if request.method == 'POST':
        add_course = CourseForm(request.POST)
        course = Course()
        course.name = request.POST['course_name']
        course.save()
    course_list = Course.objects.all()
    return render(request, 'view_course.html', {'course_list': course_list})

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
            Suggested_course.objects.create(term_nu=sug_co_term_no, teacher=teacher, exam_date=sug_co_exam_date,course_no=course_id)
            return render(request, 'add_course.html', {'add_new_course': add_new_course})
    else:
        add_new_course = SuggestedCourse()
    return render(request, 'add_course.html', {'add_new_course': add_new_course})

def all_students(request):
    if request.method == 'POST':
        search_stu = SearchStudentForm()
        student_number = request.POST['student_number']
        if student_number != '':
            all_list = Student.objects.filter(national_id=student_number).order_by('national_id')
            if not all_list:
                all_list = Student.objects.all().order_by('national_id')
        else:
            all_list = Student.objects.all().order_by('national_id')
    else:
        search_stu = SearchStudentForm()
        all_list = Student.objects.all().order_by('national_id')
    number = len(all_list)
    for x in range(0, number):
        user_list = User.objects.filter(id=all_list[x].account_no_id)
    context = RequestContext(request, {
            'student_list': all_list,
            'user_list': user_list,
    })
    return render(request, 'all_students.html', {'search_stu': search_stu}, context)

def staff(request):
    return render(request, 'staff_main.html', {'today': date.today()})


def add_course_student(request):
    all_stu = Student.objects.all().order_by('national_id').reverse()
    # user_list = ''
    # sug_list = Suggested_course.objects.all()
    # name_list = ''
    # numbery = len(sug_list)
    # for y in range(0, numbery):
    #     tempy = Course.objects.filter(id=sug_list[y].course_no.id)
    #     name_list = list(chain(name_list, tempy))
    if request.method == 'POST':
        add_new_reg_co = RegCourseStudent(request.POST)
        # if add_new_reg_co.is_valid():
        lesson = request.POST['lesson_name']
        found_course = Course.objects.values_list('id', flat=True).filter(name=lesson)
        sugg_cou_id = Suggested_course.objects.filter(course_no=found_course)
        temp = sugg_cou_id[0].id
        student_na_id = request.POST['student_id']
        Registered_course.objects.create(suggested_cou_id = temp, student_id = student_na_id , grade=0)
    else:
        add_new_reg_co = RegCourseStudent()
    # numberx = len(all_stu)
    # for x in range(0, numberx):
    #     tempx = User.objects.filter(id=all_stu[x].account_no_id)
    #     user_list = list(chain(user_list, tempx))
    context = RequestContext(request, {
        # 'user_list' : user_list,
        # 'name_list' : name_list,
        # 'sug_list' : sug_list,
        'add_new_reg_co':add_new_reg_co
    })
    return render(request, 'add_course_student.html',context)

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
                current_user_id = request.user.id
                return redirect(staff)
    else:
        log_in_form = UserForm()
    return render(request, 'login.html', {'log_in_form': log_in_form})

def teacher_main(request):
    if request.method == 'POST':
        add_grade = GiveGrade(request.POST)
        lesson = request.POST['course_name']
        stu_grade = request.POST['grade']
        stu_na_id = request.POST['national_id']
        found_course = Course.objects.values_list('id').filter(name=lesson)
        sugg_cou_id = Suggested_course.objects.filter(course_no=found_course)
        temp = sugg_cou_id[0].id
        get_reg_co = Registered_course.objects.filter(suggested_cou = temp).filter(student = stu_na_id).update(grade = stu_grade)
    else:
        add_grade = GiveGrade()
    return render(request,'teacher_main.html', {'add_grade':add_grade})

def student_main(request):
    current_user_id = request.user.id
    student = Student.objects.values_list('national_id').filter(account_no=current_user_id)
    reg_all_courses = Registered_course.objects.filter(student=student)
    Reg_cou_sug_co_id = Registered_course.objects.filter(student=student)
    numberz = len(Reg_cou_sug_co_id)
    sug_cou=''
    found_course =''
    for z in range(0,numberz):
        # sug_cou = Suggested_course.objects.filter(id=Reg_cou_sug_co_id[z].id)
        found_course = list(Course.objects.filter(id=Suggested_course.objects.values_list('id').filter(id=Reg_cou_sug_co_id[z].id)))+list (found_course)
    # for w in range(0,numberz):
    #     found_course = chain(Course.objects.filter(id=sug_cou[w].id),found_course)
    context = RequestContext(request, {
        'reg_all_courses': reg_all_courses,
        'found_course' : found_course
    })
    return render(request,'student_main.html', context)
