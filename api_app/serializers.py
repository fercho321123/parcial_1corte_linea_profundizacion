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
    autor = AutorSerializer(read_only=True)
    editorial = EditorialSerializer(read_only=True)
    autor_id = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(), source="autor", write_only=True
    )
    editorial_id = serializers.PrimaryKeyRelatedField(
        queryset=Editorial.objects.all(), source="editorial", write_only=True
    )

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
    id_libro = serializers.PrimaryKeyRelatedField(
        queryset=Libro.objects.all(), source="libro", write_only=True
    )
    id_miembro = serializers.PrimaryKeyRelatedField(
        queryset=Miembro.objects.all(), source="miembro", write_only=True
    )


    class Meta:
        model = Prestamo
        fields = '__all__'
