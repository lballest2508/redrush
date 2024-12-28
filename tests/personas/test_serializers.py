from apps.personas.serializers import PersonaSerializer, PerfilesSerializer, ModulosSerializer
from apps.personas.models import Persona, Perfiles, Modulos
import pytest

# Test para el serializers de personas
@pytest.mark.django_db
def test_create_persona():
    persona = Persona.objects.create(
        identificacion='1234567890',
        primer_nombre='Juan',
        primer_apellido='Perez',
        fecha_nacimiento='1990-01-01',
        genero='M',
        correo_electronico='jperez@gmail.com',
        telefono='1234567',
        direccion='Calle 123'
    )

    serializer = PersonaSerializer(persona)

    assert serializer.data == {
        'id': persona.id,
        'identificacion': '1234567890',
        'primer_nombre': 'Juan',
        'segundo_nombre': None,
        'primer_apellido': 'Perez',
        'segundo_apellido': None,
        'fecha_nacimiento': '1990-01-01',
        'genero': 'M',
        'correo_electronico': 'jperez@gmail.com',
        'telefono': '1234567',
        'direccion': 'Calle 123',
        'estado': True,
        'fecha_creacion': serializer.data['fecha_creacion'],
        'fecha_modificacion': serializer.data['fecha_modificacion'],
        'fecha_eliminacion': None,
        'password': serializer.data['password']
    }

# Test para el serializers de perfiles
@pytest.mark.django_db
def test_create_perfiles():
    perfil = Perfiles.objects.create(
        nombre='Administrador',
        descripcion='Perfil de administrador'
    )

    serializer = PerfilesSerializer(perfil)

    assert serializer.data == {
        'id': perfil.id,
        'nombre': 'Administrador',
        'descripcion': 'Perfil de administrador',
        'estado': True,
        'fecha_creacion': serializer.data['fecha_creacion'],
        'fecha_modificacion': serializer.data['fecha_modificacion'],
        'fecha_eliminacion': None
    }

# Test para el serializers de modulos
@pytest.mark.django_db
def test_create_modulos():
    modulo = Modulos.objects.create(
        nombre='Administracion',
        descripcion='Modulo de administracion'
    )

    serializer = ModulosSerializer(modulo)

    assert serializer.data == {
        'id': modulo.id,
        'nombre': 'Administracion',
        'descripcion': 'Modulo de administracion',
        'estado': True,
        'fecha_creacion': serializer.data['fecha_creacion'],
        'fecha_modificacion': serializer.data['fecha_modificacion'],
        'fecha_eliminacion': None
    }