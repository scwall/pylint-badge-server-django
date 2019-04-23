from django.contrib import admin

# Register your models here.
from users.models import Repository, Report, ReportDetail

admin.site.register(Repository)
admin.site.register(Report)
admin.site.register(ReportDetail)