import pytest
from apps.personas.models import Persona, Perfiles, Modulos

# Test para el modelo Persona
@pytest.mark.django_db
def test_create_persona():
    # Creamos un objeto de tipo Persona
    persona = Persona.objects.create(
        identificacion='1234567890',
        primer_nombre='Juan',
        primer_apellido='Perez',
        fecha_nacimiento='1990-01-01',
        genero='M',
        correo_electronico='jperez@gmail.com',
        telefono='1234567',
        direccion='Calle 123',
        password='123456'
    )

    # Verificamos que el objeto se haya creado correctamente
    assert persona.identificacion == '1234567890'
    assert persona.primer_nombre == 'Juan'
    assert persona.primer_apellido == 'Perez'
    assert persona.fecha_nacimiento == '1990-01-01'
    assert persona.genero == 'M'
    assert persona.correo_electronico == 'jperez@gmail.com'
    assert persona.telefono == '1234567'
    assert persona.direccion == 'Calle 123'
    assert persona.password == '123456'

# Test para el modelo Perfiles
@pytest.mark.django_db
def test_create_perfiles():
    # Creamos un objeto de tipo Perfiles
    perfil = Perfiles.objects.create(
        nombre='Administrador',
        descripcion='Administrador del sistema'
    )

    # Verificamos que el objeto se haya creado correctamente
    assert perfil.nombre == 'Administrador'
    assert perfil.descripcion == 'Administrador del sistema'

# Test para el modelo Modulos
@pytest.mark.django_db
def test_create_modulos():
    # Creamos un objeto de tipo Modulos
    modulo = Modulos.objects.create(
        nombre='Seguridad',
        descripcion='Módulo de seguridad'
    )

    # Verificamos que el objeto se haya creado correctamente
    assert modulo.nombre == 'Seguridad'
    assert modulo.descripcion == 'Módulo de seguridad'