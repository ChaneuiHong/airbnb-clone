from sys import stdout
from django.core.management.base import BaseCommand
from rooms import models as rooms_models


class Command(BaseCommand):

    help = "This command creates Facilities"

    #    def add_arguments(self, parser):
    #        parser.add_argument("--times", help="This command is Room Custom Command")
    #

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for facility in facilities:
            rooms_models.Facility.objects.create(name=facility)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
