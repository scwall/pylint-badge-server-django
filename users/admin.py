from django.contrib import admin

# Register your models here.
from users.models import Repository, Reports

admin.site.register(Repository)
admin.site.register(Reports)