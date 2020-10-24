from django.db import models

# Create your models here.
class Userlogin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)