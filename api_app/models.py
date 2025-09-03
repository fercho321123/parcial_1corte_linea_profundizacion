from django.db import models
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True, db_column='id_autor')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True, db_column='id_editorial')
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'editorial'
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True, db_column='id_libro')
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True)
    anio_publicacion = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, db_column='id_autor')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, db_column='id_editorial')

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'


class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True, db_column='id_miembro')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_membresia = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'miembro'
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'


class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True, db_column='id_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, db_column='id_libro')
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, db_column='id_miembro')

    def __str__(self):
        return f"Préstamo {self.id_prestamo} - {self.libro.titulo} a {self.miembro.nombre}"

    class Meta:
        db_table = 'prestamo'
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
