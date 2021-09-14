from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.api.serializer import UserSerializer
from apps.users.models import User

 
#Creacion de la clase
class UserAPIView (APIView):
    #Metodo get y primera vista de rest framework
    def get(self,request):
        users = User.objects.all()                              #Consulta
        user_serializer = UserSerializer(users, many=True)      #Como se serializa
        return  Response (user_serializer.data)                 #la informacion se encuentra en data

