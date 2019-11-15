from django.contrib import admin
from .models import Task, Todo


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ('title',)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('task', 'created',  'time', 'completed')
    list_editable = ('completed',)
