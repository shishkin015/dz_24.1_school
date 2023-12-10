from rest_framework import serializers

from group.models import Well, Lesson


class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = ('name', 'description')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'description')
