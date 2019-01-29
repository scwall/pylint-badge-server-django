import os

import jwt
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from pylint_badge_server.settings import SECRET_KEY


class Repository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    public_token = models.CharField(max_length=255,null=True, blank=True)
    badge = models.ImageField(upload_to='pylint_badge',null=True, blank=True)

    def __str__(self):

        return self.name

    def save(self, *args, **kwargs):
        super(Repository, self).save()
        self.public_token = jwt.encode({'user_id': self.user.id,'repository_id': self.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')
        super(Repository, self).save(*args, **kwargs)


@receiver(models.signals.pre_save, sender=Repository)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).badge
    except sender.DoesNotExist:
        return False
    try:
        new_file = instance.badge
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except:
        pass
