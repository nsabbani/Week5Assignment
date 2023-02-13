from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pollsApp/', include('pollsApp.urls')),
    path('admin/', admin.site.urls),
]
