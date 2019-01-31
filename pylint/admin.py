from django.contrib import admin

# Register your models here.
from pylint.models import ErrorPep8,WarningPep8,RefactorPep8,ConventionPep8

admin.site.register(ErrorPep8)
admin.site.register(WarningPep8)
admin.site.register(RefactorPep8)
admin.site.register(ConventionPep8)