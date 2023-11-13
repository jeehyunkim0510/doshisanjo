from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Guest(models.Model):
    writer = models.CharField(max_length=50)
    content = models.TextField(max_length=500, null=True)
    created_at = models.DateField(null=True)

    def __str__(self):
        return self.writer