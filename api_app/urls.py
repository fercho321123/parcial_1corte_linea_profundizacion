from django.urls import path
from .views import (AutorList, CrearAutor, AutorDetail, ActualizarAutor, BorrarAutor,
    ConsultarAutores, ConsultarAutorPorID,

    # Editoriales
    EditorialList, CrearEditorial, EditorialDetail, ActualizarEditorial, BorrarEditorial)



urlpatterns = [
    path('autores/', AutorList.as_view(), name='lista_autores'),
    path('autores/crear/', CrearAutor.as_view(), name='crear_autor'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='detalle_autor'),
    path('autores/<int:pk>/actualizar/', ActualizarAutor.as_view(), name='actualizar_autor'),
    path('autores/<int:pk>/borrar/', BorrarAutor.as_view(), name='borrar_autor'),

    # Filtros autores
    path('autores/consultar/', ConsultarAutores.as_view(), name='consultar_autores'),
    path('autores/consultar/<int:autor_id>/', ConsultarAutorPorID.as_view(), name='consultar_autor_por_id'),

    # ---------------- EDITORIALES ----------------
    path('editoriales/', EditorialList.as_view(), name='lista_editoriales'),
    path('editoriales/crear/', CrearEditorial.as_view(), name='crear_editorial'),
    path('editoriales/<int:pk>/', EditorialDetail.as_view(), name='detalle_editorial'),
    path('editoriales/<int:pk>/actualizar/', ActualizarEditorial.as_view(), name='actualizar_editorial'),
    path('editoriales/<int:pk>/borrar/', BorrarEditorial.as_view(), name='borrar_editorial'),
] 