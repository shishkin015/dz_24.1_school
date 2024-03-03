from rest_framework import viewsets, generics

from group.models import Well, Lesson
from group.permissions import IsModerator, IsModerOrOwner
from group.serializers import WellSerializer, LessonSerializer


class WellViewSet(viewsets.ModelViewSet):
    serializer_class = WellSerializer
    queryset = Well.objects.all()
    permission_classes = [IsModerator, IsModerOrOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsModerator]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsModerOrOwner]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsModerOrOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsModerOrOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsModerOrOwner]
