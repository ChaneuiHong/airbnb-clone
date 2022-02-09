import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from rooms.models import Room
from users.models import Users
from lists import models as lists_models


class Command(BaseCommand):

    help = "This command creates lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many lists you want to make"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        # ㅌㅏ모델 객ㅐ
        rooms = Room.objects.all()
        users = Users.objects.all()

        # seed reviews
        seeder.add_entity(
            lists_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        created = seeder.execute()
        cleaned = flatten(created.values())

        for pk in cleaned:
            list_model = lists_models.List.objects.get(pk=pk)
            for room in rooms:
                magic_number = random.randint(1, 10)
                if magic_number % 5 == 0:
                    list_model.rooms.add(room)

        self.stdout.write(self.style.SUCCESS(f"{number} Lists created!"))
