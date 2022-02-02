from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as users_models


class Command(BaseCommand):

    help = "This command creates Ameities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users you want to create?"
        )

    def handle(self, *args, **options):
        # --number 커멘드로 받은 정수를 넘겨받음
        number = options.get("number")
        seeder = Seed.seeder()

        # make the fake data by using Seed()
        seeder.add_entity(
            users_models.Users,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} Users created"))
