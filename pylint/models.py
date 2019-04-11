from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from users.models import Repository, Reports


class ErrorPep8(models.Model):
    message = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    error = GenericRelation(Reports)
    def __str__(self):
        return self.message


class WarningPep8(models.Model):
    message = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    warning = GenericRelation(Reports)
    def __str__(self):
        return self.message


class RefactorPep8(models.Model):
    message = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    refactor = GenericRelation(Reports)
    def __str__(self):
        return self.message


class ConventionPep8(models.Model):
    message = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    convention = GenericRelation(Reports)
    def __str__(self):
        return self.message
