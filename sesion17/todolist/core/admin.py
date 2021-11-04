from django.contrib import admin
from core.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'finished')
    list_filter = ('due_date', 'finished')
    search_fields = ['title']
    ordering = ('due_date',)
    fields = ('title', 'description', ('due_date', 'finished'), 'attachments')

admin.site.register(Task, TaskAdmin)