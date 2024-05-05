from django.contrib import admin

from .models import Pdf_Model, Questions

# Register your models here.
admin.site.site_title = "Cyber site admin"
admin.site.site_header = "Cyber administration"
admin.site.index_title = "Site administration"


class Pdf_Admin(admin.ModelAdmin):
    list_display = ['id', 'file', 'user']


admin.site.register(Pdf_Model, Pdf_Admin)


@admin.register(Questions)
class ChatQuestion(admin.ModelAdmin):
    list_display = ('id', 'question', 'created_at')
