# rag/urls


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('chat/', views.chatbot_response, name='chat'),
                  path('staffs/', views.staff_chatbot, name='staffs'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
