from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'cyberapp'
urlpatterns = [
                  path('upload/', views.upload_file, name='upload_document'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
