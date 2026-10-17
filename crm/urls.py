from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from users.views import StudentAPIViewSet

router = DefaultRouter()
router.register('students', StudentAPIViewSet, basename='student-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('users.urls')),

    path('api/', include(router.urls)),
    path('api/', include('academics.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )