from django.urls import path
from .views import *

urlpatterns = [
    path('', api_home, name='home'),
    path('about/', api_about, name='about')
]