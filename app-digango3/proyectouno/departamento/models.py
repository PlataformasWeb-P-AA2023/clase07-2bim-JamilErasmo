from django.db import models

# Create your models here.

class Edificio(models.Model):
    opciones_tipo_Edificio = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    )
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=30,\
                            choices= opciones_tipo_Edificio)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

  