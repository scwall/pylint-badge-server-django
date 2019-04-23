import jwt

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from pylint_badge_server.settings import SECRET_KEY
from users.storage import OverwriteStorage
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db.models import Q

class CustomUserManager(UserManager):

    def get_by_natural_key(self, username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username}) |
            Q(**{self.model.EMAIL_FIELD: username})
        )
class CustomUser(AbstractUser):
    objects = CustomUserManager()
    def __str__(self):
        return self.email


class Repository(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    public_token = models.CharField(max_length=255, null=True, blank=True)
    badge = models.ImageField(upload_to='pylint_badge', storage=OverwriteStorage(), null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Repository, self).save()
        self.public_token = jwt.encode({'user_id': self.user.id, 'repository_id': self.id}, SECRET_KEY,
                                       algorithm='HS256').decode('utf-8')
        super(Repository, self).save(*args, **kwargs)

class Report(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    number_report = models.IntegerField()
    score = models.IntegerField()

class ReportDetail(models.Model):
    line = models.IntegerField()
    path = models.CharField(max_length=255)
    column = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    obj = models.CharField(max_length=255, null=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    pep8_type = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
