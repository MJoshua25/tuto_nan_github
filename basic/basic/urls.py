from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#Je ne vois pas d'applications dans ton projet
