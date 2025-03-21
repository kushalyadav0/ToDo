from django.db import models

# Create your models here.

class Tasks(models.Model):
    task_name = models.CharField(max_length=20)
    complete = models.BooleanField(default=False)
    task_description = models.TextField(max_length=100,)
    date_added = models.DateField(auto_now_add=True)
    deadline = models.TimeField(blank=True, null=True, )

    def __str__(self):
        return self.task_name