from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)               # task title
    description = models.TextField(blank=True, null=True)  # task description
    created_at = models.DateTimeField(auto_now_add=True)   # auto timestamp when created
    completed = models.BooleanField(default=False)        # task completion status

    def __str__(self):
        return self.title
