from django.contrib import admin
from django.urls import path, include
from email_service.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('email_service.urls')),
    path('', index, name='index'),
]
