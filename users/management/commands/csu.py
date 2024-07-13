from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='emikgal2507@gmail.com',
            first_name='Admin',
            last_name='Emik',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('Emik2507')
        user.save()
