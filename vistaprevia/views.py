from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    # return HttpResponse("Hola Mundo!!!")
    contenido = {
        'nombre_sitio': 'LibrosOnline'
    }
    para_minorista = {
        'tipo_usuario':'minorista', 
        'incremento': '25'
    }
    para_mayorista = {'tipo_usuario':'mayorista', 'incremento': '10'}
    page_title = "Pagina de inicio"
    site_name = "Venta de Libros Online"
    palabras_claves = "Palabras claves"
    descripcion = "Descripción"

    return render(request, 'vistaprevia/index.html', {'contenido':contenido, 'para_minorista':para_minorista, 'para_mayorista':para_mayorista, 'page_title':page_title, 'site_name':site_name, 'palabras_claves':palabras_claves, 'descripcion':descripcion})

def contacto(request):
    return render(request, 'vistaprevia/contacto.html')
