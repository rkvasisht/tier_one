from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

 


class Workout(models.Model):
    name = models.CharField(max_length=100, default=None)
    pub_date = models.DateTimeField('date published')
  


class Excercise(models.Model):
    name = models.CharField(max_length=100, default=None)
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    mins = models.IntegerField(default=0)
    secs = models.IntegerField(default=0)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    workouts = models.ManyToManyField(Workout)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class PushedWorkout(models.Model):
    workouts = models.ManyToManyField(Workout)
    users = models.ManyToManyField(User)
    pub_date = models.DateTimeField(default=timezone.now, blank=True)
    inclass = models.BooleanField(default=True)
    assigned = models.BooleanField(default=False)



def __str__(self):
        return self.name


    

