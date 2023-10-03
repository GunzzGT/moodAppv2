from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from utils.response import api_response

from .serializers import LoginSerializer, RefreshSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email').lower()
        password = request.data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                token_refresh = RefreshToken.for_user(user)
                token_access = str(token_refresh.access_token)
                custom_response = {'access_token': token_access, 'refresh_token': str(token_refresh), }
                return api_response('200', 'Log In Successful', custom_response)
            else:
                return api_response('400', 'Invalid credentials', status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return api_response('400', 'Email and password are required', status_code=status.HTTP_400_BAD_REQUEST)


class RefreshView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RefreshSerializer

    def post(self, request):
        refresh_token = request.data.get('refresh')

        if refresh_token:
            try:
                refresh = RefreshToken.for_user(refresh_token)
                access_token = str(refresh.access_token)

                custom_response = {'access_token': access_token, 'refresh_token': refresh_token, }
                return api_response('200', 'Refresh Successful', custom_response)
            except Exception as e:
                return api_response('400', 'Invalid refresh token', status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return api_response('400', 'Refresh token is required', status_code=status.HTTP_400_BAD_REQUEST)
