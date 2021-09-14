from rest_framework import serializers
from apps.users.models import User

#Todos los serializadores para el modelo usuario
#Creacion del serializador nombremodeloSerializer
class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        #fields y exclude solo se puede ocupar uno 
        fields='__all__'
        #fields = ['name', 'last_name'] ---> campos especificos
