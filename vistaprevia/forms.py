from django.forms import ModelForm
from .models import Producto

class CargarForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['categoria', 'producto', 'fecha_publicacion', 'ruta_imagen']

        error_messages = {
            'producto': {
                'required': ("Se debe un nombre al prodcuto")
            },
            'fecha_publicacion': {'required': ("Se debe agregar la fecha de publicacion en el formato adecuado")},
        }

    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)