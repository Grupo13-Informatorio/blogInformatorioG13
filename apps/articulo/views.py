from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import UpdateView
from apps.articulo.forms import ArticuloCreationForm
from apps.comentario.forms import ComentarioCreationForm

from apps.comentario.models import Comentario

from .models import Articulo, Categoria

# Create your views here.

class ArticuloView(View):
    def get(self, request, id):
        articulo = Articulo.objects.filter(is_active = True).get(id=id)
        comentarios = Comentario.objects.filter(is_active = True, articulo = articulo)
        categorias = Categoria.objects.all()
        cant_comentarios = comentarios.count()
        form = ComentarioCreationForm()
        context = { 
                'articulo' : articulo,
                'cant_comentarios' : cant_comentarios,
                'comentarios' : comentarios,
                'categorias' : categorias,
                'form' : form,
                   }
        return render(request, 'articulo/articulo_mostrar.html', context)
        

class ArticulosView(View):
    def get(self, request):
        articulos_banner = Articulo.get_articulos_recientes()
        articulos = Articulo.objects.all()
        categorias = Categoria.objects.all()
        context = { 
                'articulos_banner' : articulos_banner,
                'articulos' : articulos,
                'categorias' : categorias
                   }
        return render(request, 'articulo/articulos_todos.html', context)


class ArticuloResumidoView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        categorias = Categoria.objects.all()
        context = { 
                'articulo' : articulo,
                'id_usuario' : "Admin",
                'comentarios' : 35,
                'categorias' : categorias
                   }
        return render(request, 'articulo/articulo_resumen.html', context)


class EditarArticulo(UpdateView):
    
    model = Articulo
    form_class = ArticuloCreationForm
    template_name = 'articulo/articulo_editar.html'
    success_url = ''
    


def crearArticulo(request):

    form_articulo = ArticuloCreationForm()
    
    if request.method == "POST":
        form = ArticuloCreationForm(data=request.POST, files=request.FILES)
        form.instance.creado_por = request.user
        if form.is_valid():
            form.save()
            return redirect('articulo:articulos')
        else:
            return redirect('articulo:articulos')
    else:
        return render(request,'articulo/articulo_crear.html',{'form': form_articulo} )
    
