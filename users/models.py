from django.contrib.auth.models import User
from django.db import models

class Repository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    badge = models.ImageField(upload_to='pylint_badge')

    def __str__(self):
        return self.name


