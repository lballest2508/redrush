import pytest
from rest_framework.test import APIClient
from apps.personas.models import Persona, Perfiles, Modulos, PersonasPerfiles, PerfilesModulos
from django.contrib.auth.hashers import make_password

# Definimos una prueba para la vista de creación de personas
@pytest.mark.django_db
def test_create_persona():
    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()
    
    # Creamos un objeto de tipo Persona
    persona = {
        'identificacion': '1234567890',
        'primer_nombre': 'Juan',
        'primer_apellido': 'Perez',
        'fecha_nacimiento': '1990-01-01',
        'genero': 'M',
        'correo_electronico': 'jperez@gmail.com',
        'telefono': '1234567',
        'direccion': 'Calle 123',
        'password': '123456'
    }

    # Hacemos una solicitud POST a la API para crear una nueva persona
    response = client.post('/api/v1/personas/', persona, format='json')

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 201

# Definimos una prueba para la lista de personas
@pytest.mark.django_db
def test_list_personas():
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

    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()
    
    # Hacemos una solicitud GET a la API para obtener la lista de personas
    response = client.get('/api/v1/personas/')

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 200

    # Verificamos que la lista de personas no esté vacía
    assert len(response.data) > 0

# Definimos una prueba para la vista de actualización de personas
@pytest.mark.django_db
def test_update_persona():
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

    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()

    # Actualizamos el correo electrónico de la persona
    persona_data = {
        'correo_electronico': 'jperez23@gmail.com',
    }

    # Hacemos una solicitud PUT a la API para actualizar la persona
    response = client.patch(f'/api/v1/personas/{persona.id}/', persona_data, format='json')

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 200

# Definimos una prueba para la creacion de perfiles
@pytest.mark.django_db
def test_create_perfil():
    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()
    
    # Creamos un objeto de tipo Perfil
    perfil = {
        'nombre': 'Administrador',
        'descripcion': 'Perfil de administrador'
    }

    # Hacemos una solicitud POST a la API para crear un nuevo perfil
    response = client.post('/api/v1/perfiles/', perfil, format='json')

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 201

# Definimos una prueba para la lista de perfiles
@pytest.mark.django_db
def test_list_perfiles():
    # Creamos un objeto de tipo Perfil
    perfil = Perfiles.objects.create(
        nombre='Administrador',
        descripcion='Perfil de administrador'
    )

    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()
    
    # Hacemos una solicitud GET a la API para obtener la lista de perfiles
    response = client.get('/api/v1/perfiles/')

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 200

    # Verificamos que la lista de perfiles no esté vacía
    assert len(response.data) > 0

# Definimos una prueba para la vista de actualización de perfiles
@pytest.mark.django_db
def test_update_perfil():
    # Creamos un objeto de tipo Perfil
    perfil = Perfiles.objects.create(
        nombre='Administrador',
        descripcion='Perfil de administrador'
    )

    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()

    # Actualizamos la descripción del perfil
    perfil_data = {
        'descripcion': 'Perfil de administrador con acceso total'
    }

    # Hacemos una solicitud PUT a la API para actualizar el perfil
    response = client.patch(f'/api/v1/perfiles/{perfil.id}/', perfil_data, format='json')

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 200

# Definimos una prueba para la creación de modulos
@pytest.mark.django_db
def test_create_modulo():
    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()
    
    # Creamos un objeto de tipo Modulo
    modulo = {
        'nombre': 'Usuarios',
        'descripcion': 'Módulo de gestión de usuarios'
    }

    # Hacemos una solicitud POST a la API para crear un nuevo módulo
    response = client.post('/api/v1/modulos/', modulo, format='json')

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 201

# Definimos una prueba para la lista de módulos
@pytest.mark.django_db
def test_list_modulos():
    # Creamos un objeto de tipo Modulo
    modulo = Modulos.objects.create(
        nombre='Usuarios',
        descripcion='Módulo de gestión de usuarios'
    )

    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()
    
    # Hacemos una solicitud GET a la API para obtener la lista de módulos
    response = client.get('/api/v1/modulos/')

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 200

    # Verificamos que la lista de módulos no esté vacía
    assert len(response.data) > 0

# Definimos una prueba para la vista de actualización de módulos
@pytest.mark.django_db
def test_update_modulo():
    # Creamos un objeto de tipo Modulo
    modulo = Modulos.objects.create(
        nombre='Usuarios',
        descripcion='Módulo de gestión de usuarios'
    )

    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()

    # Actualizamos la descripción del módulo
    modulo_data = {
        'descripcion': 'Módulo de gestión de usuarios con acceso total'
    }

    # Hacemos una solicitud PUT a la API para actualizar el módulo
    response = client.patch(f'/api/v1/modulos/{modulo.id}/', modulo_data, format='json')

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 200

# Definimos una prueba para la vista de permisos
@pytest.mark.django_db
def test_permisos():
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

    # Creamos un objeto de tipo Perfil
    perfil = Perfiles.objects.create(
        nombre='Administrador',
        descripcion='Perfil de administrador'
    )

    # Asignamos el perfil a la persona en el modelo PersonasPerfiles
    PersonasPerfiles.objects.create(
        persona=persona,
        perfil=perfil
    )

    # Creamos un objeto de tipo Modulo
    modulo = Modulos.objects.create(
        nombre='Usuarios',
        descripcion='Módulo de gestión de usuarios'
    )

    # Asignamos el módulo al perfil en el modelo PerfilesModulos
    PerfilesModulos.objects.create(
        perfil=perfil,
        modulo=modulo
    )

    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()

    # Hacemos una solicitud POST a la API para obtener los permisos de la persona
    response = client.get('/api/v1/permisos/', {'persona': persona.id})

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 200

# Definimos una prueba para la vista de autenticación
@pytest.mark.django_db
def test_authenticate():
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
        password=make_password('123456')
    )

    # Creamos un cliente para hacer solicitudes a la API
    client = APIClient()

    # Hacemos una solicitud POST a la API para autenticar a la persona
    response = client.post('/api/v1/login/', {'correo_electronico': 'jperez@gmail.com', 'password': '123456'})

    # Verificamos que la solicitud haya sido exitosa
    assert response.status_code == 200