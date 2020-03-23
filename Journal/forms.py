from django import forms
from .models import Day, Lesson, SchoolClass, Schedule, UserImage, Teacher, HomeWork
from django.contrib.auth.models import User, Group

lessons = Lesson.objects.all()
lessons_choices = [tuple([l, l]) for l in lessons]

groups = Group.objects.all()
groups_choices = [tuple([g, g]) for g in groups]

users = User.objects.all()

teachers = Teacher.objects.all()

teachers_choices = []

schoolclasses = SchoolClass.objects.all()
schoolclass_choices = [tuple([s, s]) for s in schoolclasses]

student = Group.objects.get(name='Student')


class AuthForms(forms.Form):
    username = forms.CharField(label='Username:', max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password:', max_length=200, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserAddForms(forms.ModelForm):
    group = forms.CharField(label='Group:',
                            widget=forms.Select(choices=groups_choices, attrs={'class': 'form-control', }))

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class UserEditForms(forms.Form):
    username = forms.CharField(label='Username:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First name:',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(label='Last name:',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    email = forms.CharField(label='Email:',
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True}))
    group = forms.CharField(label='Group:',
                            widget=forms.Select(choices=groups_choices, attrs={'class': 'form-control', }))


class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']


class ClassAddForms(forms.ModelForm):
    class Meta:
        model = SchoolClass
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ClassStudentsAddForms(forms.Form):
    students = forms.CharField(label='Select', widget=forms.SelectMultiple(
        choices=[tuple([u.id, u.first_name + ' ' + u.last_name]) for u in User.objects.filter(groups=student).filter
        (schoolclass=None).order_by('first_name')]))


class ScheduleAddForms(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['day', 'lesson', 'lessonteacher', 'date', 'start', 'end']
        widgets = {
            'day': forms.Select(choices=Day.objects.all(), attrs={'class': 'form-control'}),
            'lesson': forms.Select(choices=Lesson.objects.all(), attrs={'class': 'form-control'}),
            'lessonteacher': forms.Select(choices=teachers, attrs={'class': 'form-control'}),
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control'}),
            'start': forms.TimeInput(attrs={'class': 'form-control'}),
            'end': forms.TimeInput(attrs={'class': 'form-control'})
        }


class LessonAddForms(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class HomeWorkForms(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = ['schedule', 'text']
        widgets = {
            'schedule': forms.Select(attrs={'class': 'form-control'}),
        }
