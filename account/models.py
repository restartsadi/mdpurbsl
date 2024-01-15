from django.db import models
from django.utils import timezone

# Create your models here.
class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    date_created = models.DateTimeField("Date Created",default=timezone.now)
    
    def __str__(self):
        return self.email

class CommentPerson(models.Model):
        txt = models.CharField(max_length=30)
        email = models.EmailField(unique=True, max_length=100)
        mssg = models.TextField(max_length=300)
        
        def __str__(self):
             return self.email