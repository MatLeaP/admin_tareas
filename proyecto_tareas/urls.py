from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from app_tareas.views import Error404View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_tareas.urls')),
]

handler404 = Error404View.as_view()

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)