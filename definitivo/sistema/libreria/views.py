from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from libreria.models import Libro, Usuario
from .models import Lectura,Favorito,Opinion

from .auxiliares import *



def pantallaPrincipal(request):
    return render(request, "paginas/pantallaPrincipal.html")

def misFavoritos(request):
    favoritos=Favorito.objects.all()
    librosTodos=Libro.objects.all()
    idUsuario=(request.COOKIES.get('idUsuario'))
    misFavoritos=[]
    for favorito in favoritos:
        if(str(favorito.idUsuario)==str(idUsuario)):
            for libro in librosTodos:
                if(str(libro.id)==str(favorito.idLibro)):
                    favDTO=FavoritoDTO(libro.id,libro.titulo,libro.autor,libro.foto)
                    misFavoritos.append(favDTO)
            


    vacio=False
    if(len(misFavoritos)==0):
        vacio=True 
        

    return render(request, "paginas/misFavoritos.html",{"misFavoritos":misFavoritos,"vacio":vacio})

def misLecturas(request):
    lecturas=Lectura.objects.all()
    librosTodos=Libro.objects.all()
    idUsuario=(request.COOKIES.get('idUsuario'))
    misLecturas=[]
    for lectura in lecturas:
        if(str(lectura.idUsuario)==str(idUsuario)):
            for libro in librosTodos:
                if(str(libro.id)==str(lectura.idLibro)):
                    
                    lecDTO=LecturaDTO(lectura.id,libro.titulo,libro.id,lectura.paginaActual,lectura.estado)
                    misLecturas.append(lecDTO)

    vacio=False
    if(len(misLecturas)==0):
        vacio=True
    return render(request, "paginas/misLecturas.html",{"misLecturas":misLecturas,"vacio":vacio})

def buscarLibros(request):
    libros=Libro.objects.all()
    return render(request, "paginas/buscarLibros.html",{"libros":libros})

def detalleLibro(request,id):
    libro=Libro.objects.get(id=id)
    opiniones=Opinion.objects.all()
    favoritos=Favorito.objects.all()
    print(favoritos)
    idUsuario=(request.COOKIES.get('idUsuario'))

    guardaFavorito=False
    for favorito in favoritos:
        if((str(favorito.idUsuario)==str(idUsuario)) & (str(favorito.idLibro)==str(id))):
            guardaFavorito=True


    lecturas=Lectura.objects.all()
    lecturaUsuario=False
    for lectura in lecturas:
        if((str(lectura.idUsuario)==str(idUsuario)) & (str(lectura.idLibro)==str(id))):
            lecturaUsuario=True

    validas=[]
    
    for opinion in opiniones:
        if(str(opinion.idLibro)==str(id)):
            validas.append(opinion)
            
    validasOpinionesDTO=[]
    for valida in validas:
        idUsuario=(valida.idUsuario)
        usuario=Usuario.objects.get(id=idUsuario)
        opinionDTO=OpinionDTO(usuario.username, valida.comentario,valida.puntuacion)
        validasOpinionesDTO.append(opinionDTO)

            


    
    return render(request, "paginas/detalleLibro.html",{"libro": libro,"validas":validasOpinionesDTO,"guardaFavorito":guardaFavorito,"lecturaUsuario":lecturaUsuario})

def guardarOpinion(request):
    idLibro=request.GET.get('libro', None)
    print(idLibro)
   
    libro=Libro.objects.get(id=idLibro)
    return render(request, "paginas/guardarOpinion.html",{"libro":libro})


def editarLectura(request,id):
    lectura=Lectura.objects.get(id=id)
    libro=Libro.objects.get(id=lectura.idLibro)
    return render(request,"paginas/editarLectura.html",{"lectura":lectura,"libro":libro})

def identificacion(request):
    return render(request, "paginas/identificacion.html")

def registro(request):
    
    return render(request, "paginas/registro.html")


def miUsuario(request):
    print(request.COOKIES.get('idUsuario'))
    print(request.COOKIES.get('username'))
    username=request.COOKIES.get('username')

    return render(request, "paginas/miUsuario.html",{"username":username})

def registrarUsuario(request):
    username=request.POST["username"]
    password=request.POST["password"]
    email=request.POST["email"]

    usuario=Usuario.objects.create(username=username,password=password, email=email)

    messages.success(request,"Usuario registrado")
    
    return redirect("/registro")


def identificarUsuario(request):
    username=request.POST["username"]
    password=request.POST["password"]
    
    response = redirect('/miUsuario')
    
    

    usuarios=Usuario.objects.all()

    correcto=False
    for i in usuarios:
        if(i.username==username):
            if(i.password==password):
                response.set_cookie('username', i.username)
                response.set_cookie('idUsuario', i.id)
                correcto=True
    
    if(correcto==True):
        if(username!="admin"):
            return response
        else:
            response = redirect('/gestionLibros')
            return response
    else:
        messages.success(request,"Usuario y contraseña incorrecto")
        return redirect("/identificacion")
    
    
def gestionLibros(request):
    libros=Libro.objects.all()
    return render(request, "paginas/gestionLibros.html",{"libros":libros})


def crearLibro(request):
    return render(request, "paginas/crearLibro.html")

def registrarLibro(request):
    titulo=request.POST["titulo"]#cojo los datos
    autor=request.POST["autor"]
    editorial=request.POST["editorial"]
    isbn=request.POST["isbn"]
    paginas=request.POST["paginas"]

    foto=request.FILES["foto"]
    print(foto)
    

    libro=Libro.objects.create(titulo=titulo,autor=autor, editorial=editorial,isbn=isbn,paginas=paginas,foto=foto)# creo el objeto
    messages.success(request,"Libro creado")
    return redirect("/gestionLibros")


def eliminarLibro(request,id):
    
    libro=Libro.objects.get(id=id)
    libro.delete()
    print(id)


    messages.success(request,"Libro eliminado")
    return redirect("/gestionLibros")


def editarLibro(request,id):
    libro=Libro.objects.get(id=id)

    return render(request,"paginas/editarLibro.html",{"libro":libro})


def editarLibroAccion(request):
    titulo=request.POST["titulo"]#cojo los datos
    autor=request.POST["autor"]
    editorial=request.POST["editorial"]
    isbn=request.POST["isbn"]
    paginas=request.POST["paginas"]
    id=request.POST["id"]
    foto=request.FILES["foto"]
    libro=Libro.objects.get(id=id)

    libro.titulo=titulo
    libro.editorial=editorial
    libro.autor=autor
    libro.isbn=isbn
    libro.paginas=paginas
    libro.foto=foto
    libro.save()

    messages.success(request,"Libro editado")
    return redirect("/gestionLibros")


def editarLecturaAccion(request):
    id=request.POST["id"]#cojo los datos
    paginaActual=request.POST["paginaActual"]#cojo los datos
    fechaInicio=request.POST["fechaInicio"]#cojo los datos
    fechaFin=request.POST["fechaFin"]#cojo los datos
    estado=request.POST["estado"]#cojo los datos

    

    lectura=Lectura.objects.get(id=id)

    lectura.paginaActual=paginaActual
    lectura.fechaInicio=fechaInicio
    lectura.fechaFin=fechaFin
    lectura.estado=estado
    lectura.save()


    messages.success(request,"Lectura editada")
    return redirect("/misLecturas")

def buscarLibrosTitulo(request):
    titulo=request.POST["titulo"]
    libros=Libro.objects.all()
    validos=[]
    for libro in libros:
        if(libro.titulo.find(titulo)!=-1):
            validos.append(libro)


    #return render(request, "paginas/buscarLibros.html",{"libros":validos})
    ninguno=False
    if(len(validos)==0):
        ninguno=True
    return render(request, "paginas/buscarLibros.html",{"libros":validos,"ninguno":ninguno})


    

def leer(request,id):
    print(id)
    idUsuario=(request.COOKIES.get('idUsuario'))
    now = datetime.now()
    fechaInicio=str(now.day)+"/"+str(now.month)+"/"+str(now.year)

    lectura=Lectura.objects.create(idUsuario=idUsuario,idLibro=id,paginaActual=0,fechaInicio=fechaInicio,fechaFin="Sin finalizar",estado="Leyendo")
    messages.success(request,"Has empezado a leer el libro")
    return redirect("/detalleLibro/"+id)


def favorito(request,id):
    print(id)
    idUsuario=(request.COOKIES.get('idUsuario'))
    favorito=Favorito.objects.create(idUsuario=idUsuario,idLibro=id)
    messages.success(request,"Libro guardado en favoritos")
    return redirect("/detalleLibro/"+id)


def eliminarFavorito(request,id):
    favoritos=Favorito.objects.all()
    idUsuario=(request.COOKIES.get('idUsuario'))
    for favorito in favoritos:
        if((str(favorito.idUsuario)==str(idUsuario)) & (str(favorito.idLibro)==str(id))):
            favoritoEliminar=favorito
            favoritoEliminar.delete()
            messages.success(request,"Libro eliminado de favoritos")
    
    return redirect("/detalleLibro/"+id)


def eliminarFavoritoVentana(request,id):
    favoritos=Favorito.objects.all()
    idUsuario=(request.COOKIES.get('idUsuario'))
    for favorito in favoritos:
        if((str(favorito.idUsuario)==str(idUsuario)) & (str(favorito.idLibro)==str(id))):
            favoritoEliminar=favorito
            favoritoEliminar.delete()
            messages.success(request,"Libro eliminado de favoritos")
    
    return redirect("/misFavoritos")



def dejarLeer(request,id):
    lecturas=Lectura.objects.all()
    idUsuario=(request.COOKIES.get('idUsuario'))
    for lectura in lecturas:
        if((str(lectura.idUsuario)==str(idUsuario)) & (str(lectura.idLibro)==str(id))):
            lecturaEliminar=lectura
            lecturaEliminar.delete()
            messages.success(request,"Has dejado de leer el libro")
    
    return redirect("/detalleLibro/"+id)

def dejarLeerMisLecturas(request,id):
    lecturas=Lectura.objects.all()
    idUsuario=(request.COOKIES.get('idUsuario'))
    for lectura in lecturas:
        if((str(lectura.idUsuario)==str(idUsuario)) & (str(lectura.idLibro)==str(id))):
            lecturaEliminar=lectura
            lecturaEliminar.delete()
            messages.success(request,"Has dejado de leer el libro")
    
    return redirect("/misLecturas")


def guardarOpinionLibro(request):
    idLibro=request.POST["idLibro"]
    comentario=request.POST["comentario"]
    puntuacion=request.POST["puntuacion"]
    idUsuario=(request.COOKIES.get('idUsuario'))


 
    messages.success(request,"Opinión guardada")

    opinion=Opinion.objects.create(idUsuario=idUsuario,idLibro=idLibro,comentario=comentario,puntuacion=puntuacion)

    return redirect("/detalleLibro/"+idLibro)


