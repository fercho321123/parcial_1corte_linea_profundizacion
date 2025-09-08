from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Libro , Miembro, Autor, Editorial,Prestamo
from .serializers import LibroSerializer,MiembroSerializer,AutorSerializer,EditorialSerializer,PrestamoSerializer

# ----------------- CRUD AUTORES -----------------

# Listar todos los autores
class AutorList(generics.ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get(self, request):
        autores = Autor.objects.all()
        if not autores:
            raise NotFound("No se encontraron autores.")
        serializer = self.get_serializer(autores, many=True)
        return Response(
            {'success': True, 'detail': 'Listado de autores', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Crear autor
class CrearAutor(generics.CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Autor creado con éxito', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )

# Consultar un autor por ID
class AutorDetail(generics.RetrieveAPIView):
    serializer_class = AutorSerializer

    def get(self, request, pk):
        autor = Autor.objects.filter(pk=pk).first()
        if not autor:
            return Response(
                {'success': False, 'detail': 'Autor no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(autor)
        return Response(
            {'success': True, 'detail': 'Autor encontrado', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Actualizar autor
class ActualizarAutor(generics.UpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def put(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        serializer = self.get_serializer(autor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Autor actualizado con éxito', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Eliminar autor
class BorrarAutor(generics.DestroyAPIView):
    serializer_class = AutorSerializer

    def delete(self, request, pk):
        autor = Autor.objects.filter(pk=pk).first()
        if not autor:
            return Response(
                {'success': False, 'detail': 'Autor no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        autor.delete()
        return Response(
            {'success': True, 'detail': f'Autor con ID {pk} eliminado con éxito'},
            status=status.HTTP_200_OK
        )


# ----------------- CRUD EDITORIALES -----------------

# Listar todas las editoriales
class EditorialList(generics.ListAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def get(self, request):
        editoriales = Editorial.objects.all()
        if not editoriales:
            raise NotFound("No se encontraron editoriales.")
        serializer = self.get_serializer(editoriales, many=True)
        return Response(
            {'success': True, 'detail': 'Listado de editoriales', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Crear editorial
class CrearEditorial(generics.CreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Editorial creada con éxito', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )

# Consultar una editorial por ID
class EditorialDetail(generics.RetrieveAPIView):
    serializer_class = EditorialSerializer

    def get(self, request, pk):
        editorial = Editorial.objects.filter(pk=pk).first()
        if not editorial:
            return Response(
                {'success': False, 'detail': 'Editorial no encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(editorial)
        return Response(
            {'success': True, 'detail': 'Editorial encontrada', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Actualizar editorial
class ActualizarEditorial(generics.UpdateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def put(self, request, pk):
        editorial = get_object_or_404(Editorial, pk=pk)
        serializer = self.get_serializer(editorial, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Editorial actualizada con éxito', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Eliminar editorial
class BorrarEditorial(generics.DestroyAPIView):
    serializer_class = EditorialSerializer

    def delete(self, request, pk):
        editorial = Editorial.objects.filter(pk=pk).first()
        if not editorial:
            return Response(
                {'success': False, 'detail': 'Editorial no encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )
        editorial.delete()
        return Response(
            {'success': True, 'detail': f'Editorial con ID {pk} eliminada con éxito'},
            status=status.HTTP_200_OK
        )


# ----------------- FILTROS DE AUTORES -----------------

# Consultar todos los autores
class ConsultarAutores(generics.ListAPIView):
    serializer_class = AutorSerializer

    def get(self, request):
        autores = Autor.objects.all()
        if not autores:
            return Response(
                {'success': False, 'detail': 'No se encontraron autores'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(autores, many=True)
        return Response(
            {'success': True, 'detail': 'Listado de autores', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Consultar autor por ID (filtro)
class ConsultarAutorPorID(generics.RetrieveAPIView):
    serializer_class = AutorSerializer

    def get(self, request, autor_id):
        autor = Autor.objects.filter(pk=autor_id).first()
        if not autor:
            return Response(
                {'success': False, 'detail': 'Autor no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(autor)
        return Response(
            {'success': True, 'detail': f'Autor con ID {autor_id}', 'data': serializer.data},
            status=status.HTTP_200_OK
        )
