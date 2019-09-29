from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from vistaprevia.models import Producto
from vistaprevia.forms import CargarForm
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from consulta import views as consulta_views

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

def cargar_imagen(request):
    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)

        if form.is_valid():
            producto = form.cleaned_data['producto']
            fecha_publicacion = form._clean_fields['fecha_publicacion']
            ruta_imagen = form.cleaned_data['ruta_imagen']

            newdoc = Producto(producto=producto, fecha_publicacion=fecha_publicacion, ruta_imagen=ruta_imagen)
            newdoc.save()
            return redirect("index")
    else:
        form = CargarForm()
    return render(request, 'vistaprevia/formulario.html', {'form':form})

def ver_imagen(request, producto_id):
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    return render_to_response('vistaprevia/verimagen.html', {
        'producto':producto,
        'error_message': "No has seleccionado un producto.",
    }, content_type=RequestContext(request))


def ver_imagenes(request):
    try:
        productos = Producto.objects.all()
    except Producto.DoesNotExist:
        raise Http404
    return render_to_response('vistaprevia/verimagenes.html', {
        'productos': productos,
        'error_message': "No has seleccionado un producto",
    }, content_type=RequestContext(request))