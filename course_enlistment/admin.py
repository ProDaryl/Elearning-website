from django.contrib import admin
from .models import Course, Module, Content, UserProgress

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    pass
