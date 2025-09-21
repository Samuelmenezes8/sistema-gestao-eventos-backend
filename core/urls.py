from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from eventos.views import EventoViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet, basename='evento')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]