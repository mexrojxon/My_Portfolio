from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('about.urls', namespace='about')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
from django.conf.urls import handler404

handler404 = 'about.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
