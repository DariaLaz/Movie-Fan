from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import status
from ..serializers.auth_serializers import UserLoginSerializer, UserRegisterSerializer
from django.contrib.auth.models import User


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)

    
class LoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            try:
                serializer.validate(request.data)
                user = User.objects.get(username=serializer.data.get('username'))
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'username': serializer.data.get('username'),
                    'user_id': user.id
                }, status=status.HTTP_200_OK)
            except:
                return Response({"detail": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
           
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    
class RegisterView(APIView):
    serializer_class = UserRegisterSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)