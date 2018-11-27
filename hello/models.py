from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
<<<<<<< HEAD

class Shift(models.Model):
    weekday = models.CharField(max_length=9)
    start_time = models.CharField(max_length=5)
    end_time = models.CharField(max_length=5)
    def __str__(self):
        return self.weekday + ': ' + self.start_time + '-' + self.end_time

class Schedule(models.Model):
    user = models.CharField(max_length=30)
    shifts = models.ManyToManyField(Shift)
    def __str__(self):
        return self.user
=======
>>>>>>> 8bf5e16791af5989c93baf0971df91b517c89780
