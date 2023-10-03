from appSignUp.models import CustomUser
from django.db.utils import DatabaseError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from utils.response import api_response

from .models import (
    QuestionListTemplate,
    QuestionListUser,
)
from .serializers import (
    DailyQuestionSerializer,
    QuestionListSerializer,
    GetCompleteQuestionListSerializer,
    UserQuestionListSerializer,
)


class CreateQuestionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionListSerializer

    def get(self, request):
        result = QuestionListTemplate.objects.all()
        serializer = GetCompleteQuestionListSerializer(result, many=True)
        return api_response('200', 'Success', result=serializer.data)

    def post(self, request):
        serializer = QuestionListSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return api_response('201', 'Create new question set Success', result=serializer.data,
                                    status_code=status.HTTP_201_CREATED)
            else:
                error_messages = serializer.errors
                return api_response('400', error_messages, status_code=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as db_error:
            return api_response('500', 'Database error occurred', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as other_error:
            return api_response('500', other_error, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FillQuestionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DailyQuestionSerializer

    def post(self, request, pk):
        try:
            question_list = QuestionListTemplate.objects.get(pk=pk)
        except QuestionListTemplate.DoesNotExist:
            return api_response('404', 'Question set does not exist', status_code=status.HTTP_404_NOT_FOUND)

        serializer = DailyQuestionSerializer(data=request.data)
        try:
            if serializer.is_valid():
                data = serializer.validated_data

                question_data = {'pertanyaan': data['pertanyaan'], 'jawaban': '-', 'deskripsi': '-', }

                question_list.subtitle.append(question_data)

                question_list.save()

                newserializer = QuestionListSerializer(question_list)

                return api_response('201', 'Create new question set Success', result=newserializer.data,
                                    status_code=status.HTTP_201_CREATED)
            else:
                error_messages = serializer.errors
                return api_response('400', error_messages, status_code=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as db_error:
            return api_response('500', 'Database error occurred', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as other_error:
            return api_response('500', str(other_error), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateUserQuestionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserQuestionListSerializer

    def post(self, request, pk):
        try:
            CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return api_response('404', 'User Not Found', status_code=status.HTTP_404_NOT_FOUND)

        try:
            userobject = QuestionListUser.objects.get(pk=pk)
        except QuestionListUser.DoesNotExist:
            userobject = QuestionListUser.objects.create(pk=pk)

        original_data = QuestionListTemplate.objects.all()
        serializerized = GetCompleteQuestionListSerializer(original_data, many=True)
        serialized_data = serializerized.data

        for item in serialized_data:
            userobject.question_set.append(item)
            userobject.save()

        return api_response('201', 'Create new question set Success', status_code=status.HTTP_201_CREATED)
