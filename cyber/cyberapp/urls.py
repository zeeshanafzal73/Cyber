from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cyberapp'
urlpatterns = [
                  path('signup/', views.user_signup, name='signup'),
                  path('login/', views.user_login, name='login'),
                  path('change_password/', views.change_password, name='change_password'),
                  path('forgot_password/', views.forget_password, name='forgot_password'),
                  path('success/', views.success, name='success'),
                  path('home/', views.home, name='home_user'),
                  path('upload/', views.upload_file, name='upload_document'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
