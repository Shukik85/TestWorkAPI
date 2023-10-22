import restquiz
from restquiz.models import Categoryes, Quiz
from rest_framework import serializers


class CategorySerialiser(serializers.ModelSerializer):
    title = serializers.CharField()
    class Meta:
        model = Categoryes
        fields = ["title",]
        validators=[]

    def create(self, validated_data):
        category_data = validated_data
        category,answer = Categoryes.objects.get_or_create(title = category_data['title'])
        return category



class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerialiser(required=False)
    id = serializers.IntegerField(source='question_id')
    class Meta:
        model = Quiz
        fields = ['id', "airdate", 'category', 'question', 'answer', 'value']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category,answer = Categoryes.objects.get_or_create(title = category_data['title'])
        quiz,answer = Quiz.objects.get_or_create(category=category, **validated_data)
        return {"answer": answer}
