from django.urls import path
from core import views
from service1 import settings

urlpatterns = [
    path(settings.TELEBOT_API_TOKEN + "/", views.pull_messages),
    path('debug', views.view_data, name='view_data'),
]
