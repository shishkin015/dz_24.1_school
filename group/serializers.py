from rest_framework import serializers

from group.models import Well, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        course = Lesson.objects.create(**validated_data)
        return course


class WellSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson', many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Well
        fields = ('name', 'description')

    def get_lessons_count(self, instance):
        return obj.lesson.count()

    def create(self, validated_data):
        lesson = Well.objects.create(**validated_data)
        return lesson
