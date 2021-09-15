from os import stat
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.users.api.serializer import UserSerializer
from apps.users.models import User
#Con decorador
from rest_framework.decorators import api_view
 
#Creacion de la clase
"""class UserAPIView (APIView):
    #Metodo get y primera vista de rest framework
    def get(self,request):
        users = User.objects.all()                              #Consulta
        user_serializer = UserSerializer(users, many=True)      #Como se serializa
        return  Response (user_serializer.data)                 #la informacion se encuentra en data"""

#Decorador
@api_view(['GET', 'POST'])
def user_api_view(request):
    #Consulta
    if request.method == 'GET':
        users = User.objects.all()                              #Consulta
        user_serializer = UserSerializer(users, many=True)      #Como se serializa
        return  Response (user_serializer.data, status=status.HTTP_200_OK)                 #la informacion se encuentra en data"

    #Creacion                       CREATE
    elif request.method =='POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message':'No se pudo realizar la accion'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, key=None):
    #Forma correcta de utilizar rest framework
    #Consulta a la BD
    user = User.objects.filter(id=key).first()

    if user:
        #Metodo get                             READ 
        if request.method =='GET':
            user_serializer= UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
    
        #Metodo put para modificar la informacion   UPDATE
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user,data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        #Metodo para eliminar                       DELETE
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Eliminado'}, status=status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado el usuario'}, status=status.HTTP_400_BAD_REQUEST)
