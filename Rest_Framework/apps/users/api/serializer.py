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
 
#Clase creada manualmente y validada correctamente mediane las opciones que da Serializer
class TestUserSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=200) 
    email= serializers.EmailField()

    def validate_name(self, value):
        if 'develops' in value:
            return serializers.ValidationError('Error')
        print(value)
        return value

    def validate_email(self, value):
        if '@ues.edu.sv' is not value:
            print("Es un correo institucional")
        else:
            print("No es un correo institucional")
            raise serializers.ValidationError("No es un correo institucional")
        return value

    def validate(self, data):
        print("Data validate correctly")
        return data
