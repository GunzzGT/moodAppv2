from django.contrib.auth.hashers import make_password
from django.db.utils import DatabaseError
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from utils.response import api_response

from .models import AutoIncrementCounter
from .serializers import CustomUserSerializer


class CreateUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    def post(self, request):
        try:
            counter_object = AutoIncrementCounter.objects.get(pk=1)
        except AutoIncrementCounter.DoesNotExist:
            counter_object = AutoIncrementCounter.objects.create(pk=1, counter=0000)
        current_id = counter_object.counter
        counter_object.counter += 1

        serializer = CustomUserSerializer(data=request.data)

        try:
            if serializer.is_valid():
                serializer.validated_data['user_id'] = f"U{current_id:04}"
                password = serializer.validated_data.get('password')
                if password:
                    serializer.validated_data['password'] = make_password(password)
                serializer.save()
                counter_object.save()

                return api_response('201', 'Signup Success', result=serializer.data, status_code=status.HTTP_201_CREATED)
            else:
                error_messages = serializer.errors  # Use serializer errors
                return api_response('400', error_messages, status_code=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as db_error:
            # print db_error
            return api_response('500', 'Database error occurred', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as other_error:
            # print other_error
            return api_response('500', 'Unexpected error', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
