
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

from .views import api_root_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root_view),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include("api.urls"), name='api-root'),
] + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)