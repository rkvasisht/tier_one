from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Excercise, Workout, Profile




class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

  

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']

class ExcerciseForm(forms.ModelForm):
    class Meta:
        model = Excercise
        fields = ['name', 'weight', 'reps','sets','mins', 'secs',  'workout']
        help_text = {'name':'Please name the excercise', 'weight':'Please enter weight', 'reps':'Please enter reps', 'sets':'Please enter sets', 'mins':'Please enter minuetes of excercise', 'weight':'Please enter weight', 'reps':'Please enter reps', 'sets':'Please enter sets', 'secs':'Please enter seconds of excercise' }






