from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command is Room Custom Command"

    def add_arguments(self, parser):
        parser.add_argument("--times", help="This command is Room Custom Command")

    def handle(self, *args, **options):
        print("args: ", args)
        print("options: ", options)
        times = options.get("times")
        print("times: ", times)
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("success to make fake data!"))
