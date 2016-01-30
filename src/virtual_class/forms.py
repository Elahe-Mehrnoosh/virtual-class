from django import forms
from django.contrib.auth.models import User
from Choices import *
from models import Course

#
# choices = [course.name for course in Course.objects.all()]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'password')

class SearchStudentForm(forms.Form):
    student_number = forms.IntegerField(label='student_number',widget=forms.NumberInput(attrs={'class': 'form-control inner-search-by'}))
    last_name = forms.CharField(label='last_name', widget=forms.TextInput(attrs={'class': 'form-control inner-search-by'}))
    # sort = forms.ChoiceField(choices=sorts, widget=forms.RadioSelect(attrs={'class': 'form-control inner-search-by'}))

class SuggestedCourse(forms.Form):
    term_no = forms.IntegerField(label='term_no', widget=forms.NumberInput(attrs={'class': 'form-control inner-search-by'}))
    teacher_national_id = forms.IntegerField(label='teacher_national_id', widget=forms.NumberInput(attrs={'class': 'form-control inner-search-by'}))
    exam_date = forms.DateField(label='exam_date', widget=forms.DateInput(attrs={'class': 'form-control inner-search-by'}))
    # course_no = forms.ModelMultipleChoiceField(queryset=Course.objects.all().values_list('name'), label='course_name',
    #                                            widget=forms.Select(attrs={'class': 'form-control inner-search-by'}))
    course_no = forms.CharField(label='course_name', widget=forms.TextInput(attrs={'class': 'form-control inner-search-by'}))

class SearchCourseForm(forms.Form):
    course_name = forms.CharField(label='term_no', widget=forms.TextInput(attrs={'class': 'form-control inner-search-by'}))