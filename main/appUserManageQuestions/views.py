from admManageQuestions.models import (
    QuestionListTemplate,
    QuestionListUser,
)
from appSignUp.models import CustomUser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from utils.response import api_response

from .serializers import (
    GetCompleteQuestionListSerializer,
    UserQuestionListSerializer,
)


class CreateUserQuestionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserQuestionListSerializer

    def post(self, request, pk):
        user = request.user
        user_id = user.user_id
        try:
            CustomUser.objects.get(pk=user_id)
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
