from django import forms
from .models import Day, Lesson, SchoolClass
from django.contrib.auth.models import User, Group

days = Day.objects.all()
days_choices = [tuple([d, d]) for d in days]

lessons = Lesson.objects.all()
lessons_choices = [tuple([l, l]) for l in lessons]

groups = Group.objects.all()
groups_choices = [tuple([g, g]) for g in groups]

users = User.objects.all()
teacher = Group.objects.filter(name='Teacher').first()
teachers = [user for user in users if user.groups.first() == teacher]
teachers_choices = [tuple([t.first_name + ' ' + t.last_name, t.first_name]) for t in teachers]


class AuthForms(forms.Form):
    username = forms.CharField(label='Username:', max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password:', max_length=200, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserAddForms(forms.ModelForm):
    group = forms.CharField(label='Group:', widget=forms.Select(choices=groups_choices, attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ClassAddForms(forms.ModelForm):
    class Meta:
        model = SchoolClass
        fields = ['title', 'teacher']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher': forms.Select(choices=teachers_choices, attrs={'class': 'form-control'})
        }


class ScheduleAddForms(forms.Form):
    day_week = forms.CharField(label='Day of the week:', widget=forms.Select(choices=days_choices))
    lesson = forms.CharField(label='Lesson:', widget=forms.Select(choices=lessons_choices, attrs={'format': '%Y-%m-%d'})
                             )

    lesson_date = forms.DateField(label='Lesson date:', widget=forms.SelectDateWidget)

    lesson_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    lesson_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
