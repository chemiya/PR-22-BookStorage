from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns=[
    path("",views.pantallaPrincipal, name="pantallaPrincipal"),
    path("identificacion",views.identificacion, name="identificacion"),
    path("registro",views.registro, name="registro"),
    path("miUsuario",views.miUsuario, name="miUsuario"),
    path("registrarUsuario/",views.registrarUsuario, name="registrarUsuario"),
    path("registrarLibro/",views.registrarLibro, name="registrarLibro"),
    path("identificarUsuario/",views.identificarUsuario, name="identificacionUsuario"),
    path("misFavoritos",views.misFavoritos, name="misFavoritos"),
    path("misLecturas",views.misLecturas, name="misLecturas"),
    path("buscarLibros",views.buscarLibros, name="buscarLibros"),
    path("detalleLibro/<id>",views.detalleLibro, name="detalleLibro"),
    path("buscarLibrosTitulo/detalleLibro/<id>",views.detalleLibro, name="detalleLibro"),
    
    path("guardarOpinion/",views.guardarOpinion, name="guardarOpinion"),
    path("gestionLibros",views.gestionLibros, name="gestionLibros"),
    path("crearLibro",views.crearLibro, name="crearLibro"),
    path("editarLibroAccion/",views.editarLibroAccion, name="editarLibroAccion"),
    path("editarLecturaAccion/",views.editarLecturaAccion, name="editarLecturaAccion"),
    path("eliminarLibro/<id>",views.eliminarLibro),
    path("editarLibro/<id>",views.editarLibro),
    path("leer/<id>",views.leer),
    path("favorito/<id>",views.favorito),
    path("eliminarFavorito/<id>",views.eliminarFavorito),
    path("eliminarFavoritoVentana/<id>",views.eliminarFavoritoVentana),
    path("editarLectura/<id>",views.editarLectura),
    path("dejarLeer/<id>",views.dejarLeer),
    path("dejarLeerMisLecturas/<id>",views.dejarLeerMisLecturas),
    path("buscarLibrosTitulo/",views.buscarLibrosTitulo),
    path("guardarOpinionLibro/",views.guardarOpinionLibro),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)