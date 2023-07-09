from django.db import models

# Create your models here.



class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100, verbose_name="Username")
    password=models.CharField(max_length=100, verbose_name="Password")
    email=models.CharField(max_length=100, verbose_name="Email")
   


    def __str__(self):
        fila="Username:"+self.username
        return fila


    def delete(self,using=None, keep_parents=False):
        super().delete()





class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name="Titulo", null=True)
    autor=models.CharField(max_length=100, verbose_name="Autor", null=True)
    editorial=models.CharField(max_length=100, verbose_name="Editorial", null=True)
    foto=models.ImageField(upload_to="imagenes/",verbose_name="Foto" ,null=True)
    isbn=models.CharField(max_length=100, verbose_name="isbn", null=True)
    paginas=models.IntegerField(verbose_name="Paginas", null=True)
    


    def __str__(self):
        fila="Titulo:"+self.titulo
        return fila


    def delete(self,using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()


class Lectura(models.Model):
    id=models.AutoField(primary_key=True)
    idUsuario=models.IntegerField( verbose_name="IdUsuario")
    idLibro=models.IntegerField( verbose_name="IdLibro")
    paginaActual=models.IntegerField(verbose_name="PaginaActual")
    fechaInicio=models.CharField(max_length=100, verbose_name="FechaInicio", null=True)
    fechaFin=models.CharField(max_length=100, verbose_name="FechaFin", null=True)
    estado=models.CharField(max_length=100, verbose_name="Estado", null=True)


    def delete(self,using=None, keep_parents=False):
        super().delete()


class Opinion(models.Model):
    id=models.AutoField(primary_key=True)
    idUsuario=models.IntegerField( verbose_name="IdUsuario")
    idLibro=models.IntegerField( verbose_name="IdLibro")
    puntuacion=models.IntegerField(verbose_name="Puntuacion")
    comentario=models.CharField(max_length=100, verbose_name="Comentario", null=True)

    def delete(self,using=None, keep_parents=False):
        super().delete()


class Favorito(models.Model):
    id=models.AutoField(primary_key=True)
    idUsuario=models.IntegerField( verbose_name="IdUsuario")
    idLibro=models.IntegerField( verbose_name="IdLibro")


    def delete(self,using=None, keep_parents=False):
        super().delete()