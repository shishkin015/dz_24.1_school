from rest_framework import serializers

from group.models import Well, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description', 'well', 'preview')

    def create(self, validated_data):
        well = Lesson.objects.create(**validated_data)
        return well


class WellSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson', many=True, read_only=True)

    class Meta:
        model = Well
        fields = ('name', 'description', 'preview', 'lessons_count', 'lessons')

    def get_lessons_count(self, obj):
        return obj.lesson.count()

    def create(self, validated_data):
        lesson = Well.objects.create(**validated_data)
        return lesson
