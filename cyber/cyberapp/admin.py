from django.contrib import admin

# from .models import Document


# Register your models here.
admin.site.site_title = "Cyber site admin"
admin.site.site_header = "Cyber administration"
admin.site.index_title = "Site administration"

# @admin.register(Document)
# class CyberDocument(admin.ModelAdmin):
#     list_display = ('id', 'pdf', 'uploaded_at')
