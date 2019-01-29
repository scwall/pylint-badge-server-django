import jwt
from django.contrib.auth.models import User
from django.db import models

from pylint_badge_server.settings import SECRET_KEY
from users.storage import OverwriteStorage


class Repository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    public_token = models.CharField(max_length=255,null=True, blank=True)
    badge = models.ImageField(upload_to='pylint_badge',storage=OverwriteStorage(),null=True, blank=True)

    def __str__(self):

        return self.name

    def save(self, *args, **kwargs):
        super(Repository, self).save()
        self.public_token = jwt.encode({'user_id': self.user.id,'repository_id': self.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')
        super(Repository, self).save(*args, **kwargs)
