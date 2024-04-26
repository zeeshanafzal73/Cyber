from django.urls import path

from . import views

app_name = 'chatbot'
urlpatterns = [
    path('index/', views.index, name='index')
]
