from django.core.management.base import BaseCommand, CommandError
from scratchapi.models import User
import csv


class Command(BaseCommand):
    help = "This will load test data to scratch api"

    def handle(self, *args, **options):
        input_file = csv.DictReader(open("data/data.csv"))
        for row in input_file:
            # print (row)
            # print("success")
            User.objects.create(id=row["id"], name=row["name"])
