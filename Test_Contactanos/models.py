from django.db import models

class Contact(models.Model):
    rut = models.CharField(max_length=20, default=20)
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')
    apellidos = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nombre