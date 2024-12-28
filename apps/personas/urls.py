from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Personas, Perfiless, PersonasPerfiless, Moduloss, PerfilesModuloss, Permisos, login_view

# Crea una instancia del router
router = DefaultRouter()
# Registra el ViewSet
router.register(r'personas', Personas, basename='persona')
router.register(r'perfiles', Perfiless, basename='perfil')
router.register(r'personas_perfiles', PersonasPerfiless, basename='persona_perfil')
router.register(r'modulos', Moduloss, basename='modulo')
router.register(r'perfiles_modulos', PerfilesModuloss, basename='perfil_modulo')
router.register(r'permisos', Permisos, basename='permisos')

# Usa el router para las URLs
urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
]