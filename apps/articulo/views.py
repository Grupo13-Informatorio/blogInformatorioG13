from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView
from django.contrib import messages

from .models import Articulo, Categoria
from apps.comentario.models import Comentario
from .forms import ArticuloForm
from apps.comentario.forms import ComentarioForm


# ##Vista basada en clases
class DeleteArticulo(DeleteView):
    model = Articulo
    template_name = "articulo/eliminarArticulo.html"
    def get_success_url(self):
        return reverse('articulo:articulos')

class ArticuloView(View):
    template_name = 'articulo/articulo.html'

    def get(self, request, categoria=None):
        if categoria:
            articulos = Articulo.objects.filter(categoria__nombre=categoria)
        else:
            articulos = Articulo.objects.all()

        categorias = Categoria.objects.all()

        return render(request, 'articulo/articulo.html',{'articulos' : articulos,'categorias': categorias}) ##

def articulo_crear(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            print(f'form is valid: {form.is_valid()}')
            form.save()
            return redirect('apps.articulo:articulos')

    else:
        form = ArticuloForm()
    return render(request, 'articulo/articulo_form.html', {'form':form})

    
class ActualizarArticulo(UpdateView):
    
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/articulo_editar.html'
    success_url = ''

    def post(self, request, *args, **kwargs):
        messages.success(request, "Articulo actualizado correctamente")
        return super().post(request, *args, **kwargs)

class ArticuloIndividualView(View):
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
        return render(request, 'articulo/articulo_individual.html', context)

class ArticuloResumidoView(View):
    def get(self, request, id):
        articulo = Articulo.objects.get(id=id)
        categorias = Categoria.objects.all()
        context = { 
                'articulo' : articulo,
                'categorias' : categorias
                   }
        return render(request, 'articulo/articulo_resumen.html', context)
