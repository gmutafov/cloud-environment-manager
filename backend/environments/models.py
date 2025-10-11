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


class ActivityLog(models.Model):
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, related_name='activities')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.environment.name} - {self.action} by {self.user or 'System'}"
