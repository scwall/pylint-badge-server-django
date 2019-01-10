from django.db import models


# Create your models here.
class User(models.Model):
    """
    Model for the user
    """
    name = models.CharField(max_length=30)



class Repository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    badge = models.ImageField(upload_to='pylint_badge')


class Error(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    line = models.IntegerField()
    description = models.CharField(max_length=255)


class Warning(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    line = models.IntegerField()
    description = models.CharField(max_length=255)

class Refactor(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    line = models.IntegerField()
    description = models.CharField(max_length=255)
class Convention(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    line = models.IntegerField()
    description = models.CharField(max_length=255)