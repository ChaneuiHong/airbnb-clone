import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
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

        # room model 내 class 들
        all_users = users_models.Users.objects.all()
        room_types = rooms_models.RoomType.objects.all()
        amenities = rooms_models.Amenity.objects.all()
        facilities = rooms_models.Facility.objects.all()
        rules = rooms_models.HouseRule.objects.all()

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
        # seeder.execute의 반환값은 해당 데이터의 sequence(pk로 사용 가능)
        created_photos = seeder.execute()
        created_clean = flatten(created_photos.values())

        # Room 모델 안에 photo를 seeding 하는 작업
        # 위에서 생성된 Room을 순차적으로 실행
        for pk in created_clean:
            room = rooms_models.Room.objects.get(pk=pk)
            # photo의 개수를 랜덤으로 생성함
            for _ in range(3, random.randint(1, 10)):
                rooms_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    files=f"room_photos/{random.randint(1,31)}.webp",
                    room=room,
                )
            # Many To Many field에 seeding 하는 방법
            for a in amenities:
                magic_number = random.randint(1, 10)
                if magic_number % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(1, 10)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in rules:

                magic_number = random.randint(1, 10)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))
