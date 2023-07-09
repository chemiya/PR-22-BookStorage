class FavoritoDTO:
    def __init__(self,id,titulo,autor,foto):
        self.id=id
        self.titulo=titulo
        self.autor=autor
        self.foto=foto


class LecturaDTO:
    def __init__(self,id,titulo,idLibro,paginaActual,estado):
        self.id=id
        self.titulo=titulo
        self.idLibro=idLibro
        self.paginaActual=paginaActual
        self.estado=estado


class CamposParciales:
    def __init__(self,id,comentario,puntuacion):
        self.id=id
        self.comentario=comentario
        self.puntuacion=puntuacion

class OpinionDTO:
    def __init__(self,usuario,comentario,puntuacion):
        self.usuario=usuario
        self.comentario=comentario
        self.puntuacion=puntuacion
        