from django.db import models
from django.utils.html import format_html

# Create your models here.

class Categoria(models.Model):
    nombre = models.Field(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.nombre

class Producto(models.Model):

    Borrador = 'Borrador'
    Publicado = 'Publicado'
    Retirado = 'Retirado'
    APROBACION_PRODUCTO = (
        (Borrador, 'Borrador'),
        (Publicado, 'Publicado'),
        (Retirado, 'Retirado'),
    )

    producto = models.CharField(max_length=200)
    estado = models.CharField(max_length=10, choices=APROBACION_PRODUCTO, default='Borrador')
    fecha_publicacion = models.DateTimeField('Fecha de Publicacion')
    ruta_imagen = models.FileField(upload_to='fotos/%Y/%m/%d', default='defecto/defecto.png', blank=True, null=True)
    categoria = models.ManyToManyField(Categoria)

    def tipo_de_producto(self):
        if self.estado == 'Retirado':
            return format_html('<span style="color: #f00;">{}</span>', self.estado)
        elif self.estado == 'Borrador':
            return format_html('<span style="color: #f0f;">{}</span>', self.estado)
        elif self.estado == 'Publicado':
            return format_html('<span style="color: #099;">{}</span>', self.estado)

    def __str__(self):
        return('<%s => %s: %s, %s>' % (self.__class__.__name__, self.producto, self.fecha_publicacion, self.ruta_imagen))