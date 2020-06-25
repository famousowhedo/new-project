from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField( max_length=30, choices=(
        ('male','Male'),
        ('famale', 'Female'),
 
    ))
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("home", kwargs={"pk": self.pk})
    
            