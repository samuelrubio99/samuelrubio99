from django.db import models
from django.utils.translation import ugettext_lazy as _


class Usuarios (models.Model):
    identificacion = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True)
    email = models.CharField(max_length=200, unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    direccion = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    estatus = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

    class Meta():
        verbose_name_plural = ("Usuarios")


class Nivel_estudio(models.Model):
    nivel = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    
    def __str__(self):
        return str({self.nivel, self.titulo})

    class Meta():
        verbose_name_plural = ("Nivel_estudio")

class Formacion(models.Model):
    id_user =  models.ForeignKey(Usuarios, on_delete= models.CASCADE)
    id_estudio = models.ForeignKey(Nivel_estudio,on_delete=models.CASCADE)

    def __int__(self):
        return self.id_user


    class Meta():
        verbose_name_plural = ("Formacion")

class Representante_empresa(models.Model):
    documento = models.CharField(max_length=200)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    telefono = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return str(self.nombres)
    
    
    class Meta():
        verbose_name_plural = ("Representante_empresa")

class Forma_juridica(models.Model):
    f_juridica = models.CharField(max_length=300)

    def __str__(self):
        return str(self.f_juridica)
    class Meta():
        verbose_name_plural = ("Forma_juridica")

class Empresa (models.Model):
    nit = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    link_emp = models.CharField(max_length=300)
    id_representante = models.ForeignKey(Representante_empresa, on_delete=models.CASCADE)
    id_forma_juridica = models.ForeignKey(Forma_juridica, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nit)
    class Meta():
        verbose_name_plural = ("Empresa")

class Seleccion(models.Model):
    fecha_s = models.DateTimeField()
    id_user =  models.ForeignKey(Usuarios, on_delete= models.CASCADE)
    id_emp =  models.ForeignKey(Empresa, on_delete= models.CASCADE)
    
    def __str__(self):
        return str(self.fecha_s)

    class Meta():
        verbose_name_plural = ("Seleccion")

class Area_desempeno(models.Model):
    area = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.area)

    class Meta():
        verbose_name_plural = ("Area_desempeno")
    
class Usuario_desempeno(models.Model):
    id_area =  models.ForeignKey(Area_desempeno, on_delete= models.CASCADE)
    id_user =  models.ForeignKey(Usuarios, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre    

    class Meta():
        verbose_name_plural = ("Usuario_desempeno")

class Actividad_economica(models.Model):
    actividad = models.CharField(max_length=300)

    def __str__(self):
        return str(self.actividad)
    
    class Meta():
        verbose_name_plural = ("Actividad_economica")

class Empresa_actividad(models.Model):
    id_empresa =  models.ForeignKey(Empresa, on_delete= models.CASCADE)    
    id_actividad =  models.ForeignKey(Actividad_economica, on_delete= models.CASCADE)

  
    
    class Meta():
        verbose_name_plural = ("Empresa_actividad")

