from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

from .functions import toSlug, calcularCategoria

# Create your models here.

class Atleta(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=40, primary_key=True, unique=True)
    imagen = models.URLField(null=True, blank=True)
    nombre = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True)
    sexo = models.CharField(max_length=9, 
                            choices=[
                                ('M', 'M'),
                                ('F', 'F'),
                            ])
    disciplina = models.CharField(max_length=20, 
                                choices=[
                                    ('Velocista', 'Velocista'),
                                    ('Medio fondo', 'Medio fondo'),
                                    ('Fondista', 'Fondista'),
                                ])
    edad = models.DateField()
    categoria = models.CharField(max_length=10)
    federado = models.BooleanField()
    instagram = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return str(self.usuario)

    def save(self): #*args, **kwargs
        """
        Establece un slug
        Guarda la categoría del atleta en función de su edad
        """
        anio = datetime.today().year
        edad = anio - self.edad.year

        self.slug = toSlug(self.nombre, self.apellido1)
        self.categoria = calcularCategoria(edad)

        super().save()


class Marca(models.Model):
    usuario = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    fecha = models.DateField()
    lugar = models.CharField(max_length=20, 
                            choices=[
                                ('Antequera', 'Antequera'),
                                ('Chiclana', 'Chiclana'),
                                ('Granada-CAR', 'Granada-CAR'),
                                ('Granada-JUV', 'Granada-JUV'),
                                ('Málaga-CAR', 'Málaga-CAR'),
                                ('Málaga-CIU', 'Málaga-CIU'),
                                ('Monzón', 'Monzón'),
                            ])
    prueba = models.CharField(max_length=10,
                            choices={
                                ('60m', '60m'),
                                ('100m', '100m'),
                                ('200m', '200m'),
                                ('400m', '400m'),
                                ('800m', '800m'),
                                ('1500m', '1500m'),
                                ('3000m', '3000m'),
                                ('5000m', '5000m'),
                                ('10000m', '10000m'),
                            })
    tiempo = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return '%s %s' % (self.usuario, self.fecha)