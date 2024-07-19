from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.title
    
class Task(models.Model):
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)