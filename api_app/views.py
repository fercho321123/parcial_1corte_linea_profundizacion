
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import (
AutorSerializer, EditorialSerializer, LibroSerializer,
MiembroSerializer, PrestamoSerializer
)

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    
class AutorViewSet(BaseViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ['nombre', 'apellido', 'biografia']
    ordering_fields = ['nombre', 'apellido', 'id']




class EditorialViewSet(BaseViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    search_fields = ['nombre', 'direccion', 'telefono']
    ordering_fields = ['nombre', 'id']