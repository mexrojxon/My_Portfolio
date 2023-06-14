from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogListView, name='list'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('<slug:slug>/comment/', BlogDetailView.post_comment, name='comment')
]
