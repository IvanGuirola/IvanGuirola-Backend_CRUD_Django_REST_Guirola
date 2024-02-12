from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from backend.serializers import UserSerializer, UserSerializerWithToken

@api_view(['POST'])
def registerUser(request):
    data = request.data
    email = (data['email']).strip().lower()
    name = (data['name']).strip()
    password = (data['password']).strip()

    try:
        user = User.objects.create(
            first_name=name,
            username=email,
            email=email,
            password=make_password(password)
        )
        serializer = UserSerializerWithToken(user, many=False)
        print(f'Usuario registrado con éxito: {email}.')
        return Response(serializer.data)
    except Exception as e:
        print(f'Error al registrar usuario: {str(e)}.')
        message = {'detail': 'La información proporcionada no es válida, revisa el formato de tu correo'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
