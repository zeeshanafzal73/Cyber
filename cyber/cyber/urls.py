from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cyberapp.urls')),
    path('', include('rag.urls')),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('admin/', admin.site.urls),
]
