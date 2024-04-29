from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'cyberapp'
urlpatterns = [
                  path('signup/', views.signup, name='signup'),
                  path('login/', views.login, name='login'),
                  path('forgot_password/', views.forget_password, name='forget_password'),
                  path('home/', views.home, name='home'),
                  path('upload/', views.upload_file, name='upload_document'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
