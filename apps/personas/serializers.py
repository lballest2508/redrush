from rest_framework import serializers
from .models import Persona, Perfiles, PersonasPerfiles, Modulos, PerfilesModulos

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class PerfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfiles
        fields = '__all__'

class PersonasPerfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonasPerfiles
        fields = '__all__'

class ModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulos
        fields = '__all__'

class PerfilesModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilesModulos
        fields = '__all__'