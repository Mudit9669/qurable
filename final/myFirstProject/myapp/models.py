from django.db import models
from django.forms import IntegerField
# Create your models here.

class Snippet(models.Model):
    name = models.CharField( max_length=100)
    email = models.CharField(default=False, max_length=254)
    p_num = models.CharField(default=False, max_length = 10)
    body = models.TextField()
    
    def __str__(self):
        return self.name + self.email + self.p_num + self.body
