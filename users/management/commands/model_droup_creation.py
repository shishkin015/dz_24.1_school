from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from group.models import Well, Lesson


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        moderator_group, created = Group.objects.get_or_create(name='Модераторы')

        lesson_content_type = ContentType.objects.get_for_model(Lesson)
        well_content_type = ContentType.objects.get_for_model(Well)

        view_lesson_permission = Permission.objects.get(content_type=lesson_content_type, codename='view_lesson')
        change_lesson_permission = Permission.objects.get(content_type=lesson_content_type, codename='change_lesson')
        view_well_permission = Permission.objects.get(content_type=well_content_type, codename='view_well')
        change_well_permission = Permission.objects.get(content_type=well_content_type, codename='change_well')

        moderator_group.permissions.add(view_lesson_permission, change_lesson_permission,
                                        view_well_permission, change_well_permission)