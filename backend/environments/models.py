from django.db import models

from cloud_env_manager import settings


# Create your models here.

class Environment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='environments')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    environment_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.name} ({self.owner.username})"