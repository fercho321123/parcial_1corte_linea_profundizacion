from django.urls import path
from .views import (
   LibroList, CrearLibro, LibroDetail, ActualizarLibro,BorrarLibro,LibrosPorEditorial,LibrosPorAutor,MiembroList,CrearMiembro,PrestamoList,PrestamoDetail,CrearPrestamo,ActualizarPrestamo,BorrarPrestamo
   ,ActualizarMiembro,BorrarMiembro,MiembrosPorNombre,ActualizarPrestamo,BorrarPrestamo,PrestamosPorMiembro,PrestamosPorLibro
)

urlpatterns=[
# Libros
path('libros/', LibroList.as_view(), name='lista_libros'),
path('libros/crear/', CrearLibro.as_view(), name='crear_libro'),
path('libros/<int:pk>/', LibroDetail.as_view(), name='detalle_libro'),
path('libros/<int:pk>/actualizar/', ActualizarLibro.as_view(), name='actualizar_libro'),
path('libros/<int:pk>/borrar/', BorrarLibro.as_view(), name='borrar_libro'),

# Filtros
path('libros/autor/<int:autor_id>/', LibrosPorAutor.as_view(), name='libros_por_autor'),
path('libros/editorial/<int:editorial_id>/', LibrosPorEditorial.as_view(), name='libros_por_editorial'),

path('miembros/', MiembroList.as_view(), name='lista_miembros'),
path('miembros/crear/', CrearMiembro.as_view(), name='crear_miembro'),  
path('miembros/<int:pk>/actualizar/', ActualizarMiembro.as_view(), name='actualizar_miembro'),
path('miembros/<int:pk>/borrar/', BorrarMiembro.as_view(), name='borrar_miembro'),
# filtrar miembros por nombre
path('miembros/nombre/<str:nombre>/', MiembrosPorNombre.as_view(), name='miembros_por_nombre'),

# Prestamos
path('prestamos/', PrestamoList.as_view(), name='lista_prestamos'),
path('prestamos/crear/', CrearPrestamo.as_view(), name='crear_prestamo '),
path('prestamos/<int:pk>/', PrestamoDetail.as_view(), name='detalle_prestamo'),
path('prestamos/<int:pk>/actualizar/', ActualizarPrestamo.as_view(), name='actualizar_prestamo'),
path('prestamos/<int:pk>/borrar/', BorrarPrestamo.as_view(), name='borrar_prestamo'),
# filtros prestamos por miembro y por libro
path('prestamos/miembro/<int:miembro_id>/', PrestamosPorMiembro.as_view(), name='prestamos_por_miembro'),
path('prestamos/libro/<int:libro_id>/', PrestamosPorLibro.as_view(), name='prestamos_por_libro'),


] 