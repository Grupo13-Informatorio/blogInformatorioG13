from django.urls import  path

from apps.comentario.views import  registrarComentario
from .views import  ArticuloResumidoView, ArticuloView, ArticulosView, crearArticulo, EditarArticulo

app_name = 'articulo'

urlpatterns = [
    path('articulos',ArticulosView.as_view(), name = 'articulos'),
    path('articulo/<int:id>',ArticuloView.as_view(), name = 'mostrarArticulo'),
    path('articulo/crear',crearArticulo, name = 'crear'),
    path('articulo_resumido/<int:id>',ArticuloResumidoView.as_view(), name = 'articulo_resumido'),
    path('articulo/<int:id>/comentar', registrarComentario, name='comentar'),
    path('articulo/<int:pk>/editar', EditarArticulo.as_view(), name='editar')
]