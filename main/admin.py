from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from unfold.admin import ModelAdmin


from . import models

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Discussion)
admin.site.register(models.GeneralInfo)
admin.site.register(models.Document)
admin.site.register(models.Evaluation)
admin.site.register(models.AssignedEvaluation)
admin.site.register(models.Aspect)
admin.site.register(models.Question)
admin.site.register(models.SubQuestion)
admin.site.register(models.EvaluatorResponse)
admin.site.register(models.Answer)
admin.site.register(models.QuestionOption)
admin.site.register(models.FileAttachment)
admin.site.register(models.EvaluatorOption)
