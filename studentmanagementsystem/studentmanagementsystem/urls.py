
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('management.urls')),
    path('management/', include('management.urls_api')),
]
