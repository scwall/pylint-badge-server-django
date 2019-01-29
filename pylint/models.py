from django.db import models
from users.models import Repository
class Score(models.Model):
    score = models.IntegerField()
class Error(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    line = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Warning(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    line = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Refactor(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    line = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Convention(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    line = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
