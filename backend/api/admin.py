from django.contrib import admin
from  api import models
# Register your models here.
admin.site.register(models.Classroom)
admin.site.register(models.ClassSlot)
admin.site.register(models.Faculty)
admin.site.register(models.Section)
admin.site.register(models.Course)