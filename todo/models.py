from django.db import models

# Create your models here.

class AddTodo(models.Model):
    todo = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo