from rest_framework import serializers
from .models import Autor, Editorial, Libro, Miembro, Prestamo


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    # Para mostrar datos del autor y editorial dentro del libro
    autor = AutorSerializer(read_only=True)
    editorial = EditorialSerializer(read_only=True)

    class Meta:
        model = Libro
        fields = '__all__'


class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'


class PrestamoSerializer(serializers.ModelSerializer):
    # Para mostrar libro y miembro dentro del préstamo
    libro = LibroSerializer(read_only=True)
    miembro = MiembroSerializer(read_only=True)

    class Meta:
        model = Prestamo
        fields = '__all__'
