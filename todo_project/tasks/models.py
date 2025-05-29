from operator import truediv
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class complete_choices(models.TextChoices):
    YES = 'yes','Yes'
    NO = 'no', 'No'

class Tasks(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    task_name = models.CharField(max_length=20)
    task_description = models.TextField(max_length=100,)
    date_added = models.DateField(auto_now_add=True)
    deadline = models.TimeField(blank=True, null=True,)
    complete = models.CharField(max_length=3,choices=complete_choices,default=complete_choices.NO)


    def __str__(self):
        return self.task_name