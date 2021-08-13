from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Task(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'

