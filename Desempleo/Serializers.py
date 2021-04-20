from rest_framework import serializers

from .models import Usuarios, Nivel_estudio, Formacion, Representante_empresa, Empresa, Forma_juridica, Usuario_desempeno, Area_desempeno, Seleccion, Actividad_economica, Empresa_actividad


class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuarios
        fields =  ('identificacion','nombre', 'apellidos','fecha_nacimiento', 'email', 'telefono', 'direccion', 'descripcion', 'estatus')

        
class Nivel_estudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel_estudio
        fields = ('nivel', 'titulo') 


class FormacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Formacion
        fields = ['id_user', 'id_estudio']


class Representante_empresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Representante_empresa
        fields = ['documento','nombres', 'apellidos', 'email','telefono']

class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = ['nit', 'nombre', 'link_emp', 'id_representante', 'id_forma_juridica']   

class Forma_juridicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forma_juridica
        fields = ['f_juridica']

class Usuario_desempenoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario_desempeno
        fields = ['id_area', 'id_user']

class Area_desempenoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area_desempeno
        fields = ['area']

class SeleccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seleccion
        fields = ['fecha_s', 'id_user','id_emp']

class Actividad_economicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actividad_economica
        fields = ['actividad']

class Empresa_actividadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa_actividad
        fields = ['id_empresa', 'id_actividad']