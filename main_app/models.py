from django.db import models

# Create your models here.


class Workout(models.Model):
    name = models.CharField(max_length=100, default=None)
    pub_date = models.DateTimeField('date published')

def __str__(self):
        return self.name


class Excercise(models.Model):
    name = models.CharField(max_length=100, default=None)
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    mins = models.IntegerField(default=0)
    secs = models.IntegerField(default=0)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)





    

