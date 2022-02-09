import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms.models import Room
from users.models import Users
from reviews import models as reivews_models


class Command(BaseCommand):

    help = "This command creates Reivews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many reviews you want to make"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        # ㅌㅏ모델 객ㅐ
        rooms = Room.objects.all()
        users = Users.objects.all()

        # seed reviews
        seeder.add_entity(
            reivews_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(1, 5),
                "communication": lambda x: random.randint(1, 5),
                "cleanliness": lambda x: random.randint(1, 5),
                "location": lambda x: random.randint(1, 5),
                "check_in": lambda x: random.randint(1, 5),
                "value": lambda x: random.randint(1, 5),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Reviews created!"))
