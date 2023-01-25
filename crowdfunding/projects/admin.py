from django.contrib import admin
from .models import Project, Pledge

# # Register your models here.

# -----------------------
# ADMIN BLOCK
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','owner', 'goal', 'is_open', 'date_created')

admin.site.register(Project, ProjectAdmin)


class PledgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'project','supporter', 'amount', 'anonymous')

admin.site.register(Pledge, PledgeAdmin)