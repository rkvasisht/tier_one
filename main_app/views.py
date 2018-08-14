from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm, WorkoutForm, ExcerciseForm
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import requests
from .models import Excercise, Workout, Profile
from django.utils import timezone

# Create your views here.


def profile(request):
    print(request.user.id)
    userlogged = User.objects.get(id = int(request.user.id))
    workout = Workout.objects.all()
    users = User.objects.all()
    profiles = Profile.objects.all()
    userinfo = userlogged.profile
    workoutsforuser = userinfo.workouts.all()
    print(workoutsforuser)
    return render(request, 'profile.html',{'workouts': workout, 'users': users, 'profiles':profiles, 'workoutsforuser':workoutsforuser})



def workoutlanding(request):
    workouts = Workout.objects.all()
    form = WorkoutForm()
    return render(request, 'workouts/workoutlanding.html',{'workouts': workouts, 'form': form,})

def editworkout(request, workout_id):
    workout_obj = get_object_or_404(Workout, id=workout_id)
    workouts = Workout.objects.all()
    excercisesinworkout = workout_obj.excercise_set.all()
    listofexcercises = excercisesinworkout.all()
    print(excercisesinworkout, )
    form = ExcerciseForm()
    return render(request, 'workouts/editworkout.html',{'workouts': workouts, 'form': form, 'excercisesinworkout': excercisesinworkout, 'listofexcercises':listofexcercises})
    
def clientviewworkout(request, workout_id):
    print(workout_id)
    workout_obj = get_object_or_404(Workout, id=workout_id)
    workouts = Workout.objects.all()
    excercisesinworkout = workout_obj.excercise_set.all()
    listofexcercises = excercisesinworkout.all()
    print(listofexcercises)
    return render(request, 'workouts/clientworkouts.html',{'workouts': workouts,  'excercisesinworkout': excercisesinworkout, 'listofexcercises':listofexcercises})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("Account disabled")
                    return HttpResponseRedirect('/login')
            else:
                print("Username and/or password is incorrect")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def post_workout(request):
    form = WorkoutForm(request.POST)
    if form.is_valid():
        workout = form.save(commit=False)
        workout.pub_date = timezone.now()
        workout.save()
        return HttpResponseRedirect('/workouts')
    else:
        return HttpResponse('The form broke!')


def post_excercise(request, workout_id):
    print(workout_id)
    form = ExcerciseForm(request.POST)
    if form.is_valid():
        excercise = form.save(commit=False)
        excercise.save()
        return HttpResponseRedirect('/workouts')
    else:
        return HttpResponse('The form broke!')

def add_workouts_to_user(request):
    user_id = request.POST.get('user_id', None)
    workout_id = request.POST.get('workout_id', None)
    if user_id and workout_id:
        user = User.objects.get(id=int(user_id))
        profile = user.profile
        workout = Workout.objects.get(id = int(workout_id))
        profile.workouts.add(workout)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('The form broke!')



def workoutsforclients(request, user_id):
    print(user_id)
    user = User.objects.get(id=int(user_id))
    profilenumber = user.profile.id
    profile = user.profile
    workout = profile.workouts.get(profile_id=int(profilenumber))
    print(workout)
    return render(request, 'workouts/workoutsforclients.html')











  






