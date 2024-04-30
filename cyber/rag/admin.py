from django.contrib import admin
from .models import Pdf_Model

# Register your models here.

class Pdf_Admin(admin.ModelAdmin):
    list_display = ['file','user']

# Register your models here.

admin.site.register(Pdf_Model, Pdf_Admin)
