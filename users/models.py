from django.db import models


# Create your models here.
class User(models.Model):
    """
    Model for the user
    """
    name = models.CharField()


class Repository(models.Model):
    name = models.CharField()
    token = models.CharField()
    badge = models.ImageField(upload_to='pylint_badge')

class Error(models.Model):
    error = models.ForeignKey(User, on_delete=models.CASCADE)


class Warning(models.Model):
    warning = models.ForeignKey(User, on_delete=models.CASCADE)


class Refactor(models.Model):
    refactor = models.ForeignKey(User, on_delete=models.CASCADE)


class Convention(models.Model):
    convention = models.ForeignKey(User, on_delete=models.CASCADE)
