from django.db.utils import DatabaseError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from utils.response import api_response

from .serializers import ArticlesSerializer


class CreateArticle(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticlesSerializer

    def post(self, request):
        serializer = ArticlesSerializer(data=request.data)

        try:
            if serializer.is_valid():
                serializer.save()

                return api_response('201', 'Article Creation Success', result=serializer.data, status_code=status.HTTP_201_CREATED)
            else:
                error_messages = serializer.errors  # Use serializer errors
                return api_response('400', error_messages, status_code=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as db_error:
            # print db_error
            return api_response('500', 'Database error occurred', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as other_error:
            # print other_error
            return api_response('500', 'Unexpected error', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)