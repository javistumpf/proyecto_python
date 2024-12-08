from django.db import models

# Create your models here.
class Empresa(models.Model):
    razon_social = models.CharField(max_length=255)
    cuit = models.CharField(max_length=11)
    email = models.EmailField()
    sector = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=50)
    descripcion = models.TextField()
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    archivo_cv = models.FileField(upload_to='cvs/')
    profesion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

class Busqueda(models.Model):
    puesto = models.CharField(max_length=100)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="busquedas")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    modalidad_trabajo = models.CharField(max_length=50)  # Presencial, remoto, híbrido, etc.
    modalidad_contratacion = models.CharField(max_length=50)  # Indeterminado, Plazo fijo, por temporada
    descripcion = models.TextField()
    requisitos_excluyentes = models.TextField()
    requisitos_deseables = models.TextField()
    estado = models.CharField(max_length=50, choices=[
        ('Activa', 'Activa'),
        ('Finalizada', 'Finalizada')
        ])

class Postulacion(models.Model):
    id_busqueda = models.ForeignKey(Busqueda, on_delete=models.CASCADE, related_name="postulaciones")
    id_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name="postulaciones")
    fecha_postulacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[
        ('En revisión', 'En revisión'),
        ('Aceptado', 'Aceptado'),
        ('Rechazado', 'Rechazado')
        ])