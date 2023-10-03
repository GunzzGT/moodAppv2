from admManageQuestions.models import (
    QuestionListTemplate,
    QuestionListUser,
)
from rest_framework import serializers


class GetCompleteQuestionListSerializer(serializers.ModelSerializer):
    subtitle = serializers.ListField(child=serializers.JSONField())

    class Meta:
        model = QuestionListTemplate
        fields = ['question_id', 'status', 'title', 'subtitle', ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        response_data = {
            'question_id': representation['question_id'],
            'status': representation['status'],
            'title': representation['title'],
            'subtitle': representation['subtitle'],
        }
        return response_data


class UserQuestionListSerializer(serializers.Serializer):
    question_set = serializers.ListField(child=serializers.JSONField())

    class Meta:
        model = QuestionListUser
        fields = ['user_id', 'question_set']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        response_data = {
            'user_id': representation['user_id'],
            'question_set': representation['question_set'],
        }
        return response_data
