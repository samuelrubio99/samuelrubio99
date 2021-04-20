from django.contrib import admin

from .models import Usuarios, Nivel_estudio, Formacion, Representante_empresa, Empresa, Forma_juridica, Usuario_desempeno, Area_desempeno, Seleccion, Actividad_economica, Empresa_actividad
# Register your models here.


class UsuariosAdmin(admin.ModelAdmin):
        list_display = ('identificacion','nombre', 'apellidos','fecha_nacimiento', 'email', 'telefono', 'direccion', 'descripcion', 'estatus')

class Nivel_estudioAdmin(admin.ModelAdmin):
        list_display =  ('nivel', 'titulo')

class FormacionAdmin(admin.ModelAdmin):
        list_display = ('id_user', 'id_estudio')


class Representante_empresaAdmin(admin.ModelAdmin):
        list_display = ('documento','nombres', 'apellidos', 'email','telefono')


class EmpresaAdmin(admin.ModelAdmin):
        list_display = ('nit', 'nombre', 'link_emp', 'id_representante', 'id_forma_juridica')


class Usuario_desempenoAdmin(admin.ModelAdmin):
        list_display = ('id_area', 'id_user')


class Area_desempenoAdmin(admin.ModelAdmin):
        list = ('area')

class Forma_juridicaAdmin(admin.ModelAdmin):
        list = ('f_juridica')

class SeleccionAdmin(admin.ModelAdmin):
        list_display = ('fecha_s', 'id_user','id_emp')


class Empresa_actividadAdmin(admin.ModelAdmin):
        list_display = ('id_empresa', 'id_actividad')

admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Nivel_estudio, Nivel_estudioAdmin)
admin.site.register(Formacion, FormacionAdmin)
admin.site.register(Representante_empresa, Representante_empresaAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Forma_juridica, Forma_juridicaAdmin)
admin.site.register(Seleccion, SeleccionAdmin)
admin.site.register(Usuario_desempeno, Usuario_desempenoAdmin)
admin.site.register(Area_desempeno)
admin.site.register(Actividad_economica)
admin.site.register(Empresa_actividad, Empresa_actividadAdmin)