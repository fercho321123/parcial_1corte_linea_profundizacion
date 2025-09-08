from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, EditorialViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet, basename='autor')
router.register(r'editoriales', EditorialViewSet, basename='editorial')

urlpatterns = [
    path('', include(router.urls)),
]