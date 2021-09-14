import re
from django.http.response import JsonResponse
from rest_framework.views import APIView
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
    if request.method == 'GET':
        users = User.objects.all()                              #Consulta
        user_serializer = UserSerializer(users, many=True)      #Como se serializa
        return  Response (user_serializer.data)                 #la informacion se encuentra en data"
    elif request.method =='POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors)
#        print(request.data)

