from django.contrib import admin
from . import models
# Register your models here.
class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember
    
admin.site.register(models.Group)