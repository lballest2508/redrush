from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Persona(models.Model):
    identificacion = models.CharField(max_length=20, unique=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.primer_nombre} {self.primer_apellido}'
    
    def check_password(self, password):
        return check_password(password, self.password)
    
    class Meta:
        db_table = 'personas'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

class Perfiles(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'perfiles'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

class PersonasPerfiles(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfiles, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.persona} - {self.perfil}'
    
    class Meta:
        db_table = 'personas_perfiles'
        verbose_name = 'Persona Perfil'
        verbose_name_plural = 'Personas Perfiles'

class Modulos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'modulos'
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'

class PerfilesModulos(models.Model):
    perfil = models.ForeignKey(Perfiles, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulos, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.perfil} - {self.modulo}'
    
    class Meta:
        db_table = 'perfiles_modulos'
        verbose_name = 'Perfil Modulo'
        verbose_name_plural = 'Perfiles Modulos'