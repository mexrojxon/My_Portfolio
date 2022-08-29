from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]
