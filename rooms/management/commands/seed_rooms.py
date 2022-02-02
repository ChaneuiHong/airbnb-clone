import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as users_models
from rooms import models as rooms_models


class Command(BaseCommand):

    help = "This command creates Rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        all_users = users_models.Users.objects.all()
        room_types = rooms_models.RoomType.objects.all()

        print(all_users)
        print(room_types)

        seeder.add_entity(
            rooms_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
                "guests": lambda x: random.randint(1, 20),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))
