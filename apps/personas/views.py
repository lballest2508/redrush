from rest_framework import viewsets
from .models import Persona, Perfiles, PersonasPerfiles, Modulos, PerfilesModulos
from .serializers import PersonaSerializer, PerfilesSerializer, PersonasPerfilesSerializer, ModulosSerializer, PerfilesModulosSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

class Personas(viewsets.ModelViewSet):
    # Definimos la consulta que se usará para obtener los objetos de la base de datos
    queryset = Persona.objects.all()
    
    # Definimos el serializador que se usará para validar y serializar los datos
    serializer_class = PersonaSerializer

    def create(self, request, *args, **kwargs):
        # Convertimos los datos de la solicitud a un diccionario mutable
        # Esto es necesario para poder modificar los datos antes de guardarlos
        data = request.data.copy()
        
        # Verificamos si existe la clave 'password' en los datos
        if 'password' in data:
            # Encriptamos la contraseña usando make_password
            data['password'] = make_password(data['password'])
        
        # Creamos un nuevo objeto de serializador con los datos encriptados
        serializer = self.get_serializer(data=data)
        
        # Validamos los datos del serializador
        # raise_exception=True significa que se lanzará una excepción si los datos no son válidos
        serializer.is_valid(raise_exception=True)
        
        # Si los datos son válidos, se llama a perform_create para guardar el objeto en la base de datos
        self.perform_create(serializer)
        
        # Obtenemos los encabezados de éxito para la respuesta
        headers = self.get_success_headers(serializer.data)
        
        # Retornamos una respuesta con los datos del nuevo objeto creado, un estado 201 (Creado) y los encabezados
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class Perfiless(viewsets.ModelViewSet):
    queryset = Perfiles.objects.all()
    serializer_class = PerfilesSerializer

class PersonasPerfiless(viewsets.ModelViewSet):
    queryset = PersonasPerfiles.objects.all()
    serializer_class = PersonasPerfilesSerializer

class Moduloss(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    serializer_class = ModulosSerializer

class PerfilesModuloss(viewsets.ModelViewSet):
    queryset = PerfilesModulos.objects.all()
    serializer_class = PerfilesModulosSerializer

class Permisos(viewsets.ViewSet):
    def list(self, request):
        try:
            modulos_acceso = Modulos.objects.filter(
                perfilesmodulos__perfil__personasperfiles__persona=1
            ).distinct()

            if not modulos_acceso:
                return Response({'data': []}, status=status.HTTP_200_OK)
            else:
                return Response({'data': [{'id': modulo.id, 'nombree': modulo.nombre, 'descripcion': modulo.descripcion} for modulo in modulos_acceso]}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def login_view(request):
    try:
        correo_electronico = request.data.get('correo_electronico')
        password = request.data.get('password')
    
        user = Persona.objects.get(correo_electronico=correo_electronico)
    
        if user is not None:
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Persona.DoesNotExist:
        return Response({'error': 'El correo asociado no existe!'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)