from django.db import models

# Create your models here.
# class Users
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    def __unicode__(self):
        return self.username