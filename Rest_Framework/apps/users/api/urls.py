from django.urls import path
#from apps.users.api.api import UserAPIView Clase
from apps.users.api.api  import user_api_view, user_detail_api_view, user_test_validate

urlpatterns =[
#        path('usuario/', UserAPIView.as_view(), name='usuario_api') Clase
        path('usuario/', user_api_view, name='usuario_api'), #Funcion
        path('usuario/<int:key>/', user_detail_api_view, name='usuario_detail_api_view'),
        path('prueba_test/', user_test_validate, name='user_test_validate' ),
]
