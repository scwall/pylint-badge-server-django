from django.contrib import admin

# Register your models here.
from pylint.models import Error,Warning,Refactor,Convention

admin.site.register(Error)
admin.site.register(Warning)
admin.site.register(Refactor)
admin.site.register(Convention)