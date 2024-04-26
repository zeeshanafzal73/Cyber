from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('cyber/', include('cyberapp.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('admin/', admin.site.urls),
]
