from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=500)
    event_location = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    image = models.FileField(upload_to='event_images/')
    likes = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.event_name
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)