from django import forms
from django.contrib.auth.models import User
from Choices import *

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
