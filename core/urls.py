from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'pages.views.handle_not_found'
