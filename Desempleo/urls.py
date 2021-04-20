from django.urls import include, path
#from .views import HomePageView, AboutPageView

from rest_framework import routers

from .views import  UsuariosViewSet, Nivel_estudioViewSet, FormacionViewSet, Representante_empresaViewSet, EmpresaViewSet, Forma_juridicaViewSet, Usuario_desempenoViewSet,Area_desempenoViewSet, SeleccionViewSet, Actividad_economicaViewSet, Empresa_actividadViewSet

router = routers.DefaultRouter()
router.register('usuario', UsuariosViewSet)
router.register('nivel_estudio', Nivel_estudioViewSet)
router.register('formacion', FormacionViewSet)
router.register('representante_empresa', Representante_empresaViewSet)
router.register('empresa', EmpresaViewSet)
router.register('forma_juridica', Forma_juridicaViewSet)
router.register('usuario_desempeno', Usuario_desempenoViewSet)
router.register('area_desempeno', Area_desempenoViewSet)
router.register('seleccion', SeleccionViewSet)
router.register('actividad_economica', Actividad_economicaViewSet)
router.register('empresa_actividad', Empresa_actividadViewSet)

urlpatterns = [

    path('api/v1/', include(router.urls)),

    
]