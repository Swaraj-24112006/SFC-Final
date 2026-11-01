from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from redflag.views import RedFlagListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    re_path(r'^api/redflags/?$', RedFlagListCreateView.as_view(), name='redflag-list-root'),
    re_path(r'^api/redflags/', include('redflag.urls')),
]
