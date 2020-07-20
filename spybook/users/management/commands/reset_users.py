from django.core.management.base import BaseCommand, CommandError

from ...models import Driver, Spy, User


class Command(BaseCommand):
    help = "Adds a few base users"

    def handle(self, *args, **options):
        User.objects.all().delete()
        Spy.objects.create(
            username="daniel", email="daniel@feldroy.com", type=User.Types.SPY
        )
        Driver.objects.create(
            username="audrey", email="audrey@feldroy.com", type=User.Types.DRIVER
        )
        Driver.objects.create(
            username="uma", email="uma@feldroy.com", type=User.Types.DRIVER
        )
        self.stdout.write(self.style.SUCCESS("Users reset"))

