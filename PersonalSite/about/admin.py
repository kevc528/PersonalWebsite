from django.contrib import admin
from projects.models import ProjectCategory, Comment, Project

# Register your models here.
admin.site.register(ProjectCategory)
admin.site.register(Comment)
admin.site.register(Project)