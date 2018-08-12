from django.urls import path
from . import views



urlpatterns = [
    
    
    path('', views.profile, name='profile'),
    path('post_workout/', views.post_workout, name='post_workout'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('workouts/', views.home, name='home'),
    path('workouts/editworkout/<int:workout_id>/', views.editworkout, name='editworkout'),
    path('logout/', views.logout_view, name='logout'),
    path('workouts/editworkout/<int:workout_id>/post_excercise', views.post_excercise, name='post_excercise')

    
    


   
]