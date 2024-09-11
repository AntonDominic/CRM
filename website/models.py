from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_time = models.DateTimeField()
    
    def __str__(self):
        return(f"{self.title} {self.description}")  

