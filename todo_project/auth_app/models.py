from django.db import models

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length=12)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.username