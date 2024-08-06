from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailAccountViewSet, EmailMessageViewSet


router = DefaultRouter()
router.register(r'accounts', EmailAccountViewSet)
router.register(r'messages', EmailMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]