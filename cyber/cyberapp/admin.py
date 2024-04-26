from django.contrib import admin

from .models import Document


# Register your models here.

@admin.register(Document)
class CyberDocument(admin.ModelAdmin):
    list_display = ('id', 'pdf', 'uploaded_at')
