
from django.db import models
from django.utils import timezone

class Asset(models.Model):
    name = models.CharField(max_length=100)
    service_time = models.DateTimeField()
    expiration_time = models.DateTimeField()
    serviced = models.BooleanField(default=False)

class Notification(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)  # service or expiration
    created_at = models.DateTimeField(auto_now_add=True)

class Violation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
