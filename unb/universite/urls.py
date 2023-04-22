from django.urls import path, include
from .views import *


urlpatterns = [
    path("", Home_PageView, name='home')
]
