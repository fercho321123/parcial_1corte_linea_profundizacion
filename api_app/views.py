from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Libro , Miembro, Autor, Editorial,Prestamo
from .serializers import LibroSerializer,MiembroSerializer,AutorSerializer,EditorialSerializer,PrestamoSerializer






































































































































































































# ----------------- CRUD LIBROS -----------------

# Listar todos los libros
class LibroList(generics.ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request):
        libros = Libro.objects.all()
        if not libros:
            raise NotFound("No se encontraron libros.")
        serializer = self.get_serializer(libros, many=True)
        return Response(
            {'success': True, 'detail': 'Listado de libros', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Crear libro
class CrearLibro(generics.CreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Libro creado con éxito', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )

# Consultar un libro por ID
class LibroDetail(generics.RetrieveAPIView):
    serializer_class = LibroSerializer

    def get(self, request, pk):
        libro = Libro.objects.filter(pk=pk).first()
        if not libro:
            return Response(
                {'success': False, 'detail': 'Libro no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(libro)
        return Response(
            {'success': True, 'detail': 'Libro encontrado', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Actualizar libro
class ActualizarLibro(generics.UpdateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def put(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        serializer = self.get_serializer(libro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Libro actualizado con éxito', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Eliminar libro
class BorrarLibro(generics.DestroyAPIView):
    serializer_class = LibroSerializer

    def delete(self, request, pk):
        libro = Libro.objects.filter(pk=pk).first()
        if not libro:
            return Response(
                {'success': False, 'detail': 'Libro no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        libro.delete()
        return Response(
            {'success': True, 'detail': f'Libro con ID {pk} eliminado con éxito'},
            status=status.HTTP_200_OK
        )

# ----------------- FILTROS -----------------

# Filtrar por autor
class LibrosPorAutor(generics.ListAPIView):
    serializer_class = LibroSerializer

    def get(self, request, autor_id):
        libros = Libro.objects.filter(autor_id=autor_id)
        if not libros:
            return Response(
                {'success': False, 'detail': 'No se encontraron libros para este autor'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(libros, many=True)
        return Response(
            {'success': True, 'detail': f'Libros del autor con ID {autor_id}', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

# Filtrar por editorial
class LibrosPorEditorial(generics.ListAPIView):
    serializer_class = LibroSerializer

    def get(self, request, editorial_id):
        libros = Libro.objects.filter(editorial_id=editorial_id)
        if not libros:
            return Response(
                {'success': False, 'detail': 'No se encontraron libros para esta editorial'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(libros, many=True)
        return Response(
            {'success': True, 'detail': f'Libros de la editorial con ID {editorial_id}', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# ----------------- CRUD MIEMBROS -----------------

# Listar miembros
class MiembroList(generics.ListAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def get(self, request):
        miembros = Miembro.objects.all()
        if not miembros:
            raise NotFound("No se encontraron miembros.")
        serializer = self.get_serializer(miembros, many=True)
        return Response(
            {'success': True, 'detail': 'Listado de miembros', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# Crear miembro
class CrearMiembro(generics.CreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Miembro creado con éxito', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )


# Actualizar miembro
class ActualizarMiembro(generics.UpdateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def put(self, request, pk):
        miembro = get_object_or_404(Miembro, pk=pk)
        serializer = self.get_serializer(miembro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Miembro actualizado con éxito', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# Eliminar miembro
class BorrarMiembro(generics.DestroyAPIView):
    serializer_class = MiembroSerializer

    def delete(self, request, pk):
        miembro = Miembro.objects.filter(pk=pk).first()
        if not miembro:
            return Response(
                {'success': False, 'detail': 'Miembro no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        miembro.delete()
        return Response(
            {'success': True, 'detail': f'Miembro con ID {pk} eliminado con éxito'},
            status=status.HTTP_200_OK
        )


# ----------------- FILTROS -----------------

# Filtrar miembros por nombre
class MiembrosPorNombre(generics.ListAPIView):
    serializer_class = MiembroSerializer

    def get(self, request, nombre):
        miembros = Miembro.objects.filter(nombre__icontains=nombre)
        if not miembros:
            return Response(
                {'success': False, 'detail': 'No se encontraron miembros con ese nombre'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(miembros, many=True)
        return Response(
            {'success': True, 'detail': f'Miembros con nombre parecido a "{nombre}"', 'data': serializer.data},
            status=status.HTTP_200_OK
        )
    

# ----------------- CRUD PRÉSTAMOS -----------------

# Listar préstamos
class PrestamoList(generics.ListAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get(self, request):
        prestamos = Prestamo.objects.all()
        if not prestamos:
            raise NotFound("No se encontraron préstamos.")
        serializer = self.get_serializer(prestamos, many=True)
        return Response(
            {'success': True, 'detail': 'Listado de préstamos', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# Ver préstamo específico
class PrestamoDetail(generics.RetrieveAPIView):
    serializer_class = PrestamoSerializer

    def get(self, request, pk):
        prestamo = Prestamo.objects.filter(pk=pk).first()
        if not prestamo:
            return Response(
                {'success': False, 'detail': 'Préstamo no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(prestamo)
        return Response(
            {'success': True, 'detail': 'Préstamo encontrado', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# Crear préstamo
class CrearPrestamo(generics.CreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Préstamo registrado con éxito', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )


# Actualizar préstamo
class ActualizarPrestamo(generics.UpdateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def put(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        serializer = self.get_serializer(prestamo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Préstamo actualizado con éxito', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# Eliminar préstamo
class BorrarPrestamo(generics.DestroyAPIView):
    serializer_class = PrestamoSerializer

    def delete(self, request, pk):
        prestamo = Prestamo.objects.filter(pk=pk).first()
        if not prestamo:
            return Response(
                {'success': False, 'detail': 'Préstamo no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        prestamo.delete()
        return Response(
            {'success': True, 'detail': f'Préstamo con ID {pk} eliminado con éxito'},
            status=status.HTTP_200_OK
        )


# ----------------- FILTROS -----------------

# Filtrar préstamos por miembro
class PrestamosPorMiembro(generics.ListAPIView):
    serializer_class = PrestamoSerializer

    def get(self, request, miembro_id):
        prestamos = Prestamo.objects.filter(miembro_id=miembro_id)
        if not prestamos:
            return Response(
                {'success': False, 'detail': 'No se encontraron préstamos para este miembro'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(prestamos, many=True)
        return Response(
            {'success': True, 'detail': f'Préstamos del miembro con ID {miembro_id}', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


# Filtrar préstamos por libro (historial de un libro)
class PrestamosPorLibro(generics.ListAPIView):
    serializer_class = PrestamoSerializer

    def get(self, request, libro_id):
        prestamos = Prestamo.objects.filter(libro_id=libro_id)
        if not prestamos:
            return Response(
                {'success': False, 'detail': 'No se encontraron préstamos para este libro'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(prestamos, many=True)
        return Response(
            {'success': True, 'detail': f'Historial de préstamos del libro con ID {libro_id}', 'data': serializer.data},
            status=status.HTTP_200_OK
        )