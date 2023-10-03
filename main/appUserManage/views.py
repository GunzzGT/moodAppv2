from appSignUp.models import CustomUser
from appSignUp.serializers import CustomUserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from utils.response import api_response


class ViewSelf(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get(self, request):
        user = request.user
        user_id = user.user_id
        try:
            user = CustomUser.objects.get(pk=user_id)
            serializer = CustomUserSerializer(user)
            return api_response('200', 'Success', result=serializer.data)
        except CustomUser.DoesNotExist:
            return api_response('404', 'User Not Found', status_code=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        user = request.user
        user_id = user.user_id
        try:
            data = request.data
            user = CustomUser.objects.get(pk=user_id)

            user.name = data.get('name', user.name)
            user.nickname = data.get('nickname', user.nickname)
            user.telephone = data.get('telephone', user.telephone)
            user.address = data.get('address', user.address)
            user.gender = data.get('gender', user.gender)
            user.date_birth = data.get('date_birth', user.date_birth)
            user.save()
            serializer = CustomUserSerializer(user)
            return api_response('200', 'Success', result=serializer.data)
        except CustomUser.DoesNotExist:
            return api_response('404', 'User Not Found', status_code=status.HTTP_404_NOT_FOUND)
