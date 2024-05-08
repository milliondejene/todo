from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)  # Use timezone.now() as the default value

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task'
        app_label = 'todoApp'  # Replace 'todoApp' with the name of your Django app
