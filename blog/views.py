from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from apps.articulo.models import Articulo, Categoria



class IndexView(View):
    def get(self, request):
        articulos_banner = Articulo.get_articulos_recientes()
        articulos = Articulo.objects.all()
        categorias = Categoria.objects.all()
        comentarios = 25
        id_usuario = "Admin"
        context = { 
                'articulos_banner' : articulos_banner,
                'articulos' : articulos,
                'id_usuario' : id_usuario,
                'comentarios' : comentarios,
                'categorias' : categorias
                   }
        return render(request, 'index.html', context)

def contacto(request):
    return render(request,'contacto.html')

def sobre_nosotros(request):
    return render(request, 'nosotros.html')

def registrarse(request):
    return render(request, 'registrarse.html',
                  {'form':UserCreationForm})
    
def registration_success(request):
    return render(request,'registration/registration_success.html' )