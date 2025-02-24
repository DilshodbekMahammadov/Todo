from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOISES = (
        ('to do', 'to do'),
        ('in progress', 'in progress'),
        ('done', 'done'),
    )
    title = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default='to do')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

