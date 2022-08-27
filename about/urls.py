from django.urls import path
from .views import *

app_name = 'about'

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('contact/',ContactView.as_view(), name='contact'),
]