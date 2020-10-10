from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('shop.urls', namespace='shop')),

    # Api Url
    path('api/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
]