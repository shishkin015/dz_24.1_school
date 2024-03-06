from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='shishkin014@mail.ru',
            first_name='Aleksandr',
            last_name='Shishkin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123')
        user.save()