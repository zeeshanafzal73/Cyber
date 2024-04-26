from django.contrib import admin

from .models import Questions


# Register your models here.
@admin.register(Questions)
class ChatQuestion(admin.ModelAdmin):
    list_display = ('id', 'question', 'created_at')
