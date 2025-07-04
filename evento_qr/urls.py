from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('invitados.urls')),
    
    # PWA files
    path('manifest.json', TemplateView.as_view(
        template_name='pwa/manifest.json', 
        content_type='application/json'
    )),
    path('sw.js', TemplateView.as_view(
        template_name='pwa/sw.js', 
        content_type='application/javascript'
    )),
    path('offline.html', TemplateView.as_view(template_name='pwa/offline.html')),
]

# Servir archivos media y static en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])